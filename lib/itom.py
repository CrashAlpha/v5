import re
from base import *
from db import *

class Itom(object):
	"""impt Template Object Model member object
	
		Naming convention for impt members:
			objects:		the impt class name with a leading underscore,
							all lower-case as per the python naming convention for
							private class members. A get/set @property method is 
							declared without the leading underscore (i.e. the member 
							object class name, all lowercase). 
			fields:		the impt member field name, all lowercase with no leading
							underscore as per the python naming convention for public
							members as well as no trailing underscore.
			metadata:	information about the object other than member objects
							and fields will be held in a variable named "meta" from
							class "Meta". These names are the only ones allowed in impt 
							objects/classes that are NOT the names of impt members.
							Therefore, "meta" is considered a reserved word and no
							impt member may be named "meta".
			classes:		python member class declarations corresponding to impt
							objects names are the same as their impt class name with the
							first letter being shifted to uppercase as per the python
							naming convention for public class members. Every class has a
							nested class named "Meta" to hold additional data other than
							member classes and fields.
	"""

	#  Class variables
	echo_status = False
	document = None

	def __init__(self, p_path=None, p_index=None):
		if p_path is None:
			self.meta = None
		else:
			self.meta = Itom.Meta(p_path, p_index)
		return

	def echo(self, args):
		"""Itom class echo for printing Itom-operations"""
		if Itom.echo_status:
			echo(args)
		return

	@staticmethod
	def parent_path_text(p_path_text):
		"""Return the parent path text of a path's text"""
		return re.sub(r"(.*)\.(.*)", r"\1", p_path_text)

	def has_member(self, p_member_name, p_index=None):
		"""Given a name and optionally an index, find out if this record
		has an impt-member object or field of that name/index
		"""
		result = False
		key = '_' + p_member_name
		
		if key in self.__dict__:
			result = True

			if p_index is not None and p_index not in self.__dict__[key].keys():
				result = False

		return result

	def get_member(self, p_member_name, p_index=None):
		"""Given a name and optionally an index, return the contents of 
		an impt-member object or field with that name/index
		"""
		result = None
		
		if self.has_member(p_member_name, p_index):
			key = '_' + p_member_name		
			result = self.__dict__[key]

			if p_index is not None:
				result = result[p_index]

		return result

	def has_active_object(self, p_member_name, p_index=None):
		"""Given a name and optionally an index, find out if this record
		has an active impt-member object of that name/index
		"""
		
		if p_member_name in self.meta.active_objects:
			result = self.has_member(p_member_name, p_index)
		else:
			result = False

		return result

	def has(self, p_member_name, p_index=None):
		"""Synonym for has_active_object to improve code legibility"""
		
		if p_member_name in self.meta.active_objects:
			result = self.has_member(p_member_name, p_index)
		else:
			result = False

		return result

	def get_active_object(self, p_member_name, p_index=None):
		"""Given a name and optionally an index, return the contents of 
		an impt-member object collection that name/index or object record
		with that name and index
		"""
		
		if self.has_active_object(p_member_name, p_index):					
			result = self.get_member(p_member_name, p_index)
		else:
			result = None

		return result

	def set_field(self, p_field_name, p_value):
		"""Set an impt field, making sure it's active and in the read map"""
		field_key = '_' + p_field_name
		self.__dict__[field_key] = p_value

		# Field not yet active? Make it active and update any active read map
		if p_field_name not in self.meta.active_fields:
			self.meta.active_fields.append(p_field_name)
			
			# Active document found?
			# Make sure this field is included in the read map so that
			# it's cleared with every impt table row read
			if Itom.document is not None:
				document = Itom.document
				path_text = self.meta.path.text + "." + p_field_name
				path = document.path_from_text(path_text)				
				entry = document.ReadMapEntry(None, path)
				entry_key = "*" + path_text
				read_map = document.meta.read_map
				read_map[entry_key] = entry
				pass

	def set_collapse_not_indexed(self, p_value):
		"""Set flag to indicate whether this object and
		its member objects should collapse indexes
		- a collapsed index is a path notation method
		  which does not require that an object record
		  include an index if it is known to be the only
		  object in the collection, and its index key is 0.
		  Use this for V4 impt compatability and easier coding.
		  See member field @property defs for its implementation.
		"""
		self.meta.collapse_not_indexed = p_value
		for member in self.meta.active_objects:
			exec_str = "indexes = self.%s_indexes()" % (member)
			exec exec_str
			for idx in indexes:
				exec_str = "self._%s[%i].set_collapse_not_indexed(%s)" \
						% (member, idx, p_value)
				exec exec_str
		return

	#
	#  Itom nested-classes
	#

	class Meta(object):
		"""Meta data describing impt-object
		"""

		class Core(object):
			"""This Itom.Core record's DB relation information
			in the core schema
			"""

			class Meta:
				"""Itom.meta.Core meta data describing core-object"""

				def __init__(self, p_class_code):
					"""Itom.meta.Core.meta constructor"""
					self.class_code = p_class_code
					self.context = None
					self.table_name = None
					self.pkey_column_name = None
					self.pkey_value = None
					self.active_columns = []

			def __init__(self, p_class_code):
				"""Itom.meta.Core constructor"""
				self.meta = self.Meta(p_class_code)

		def __init__(self, p_path_text, p_index, p_is_indexed=False):
			"""Itom.meta Constructor"""
			self.index = p_index
			self.path = ItomDoc.Path()
			self.path.text = p_path_text
			self.path.record = self
			self.path.type = "record"
			self.context = re.sub(r"\[[0-9]\]", "", p_path_text)
			self.name = re.sub(r"(.*)\.(.*)", r"\2", self.context)
			self.core = None
			self.active_objects = []
			self.active_fields = []
			self.is_indexed = p_is_indexed
			self.is_root = False
			self.collapse_not_indexed = True
			self.parent_record = None
			return


		@property
		def type(self):
			"""What type of impt table is this?
				Only applies to document
				"P" is a pro (provider) import
				"F" is a facil (facility) import
				None is "cannot be determined"
			"""
			result = None

			if self.is_root:
				if "pro" in self.active_objects:
					result = "P"
				if result is None and "facil" in self.active_objects:
					result = "F"

			return result

		def active_objects_add(self, p_member_code):
			"""Add the class name of a member object to the active objects list
			so we know which member objects have actually been declared
			"""
			self.active_objects.append(p_member_code)
			return

		def active_objects_add_new(self, p_member_code):
			"""Add the class name of a member object to the active objects list
			if not already in the list
			"""
			if p_member_code not in self.active_objects:
				self.active_objects_add(p_member_code)
			return

		def active_fields_add(self, p_member_code):
			"""Add the name of a member field to the active fields list
			so we know which fields have actually been declared
			"""
			self.active_fields.append(p_member_code)
			return

		def active_fields_add_new(self, p_member_code):
			"""Add the name of a member field to the active fields list
			#  if not already in the list
			"""
			if p_member_code not in self.active_fields:
				self.active_fields_add(p_member_code)
			return

		def parent_path_text(self):
			"""Get the parent path of the current object"""
			return Itom.parent_path_text(self.path.text)


