#!/usr/bin/env python
import sys
import psycopg2.extras

#   ____________________________________________________________________________
#
#   SQL Database static class to be used in DB-intensive applications
#   which always work with one connection to a host/database. A default
#   DB connection is raised and held open until explicitly closed,
#   only one SQL command is being processed at a time, etc.
#   ____________________________________________________________________________
class Db:
	connect_str = ""
	connect_handle = None
	sql_text = ""
	sql_args = {}


	#   ________________________________________________________________________
	#
	#   Connect to host/database
	#   ________________________________________________________________________
	@classmethod
	def open(cls, pCnStr):
		cls.connect_str = pCnStr
		cls.connect_handle = psycopg2.connect(pCnStr)


	#   ________________________________________________________________________
	#
	#   Close the connection by disconnecting from host/database
	#   ________________________________________________________________________
	@classmethod
	def close(cls):
		if cls.connect_handle is not None:
			cls.connect_handle.close()


	#   ________________________________________________________________________
	#
	#   Set/continue SQL command text and arguments for the default SQL command
	#   The default SQL command is the comman that is run for SQL code
	#   execution methods, such as select - it is the primary means to
	#   enter SQL commands.
	#   ________________________________________________________________________
	@classmethod
	def sql(cls, text=None, args=None, cont=False):
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


	#   ________________________________________________________________________
	#
	#   Clear the SQL command text and arguments for the Default SQL command
	#   ________________________________________________________________________
	@classmethod
	def sql_new(cls, text=None, args=None):
		cls.sql(text=text, args=args, cont=False)
		return cls.sql_text


	#   ________________________________________________________________________
	#
	#   Continue SQL command text and arguments for the default SQL command
	#   ________________________________________________________________________
	@classmethod
	def sql_add(cls, text=None, args=None):
		cls.sql(text=text, args=args, cont=True)
		return cls.sql_text


	"""#   ________________________________________________________________________
	#
	#   Set SQL command arguments for the default SQL command
	#   ________________________________________________________________________
	@classmethod
	def sql_args(cls, args):
		argsDict = args
		return args
	"""

	#   ________________________________________________________________________
	#
	#   Run a SQL command and return rows in a Python Dictionary format
	#   one would expect from a SQL Select statement
	#   ________________________________________________________________________
	@classmethod
	def execute(cls, text=None, args=None):
		result = cls.connect_handle.cursor()

		if text is None:
			text = cls.sql_text
		if args is None:
			args = cls.sql_args

		result.execute(text, args)
		cls.sql_new()
		return result


	#   ________________________________________________________________________
	#
	#   Run a SQL command and return rows in a Python Dictionary format
	#   one would expect from a SQL Select statement
	#   ________________________________________________________________________
	@classmethod
	def select(cls, text=None, args=None,):
		result = cls.connect_handle.cursor(
				  cursor_factory=psycopg2.extras.DictCursor)

		if args is None:
			args = cls.sql_args
		if text is None:
			text = cls.sql_text
			cls.sql_new()

		result.execute(text, args)
		return result


	#   ________________________________________________________________________
	#
	#   Run a SQL command and return value from the first row
	#   Used for single scalar-value selects or function calls
	#   ________________________________________________________________________
	@classmethod
	def select_value(cls, text=None, args=None,):
		cmd = "SELECT (" + text + ") AS result LIMIT 1"
		for row in cls.select(cmd, args):
			result = row["result"]
		return result


	#   ________________________________________________________________________
	#
	#   SQL commit
	#   ________________________________________________________________________
	@classmethod
	def commit(cls):
		connect_handle.commit()
		return


	#   ________________________________________________________________________
	#
	#   SQL rollback
	#   ________________________________________________________________________
	@classmethod
	def rollback(cls):
		connect_handle.rollback()
		return
