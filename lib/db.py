#!/usr/bin/env python
import sys
import psycopg2.extras

class Db:
	"""
	SQL Database static class to be used in DB-intensive applications
	which always work with one connection to a host/database. A default
	DB connection is created and held open until explicitly closed,
	only one SQL command is being processed at a time, etc.

	"""
	connect_str = ""
	connect_handle = None
	sql_text = ""
	sql_args = {}


	@classmethod
	def open(cls, pCnStr):
		"""
		Connect to host/database
		"""
		cls.connect_str = pCnStr
		cls.connect_handle = psycopg2.connect(pCnStr)


	@classmethod
	def close(cls):
		"""
		Close the connection by disconnecting from host/database
		"""
		if cls.connect_handle is not None:
			cls.connect_handle.close()


	@classmethod
	def sql(cls, text=None, args=None, cont=False):
		"""
		Set/continue SQL command text and arguments for the default SQL command
		The default SQL command is the comman that is run for SQL code
		execution methods, such as select - it is the primary means to
		enter SQL commands.
		"""
		if (text is not None):
			if not cont:
				cls.sql_text = ""
				cls.sql_args = {}
			elif cls.sql_text != "":
				text += "\n"
			cls.sql_text += text

		if (args is not None):
			if cont:
				cls.sql_args.update(args)
			else:
				cls.sql_args = args

		return cls.sql_text


	@classmethod
	def sql_new(cls, text=None, args=None):
		"""
		Clear the SQL command text and arguments for the Default SQL command
		"""
		cls.sql(text=text, args=args, cont=False)
		return cls.sql_text


	@classmethod
	def sql_add(cls, text=None, args=None):
		"""
		Continue SQL command text and arguments for the default SQL command
		"""
		cls.sql(text=text, args=args, cont=True)
		return cls.sql_text


	"""
	#   ________________________________________________________________________
	#
	#   Set SQL command arguments for the default SQL command
	#   ________________________________________________________________________
	@classmethod
	def sql_args(cls, args):
		argsDict = args
		return args
	"""

	@classmethod
	def execute(cls, text=None, args=None):
		"""
		#
		Run a SQL command and return rows in a Python Dictionary format
		one would expect from a SQL Select statement
		"""
		result = cls.connect_handle.cursor()

		if text is None:
			text = cls.sql_text
		if args is None:
			args = cls.sql_args

		result.execute(text, args)
		cls.sql_new()
		return result


	@classmethod
	def select(cls, text=None, args=None,):
		"""
		#
		Run a SQL command and return rows in a Python Dictionary format
		one would expect from a SQL Select statement
		"""
		result = cls.connect_handle.cursor(
				  cursor_factory=psycopg2.extras.DictCursor)

		if args is None:
			args = cls.sql_args
		if text is None:
			text = cls.sql_text
			cls.sql_new()

		result.execute(text, args)
		return result


	@classmethod
	def select_top(cls, text=None, args=None,):
		"""
		Run a SQL command and return the top row in a Python Dictionary format
		one would expect from a SQL Select statement
		"""
		result = None
		for row in cls.select(text, args):
			result = row
			break
		
		return result

	@classmethod
	def select_value(cls, text=None, args=None,):
		"""
		Run a SQL command and return value from the first row
		Used for single scalar-value selects or function calls
		"""
		if args is None:
			args = cls.sql_args
		if text is None:
			text = cls.sql_text
			cls.sql_new()
			
		cmd = "SELECT (" + text + ") AS result LIMIT 1"
		for row in cls.select(cmd, args):
			result = row["result"]
		return result


	@classmethod
	def commit(cls):
		"""
		SQL commit
		"""
		connect_handle.commit()
		return


	@classmethod
	def rollback(cls):
		"""
		SQL rollback
		"""
		connect_handle.rollback()
		return


	@classmethod
	def int_scope_expr(cls, p_str):
		"""
		Convert a string to a scope expression assuming integer values,
		using =, BETWEEN or IN clause depending on the format of the string
		passed.
		If the string looks like:
			-	integers separated by commas an IN expression is generated,
				e.g. 12345,12346,12347
			-	a pair of integers seperated by spaces, a BETWEEN expression is
				generated, e.g. 12345-67890		
			-	else (assuming a single integer value) an = expression is
				generated, e.g. 12345
		"""

		if "-" in p_str:
			vals = p_str.split("-")
			result = "BETWEEN %s AND %s" % (vals[0], vals[1])
		elif "," in p_str:
			result = "IN (%s)" % (p_str,)
		else:
			result = "= %s" % (p_str,)

		return result