class ItomDoc(Itom):
	"""impt Template Object Model root Document
	"""

	class ReadMapEntry:
		"""A single entry in the dictionary used to map data to set
		(typically, impt table fields) to items in the impt document tree
		"""

		def __init__(self, p_column_name, p_path):
			"""ItomDoc.ReadMapEntry constructor"""
			self.column_name = p_column_name
			self.path = p_path
			self.field = p_path.field
			# self.exec_str = None

	def __init__(self, p_path_text=None):
		"""ItomDoc constructor"""
		if p_path_text is None:
			p_path_text = "impt"
		Itom.__init__(self, p_path_text)
		self.meta.id = None
		self.input_source_id = None
		self.meta.ident_type_id = None
		self.meta.is_root = True
		self.meta.read_map = None
		self.meta.table = None
		# self.meta.exec_read = None
		self.meta.open_fail_messages = []
		return

	def open(self, p_table):
		"""Open the document, prepare it then load an impt table's column
		data into a load map which contains the impt column names and the
		related path to itom paths to fields in the document.
		The read method  uses this map to read each impt row's column and assign
		its value to the itom field.
		"""
		Itom.document = self
		self.meta.table = p_table
		self.meta.id = None
		self.meta.read_map = {}

		# Find the input source and its source id, default identifier type
		# and properties of the impt table
		row = Db.select_top("""
			SELECT input_source_id, properties
			FROM mdx_core.input_resource
			WHERE
			(
			   CASE
			   WHEN resource LIKE '%%.%%' THEN '' 
			   ELSE 'mdx_import.'
			   END || resource
			) = %s""", (self.meta.table,))
		if row == None:
			raise ValueError(
					"Cannot find input_resource for impt table %s",
					(self.meta.table,))

		self.meta.ident_type_id = Db.select_value("""
			SELECT identifier_type_id
			FROM mdx_taxa.identifier_type
			WHERE input_source_id = %s""", (row['input_source_id'],))
		

		# Create a local variable that has the same name as the
		# document name (kinda dangerous!) as the load map is meant
		# to be readable and should use the actual document name,
		# not "self"
		doc_obj_name = self.meta.name
		exec "%s = self" % doc_obj_name
		Db.sql("""
				 SELECT * FROM mdx_lib.impt_table_parse_elements(%(imptTable)s)
				 ORDER BY ordinal_position, element_ordinal_position""",
				{"imptTable": self.meta.table}
		)

		skip_row = False
		is_error = False

		# Read in the elements, render as iTOM paths
		# off of the document root
		for row in Db.select():

			# First element? New path off of base
			# A "direct path" accesses the objects hidden member attributes
			# so the load map is not confused by path-mangling conditions
			# such as collapse_not_indexed
			if row['element_ordinal_position'] == 1:
				# Release persistent skip
				skip_row = False
				prv_path = doc_obj_name
				prv_direct_path = doc_obj_name

			# Element should skip? Configure 'from' reason
			if not row['is_valid'] or row['element_code'] == "extra":
				# Skip persists until this path is done
				skip_row = True

				if not row['is_valid']:
					is_error = True
					msg = "Failing"
					self.meta.open_fail_messages.append(msg)
				else:
					msg = "Ignoring"

			if skip_row:
				self.echo("%s %s for %s" % (msg, row['column_name'], row['element_code']))
				continue

			exec_str = ""

			# Object element? Keep building the path until we hit a field
			if row['element_type_code'] == "object":

				if row['element_code'] <> "impt":
					obj = row['element_code']
					rec = "self.%s()" % row['element_code'].capitalize()
					idx = row['element_index']
					path = prv_path + ".%s[%d]" % (obj, idx)
					direct_path = prv_direct_path + "._%s[%d]" % (obj, idx)
					# add_obj = '%s_add_new(%s, "%s", %d)' % (obj, rec, path, idx)
					add_obj = "%s_add_new(%s, %d)" % (obj, rec, idx)
					exec_str += "%s.%s\n" % (prv_direct_path, add_obj)

					prv_path = path
					prv_direct_path = direct_path

			# Field element? Should be final element in the path
			elif row['element_type_code'] == "field":
				entry = self.ReadMapEntry(row['column_name'], self.Path())
				#entry.path.text = "%s.%s" % (prv_direct_path, row['element_code'])
				entry.path.text = "%s.%s" % (prv_path, row['element_code'])
				self.meta.read_map[row['column_name']] = entry
				exec_str += '%s.meta.active_fields_add_new("%s")\n' \
						% (prv_direct_path, row['element_code'])
				exec_str += '%s.meta.collapse_not_indexed = %s' \
						% (prv_direct_path, self.meta.collapse_not_indexed)
			else:
				raise ValueError("Unexpected element_type_code '%'" \
						% row['element_type_code'])

			# Document building script created? Execute it
			if exec_str <> "":
				# echo(exec_str)
				exec exec_str
		
		# Redefine the load map entries, converting the path
		# from a field type to a record type and
		# then assigning the path to the document record
		# where it belongs
		for col, entry in impt.meta.read_map.iteritems():

			# Render the full path object from the partial object's path text
			# already in the load map, convert it to a record
			path_text = entry.path.text
			entry.path = self.path_from_text(path_text)
			entry.field = entry.path.field
			entry.path.field = None
			entry.path.type = "record"

			# Find the parent record of this record,
			# iterate through all parents making sure thay have references to
			# their parents; as we are iterating backwards through the path
			# save the list of record references to later iterate forward
			# through the path and build the core contexts for each record
			records = []
			child = entry.path.record
			while child.meta.name <> self.meta.name:
				records.insert(0, child)
				parent = child.meta.parent_record

				if parent is None:
					path_text = Itom.parent_path_text(child.meta.path.text)
					# Indirect?
					parent = self.path_from_text(path_text).record
					child.meta.parent_record = parent

				child = parent

			# Update all records referenced in the path that don't have
			# core contexts yet
			core_class_codes = []
			for rec in records:

				if rec.meta.core.meta.class_code is None:
					continue

				core_class_codes.append(rec.meta.core.meta.class_code)
				core_context = ".".join(core_class_codes)

				# Rename contexts in special cases
				if core_context == "provider.practice.facility":
					core_context = "facility"
				elif core_context == "provider.practice.facility.address":
					core_context = "facility.address"
				elif core_context == "provider.practice.facility.address.phone":
					core_context = "provider.practice.phone"

				if rec.meta.core.meta.context is None:
					rec.meta.core.meta.context = core_context
					core_table_name = core_context.replace(".", "_")
					rec.meta.core.meta.table_name = core_table_name
					rec.meta.core.meta.pkey_column_name = core_table_name + "_id"
					rec.meta.core.meta.pkey_column_value = None
		
		return

	def close(self):
		"""Close the document, deallocate resources in use"""
		self.meta.read_map = None
		self.meta.table = None
		self.meta.exec_read = None

		for field in self.meta.active_fields:
			delattr(self, "_" + field)

		for obj in self.meta.active_objects:
			delattr(self, "_" + obj)

		delattr(self, "meta")
		return

	def read(self, p_row):
		"""Read a dictionary whose keys are impt column names and
		load them into the iTOM document
		"""
		self.meta.id = p_row['impt_id']

		# Iterate through the load map entries and assign
		# field values, reset core values in each record
		# declared in the map entry's path
		for col, entry in self.meta.read_map.iteritems():

			# No column name in the read map entry?
			# This came from a manual impt field setting and impt field
			# should be cleared with each read of the impt table
			if entry.column_name is None:
				value = None
			else:
				value = p_row[entry.column_name]
				
			record = entry.path.record
			field = entry.field
			record.__dict__[field] = value
			if record.meta.core is not None:
				record.meta.core.meta.pkey_value = None

		return


	class Path:
		"""Rendering of a path from its text format to its
		to an object representing the member information
		about its type, as well as references to itself within
		the document including collection and record.
		"""
		def __init__(self):
			self.record = None
			self.collection = None
			self.field = None
			self.text = None
			self.value = None
			self.type = None
			self.document = None

	def path_from_text(self, p_path_text):
		"""Perform the path breakdown from the path text to a python object
		(not an impt-object) rendering the data to describe the impt-field or
		impt-object named in the path text.
		"""

		# Default return state for empty document
		result = ItomDoc.Path()
		result.collection = None
		result.record = self
		result.field = None
		result.text = p_path_text
		result.type = "document"
		result.document = self

		# Iterate through path parts
		i = 0
		is_root = self.meta.is_root
		obj_name = ""
		prv_type = result.type
		d_path =  re.split("(?:[\.\[\]]+)", p_path_text)
		n_last = len(d_path)

		for part in d_path:
			i += 1

			if part <> "":
				if prv_type == "collection":
					result.type = "record"
					record_idx = int(part)
					result.record = result.collection[record_idx]
				else:
					if is_root:
						result.type = "document"
						is_root = False
					else:

						if part in result.record.meta.active_fields \
								and i == n_last:
							result.type = "field"
							result.field = "_" + part
							result.value \
									= result.record.__dict__[result.field]
						else:

							# Part not a direct path element? Make it one
							if part[0] <> "_":
								obj_name = "_" + part
							else:
								obj_name = part

							result.type = "collection"
							result.collection \
									= result.record.__dict__[obj_name]
							result.record = None

				prv_type = result.type

		return result
