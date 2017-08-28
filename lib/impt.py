#
# Impt class ORM based on the Import Template Object Model (iTOM) generated on 2017-08-24 17:04:27.83418-04
from itom import *

# Import Template object
class Impt(ItomDoc):

	def __init__(self, p_path=None):
		ItomDoc.__init__(self, p_path)

		# impt-field type members
		self._date = None
		self._facility_id = None
		self._fail_msg = None
		self._id = None
		self._provider_id = None
		self._seq = None
		self._source_date = None
		self._status = None

		# impt-object type members
		self._facil = {}
		self._pro = {}

	#	facil member impt-object methods and properties
	#		Parameters
	#			arg1: instance of impt-object class Impt.Facil
	#			arg2: index for instance, if None, 0 is assumed
	#		- or -
	#			arg1: index for instance, if None, 0 is assumed
	#			      instance of impt-object class Impt.Facil
	#			      created internally

	def facil_add(self, p_arg1, *args):
		if len(args) == 0:
			obj = Impt.Facil()
			idx = p_arg1
		else:
			obj = p_arg1
			idx = args[0]
		if idx is None:
			idx = 0
		path_text = self.meta.path.text + ".facil[" + str(idx) + "]"
		self._facil[idx] = obj
		self._facil[idx].meta = Itom.Meta(path_text, idx, False)
		self._facil[idx].meta.core = self.meta.Core("facility")
		self.meta.active_objects_add_new("facil")

	def facil_add_new(self, p_arg1, *args):
		if len(args) == 0:
			obj = Impt.Facil()
			idx = p_arg1
		else:
			obj = p_arg1
			idx = args[0]
		if idx is None:
			idx = 0
		if idx not in self._facil:
			self.facil_add(obj, idx)

	@property
	def facil(self):
		if self._facil.keys() == [0] and self.meta.collapse_not_indexed:
			return self._facil[0]
		else:
			return self._facil

	def facils(self):
		"""Value iterator for facil regardless of meta.collapse_not_indexed"""
		return self._facil.itervalues()

	def facil_indexes(self):
		return self._facil.keys()

	#	pro member impt-object methods and properties
	#		Parameters
	#			arg1: instance of impt-object class Impt.Pro
	#			arg2: index for instance, if None, 0 is assumed
	#		- or -
	#			arg1: index for instance, if None, 0 is assumed
	#			      instance of impt-object class Impt.Pro
	#			      created internally

	def pro_add(self, p_arg1, *args):
		if len(args) == 0:
			obj = Impt.Pro()
			idx = p_arg1
		else:
			obj = p_arg1
			idx = args[0]
		if idx is None:
			idx = 0
		path_text = self.meta.path.text + ".pro[" + str(idx) + "]"
		self._pro[idx] = obj
		self._pro[idx].meta = Itom.Meta(path_text, idx, False)
		self._pro[idx].meta.core = self.meta.Core("provider")
		self.meta.active_objects_add_new("pro")

	def pro_add_new(self, p_arg1, *args):
		if len(args) == 0:
			obj = Impt.Pro()
			idx = p_arg1
		else:
			obj = p_arg1
			idx = args[0]
		if idx is None:
			idx = 0
		if idx not in self._pro:
			self.pro_add(obj, idx)

	@property
	def pro(self):
		if self._pro.keys() == [0] and self.meta.collapse_not_indexed:
			return self._pro[0]
		else:
			return self._pro

	def pros(self):
		"""Value iterator for pro regardless of meta.collapse_not_indexed"""
		return self._pro.itervalues()

	def pro_indexes(self):
		return self._pro.keys()

	# date member impt-field methods and properties
	#
	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, p_value):
		self.set_field("date", p_value)

	# facility_id member impt-field methods and properties
	#
	@property
	def facility_id(self):
		return self._facility_id

	@facility_id.setter
	def facility_id(self, p_value):
		self.set_field("facility_id", p_value)

	# fail_msg member impt-field methods and properties
	#
	@property
	def fail_msg(self):
		return self._fail_msg

	@fail_msg.setter
	def fail_msg(self, p_value):
		self.set_field("fail_msg", p_value)

	# id member impt-field methods and properties
	#
	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, p_value):
		self.set_field("id", p_value)

	# provider_id member impt-field methods and properties
	#
	@property
	def provider_id(self):
		return self._provider_id

	@provider_id.setter
	def provider_id(self, p_value):
		self.set_field("provider_id", p_value)

	# seq member impt-field methods and properties
	#
	@property
	def seq(self):
		return self._seq

	@seq.setter
	def seq(self, p_value):
		self.set_field("seq", p_value)

	# source_date member impt-field methods and properties
	#
	@property
	def source_date(self):
		return self._source_date

	@source_date.setter
	def source_date(self, p_value):
		self.set_field("source_date", p_value)

	# status member impt-field methods and properties
	#
	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, p_value):
		self.set_field("status", p_value)


	# Addr impt-object defining Address
	class Addr(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._department = None
			self._is_primary = None
			self._lat = None
			self._line1 = None
			self._line2 = None
			self._location_id = None
			self._long = None
			self._name = None
			self._type_code = None

			# impt-object members
			self._awd = {}
			self._datum = {}
			self._extid = {}
			self._ident = {}
			self._insp = {}
			self._lang = {}
			self._mda = {}
			self._parsed = {}
			self._phone = {}
			self._spe = {}

		#	awd member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Awd
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Awd
		#			      created internally

		def awd_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".awd[" + str(idx) + "]"
			self._awd[idx] = obj
			self._awd[idx].meta = Itom.Meta(path_text, idx, True)
			self._awd[idx].meta.core = self.meta.Core("award")
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._awd:
				self.awd_add(obj, idx)

		@property
		def awd(self):
			if self._awd.keys() == [0] and self.meta.collapse_not_indexed:
				return self._awd[0]
			else:
				return self._awd

		def awds(self):
			"""Value iterator for awd regardless of meta.collapse_not_indexed"""
			return self._awd.itervalues()

		def awd_indexes(self):
			return self._awd.keys()

		#	datum member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Datum
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Datum
		#			      created internally

		def datum_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".datum[" + str(idx) + "]"
			self._datum[idx] = obj
			self._datum[idx].meta = Itom.Meta(path_text, idx, True)
			self._datum[idx].meta.core = self.meta.Core("datum")
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._datum:
				self.datum_add(obj, idx)

		@property
		def datum(self):
			if self._datum.keys() == [0] and self.meta.collapse_not_indexed:
				return self._datum[0]
			else:
				return self._datum

		def datums(self):
			"""Value iterator for datum regardless of meta.collapse_not_indexed"""
			return self._datum.itervalues()

		def datum_indexes(self):
			return self._datum.keys()

		#	extid member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Extid
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Extid
		#			      created internally

		def extid_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".extid[" + str(idx) + "]"
			self._extid[idx] = obj
			self._extid[idx].meta = Itom.Meta(path_text, idx, True)
			self._extid[idx].meta.core = self.meta.Core("extid")
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._extid:
				self.extid_add(obj, idx)

		@property
		def extid(self):
			if self._extid.keys() == [0] and self.meta.collapse_not_indexed:
				return self._extid[0]
			else:
				return self._extid

		def extids(self):
			"""Value iterator for extid regardless of meta.collapse_not_indexed"""
			return self._extid.itervalues()

		def extid_indexes(self):
			return self._extid.keys()

		#	ident member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Ident
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Ident
		#			      created internally

		def ident_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".ident[" + str(idx) + "]"
			self._ident[idx] = obj
			self._ident[idx].meta = Itom.Meta(path_text, idx, True)
			self._ident[idx].meta.core = self.meta.Core("identifier")
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._ident:
				self.ident_add(obj, idx)

		@property
		def ident(self):
			if self._ident.keys() == [0] and self.meta.collapse_not_indexed:
				return self._ident[0]
			else:
				return self._ident

		def idents(self):
			"""Value iterator for ident regardless of meta.collapse_not_indexed"""
			return self._ident.itervalues()

		def ident_indexes(self):
			return self._ident.keys()

		#	insp member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Insp
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Insp
		#			      created internally

		def insp_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Insp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".insp[" + str(idx) + "]"
			self._insp[idx] = obj
			self._insp[idx].meta = Itom.Meta(path_text, idx, True)
			self._insp[idx].meta.core = self.meta.Core("ins_plan")
			self.meta.active_objects_add_new("insp")

		def insp_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Insp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._insp:
				self.insp_add(obj, idx)

		@property
		def insp(self):
			if self._insp.keys() == [0] and self.meta.collapse_not_indexed:
				return self._insp[0]
			else:
				return self._insp

		def insps(self):
			"""Value iterator for insp regardless of meta.collapse_not_indexed"""
			return self._insp.itervalues()

		def insp_indexes(self):
			return self._insp.keys()

		#	lang member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Lang
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Lang
		#			      created internally

		def lang_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".lang[" + str(idx) + "]"
			self._lang[idx] = obj
			self._lang[idx].meta = Itom.Meta(path_text, idx, False)
			self._lang[idx].meta.core = self.meta.Core(None)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._lang:
				self.lang_add(obj, idx)

		@property
		def lang(self):
			if self._lang.keys() == [0] and self.meta.collapse_not_indexed:
				return self._lang[0]
			else:
				return self._lang

		def langs(self):
			"""Value iterator for lang regardless of meta.collapse_not_indexed"""
			return self._lang.itervalues()

		def lang_indexes(self):
			return self._lang.keys()

		#	mda member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Mda
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Mda
		#			      created internally

		def mda_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Mda()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".mda[" + str(idx) + "]"
			self._mda[idx] = obj
			self._mda[idx].meta = Itom.Meta(path_text, idx, True)
			self._mda[idx].meta.core = self.meta.Core("media")
			self.meta.active_objects_add_new("mda")

		def mda_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Mda()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._mda:
				self.mda_add(obj, idx)

		@property
		def mda(self):
			if self._mda.keys() == [0] and self.meta.collapse_not_indexed:
				return self._mda[0]
			else:
				return self._mda

		def mdas(self):
			"""Value iterator for mda regardless of meta.collapse_not_indexed"""
			return self._mda.itervalues()

		def mda_indexes(self):
			return self._mda.keys()

		#	parsed member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Parsed
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Parsed
		#			      created internally

		def parsed_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Parsed()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".parsed[" + str(idx) + "]"
			self._parsed[idx] = obj
			self._parsed[idx].meta = Itom.Meta(path_text, idx, False)
			self._parsed[idx].meta.core = self.meta.Core("address")
			self.meta.active_objects_add_new("parsed")

		def parsed_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Parsed()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._parsed:
				self.parsed_add(obj, idx)

		@property
		def parsed(self):
			if self._parsed.keys() == [0] and self.meta.collapse_not_indexed:
				return self._parsed[0]
			else:
				return self._parsed

		def parseds(self):
			"""Value iterator for parsed regardless of meta.collapse_not_indexed"""
			return self._parsed.itervalues()

		def parsed_indexes(self):
			return self._parsed.keys()

		#	phone member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Phone
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Phone
		#			      created internally

		def phone_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Phone()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".phone[" + str(idx) + "]"
			self._phone[idx] = obj
			self._phone[idx].meta = Itom.Meta(path_text, idx, True)
			self._phone[idx].meta.core = self.meta.Core("phone")
			self.meta.active_objects_add_new("phone")

		def phone_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Phone()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._phone:
				self.phone_add(obj, idx)

		@property
		def phone(self):
			if self._phone.keys() == [0] and self.meta.collapse_not_indexed:
				return self._phone[0]
			else:
				return self._phone

		def phones(self):
			"""Value iterator for phone regardless of meta.collapse_not_indexed"""
			return self._phone.itervalues()

		def phone_indexes(self):
			return self._phone.keys()

		#	spe member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Spe
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Spe
		#			      created internally

		def spe_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".spe[" + str(idx) + "]"
			self._spe[idx] = obj
			self._spe[idx].meta = Itom.Meta(path_text, idx, True)
			self._spe[idx].meta.core = self.meta.Core("field_specialty")
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._spe:
				self.spe_add(obj, idx)

		@property
		def spe(self):
			if self._spe.keys() == [0] and self.meta.collapse_not_indexed:
				return self._spe[0]
			else:
				return self._spe

		def spes(self):
			"""Value iterator for spe regardless of meta.collapse_not_indexed"""
			return self._spe.itervalues()

		def spe_indexes(self):
			return self._spe.keys()

		# department member impt-field methods and properties
		#
		@property
		def department(self):
			return self._department

		@department.setter
		def department(self, p_value):
			self.set_field("department", p_value)

		# is_primary member impt-field methods and properties
		#
		@property
		def is_primary(self):
			return self._is_primary

		@is_primary.setter
		def is_primary(self, p_value):
			self.set_field("is_primary", p_value)

		# lat member impt-field methods and properties
		#
		@property
		def lat(self):
			return self._lat

		@lat.setter
		def lat(self, p_value):
			self.set_field("lat", p_value)

		# line1 member impt-field methods and properties
		#
		@property
		def line1(self):
			return self._line1

		@line1.setter
		def line1(self, p_value):
			self.set_field("line1", p_value)

		# line2 member impt-field methods and properties
		#
		@property
		def line2(self):
			return self._line2

		@line2.setter
		def line2(self, p_value):
			self.set_field("line2", p_value)

		# location_id member impt-field methods and properties
		#
		@property
		def location_id(self):
			return self._location_id

		@location_id.setter
		def location_id(self, p_value):
			self.set_field("location_id", p_value)

		# long member impt-field methods and properties
		#
		@property
		def long(self):
			return self._long

		@long.setter
		def long(self, p_value):
			self.set_field("long", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

	# Affil impt-object defining Affiliation
	class Affil(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._dept = None
			self._desc = None
			self._info = None
			self._is_practicing = None
			self._name = None
			self._position = None
			self._record_status = None
			self._start_date = None

			# impt-object members
			self._facil = {}

		#	facil member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Facil
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Facil
		#			      created internally

		def facil_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".facil[" + str(idx) + "]"
			self._facil[idx] = obj
			self._facil[idx].meta = Itom.Meta(path_text, idx, False)
			self._facil[idx].meta.core = self.meta.Core("facility")
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._facil:
				self.facil_add(obj, idx)

		@property
		def facil(self):
			if self._facil.keys() == [0] and self.meta.collapse_not_indexed:
				return self._facil[0]
			else:
				return self._facil

		def facils(self):
			"""Value iterator for facil regardless of meta.collapse_not_indexed"""
			return self._facil.itervalues()

		def facil_indexes(self):
			return self._facil.keys()

		# dept member impt-field methods and properties
		#
		@property
		def dept(self):
			return self._dept

		@dept.setter
		def dept(self, p_value):
			self.set_field("dept", p_value)

		# desc member impt-field methods and properties
		#
		@property
		def desc(self):
			return self._desc

		@desc.setter
		def desc(self, p_value):
			self.set_field("desc", p_value)

		# info member impt-field methods and properties
		#
		@property
		def info(self):
			return self._info

		@info.setter
		def info(self, p_value):
			self.set_field("info", p_value)

		# is_practicing member impt-field methods and properties
		#
		@property
		def is_practicing(self):
			return self._is_practicing

		@is_practicing.setter
		def is_practicing(self, p_value):
			self.set_field("is_practicing", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# position member impt-field methods and properties
		#
		@property
		def position(self):
			return self._position

		@position.setter
		def position(self, p_value):
			self.set_field("position", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# start_date member impt-field methods and properties
		#
		@property
		def start_date(self):
			return self._start_date

		@start_date.setter
		def start_date(self, p_value):
			self.set_field("start_date", p_value)

	# Alias impt-object defining Alias
	class Alias(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._first_name = None
			self._last_name = None
			self._middle_name = None
			self._name = None
			self._suffix = None

		# first_name member impt-field methods and properties
		#
		@property
		def first_name(self):
			return self._first_name

		@first_name.setter
		def first_name(self, p_value):
			self.set_field("first_name", p_value)

		# last_name member impt-field methods and properties
		#
		@property
		def last_name(self):
			return self._last_name

		@last_name.setter
		def last_name(self, p_value):
			self.set_field("last_name", p_value)

		# middle_name member impt-field methods and properties
		#
		@property
		def middle_name(self):
			return self._middle_name

		@middle_name.setter
		def middle_name(self, p_value):
			self.set_field("middle_name", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# suffix member impt-field methods and properties
		#
		@property
		def suffix(self):
			return self._suffix

		@suffix.setter
		def suffix(self, p_value):
			self.set_field("suffix", p_value)

	# Asn impt-object defining Association
	class Asn(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._association_id = None
			self._end_year = None
			self._institution = None
			self._record_status = None
			self._start_year = None
			self._title = None
			self._type_code = None

		# association_id member impt-field methods and properties
		#
		@property
		def association_id(self):
			return self._association_id

		@association_id.setter
		def association_id(self, p_value):
			self.set_field("association_id", p_value)

		# end_year member impt-field methods and properties
		#
		@property
		def end_year(self):
			return self._end_year

		@end_year.setter
		def end_year(self, p_value):
			self.set_field("end_year", p_value)

		# institution member impt-field methods and properties
		#
		@property
		def institution(self):
			return self._institution

		@institution.setter
		def institution(self, p_value):
			self.set_field("institution", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# start_year member impt-field methods and properties
		#
		@property
		def start_year(self):
			return self._start_year

		@start_year.setter
		def start_year(self, p_value):
			self.set_field("start_year", p_value)

		# title member impt-field methods and properties
		#
		@property
		def title(self):
			return self._title

		@title.setter
		def title(self, p_value):
			self.set_field("title", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

	# Attr impt-object defining Attribute
	class Attr(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._desc = None
			self._record_status = None
			self._type_code = None
			self._value = None

		# desc member impt-field methods and properties
		#
		@property
		def desc(self):
			return self._desc

		@desc.setter
		def desc(self, p_value):
			self.set_field("desc", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

		# value member impt-field methods and properties
		#
		@property
		def value(self):
			return self._value

		@value.setter
		def value(self, p_value):
			self.set_field("value", p_value)

	# Awd impt-object defining Award
	class Awd(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._end_year = None
			self._institution = None
			self._name = None
			self._record_status = None
			self._start_year = None
			self._type_code = None
			self._value = None
			self._website_url = None

		# end_year member impt-field methods and properties
		#
		@property
		def end_year(self):
			return self._end_year

		@end_year.setter
		def end_year(self, p_value):
			self.set_field("end_year", p_value)

		# institution member impt-field methods and properties
		#
		@property
		def institution(self):
			return self._institution

		@institution.setter
		def institution(self, p_value):
			self.set_field("institution", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# start_year member impt-field methods and properties
		#
		@property
		def start_year(self):
			return self._start_year

		@start_year.setter
		def start_year(self, p_value):
			self.set_field("start_year", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

		# value member impt-field methods and properties
		#
		@property
		def value(self):
			return self._value

		@value.setter
		def value(self, p_value):
			self.set_field("value", p_value)

		# website_url member impt-field methods and properties
		#
		@property
		def website_url(self):
			return self._website_url

		@website_url.setter
		def website_url(self, p_value):
			self.set_field("website_url", p_value)

	# Datum impt-object defining Data
	class Datum(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._desc = None
			self._record_status = None
			self._type_code = None
			self._value = None

			# impt-object members
			self._attr = {}

		#	attr member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Attr
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Attr
		#			      created internally

		def attr_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Attr()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".attr[" + str(idx) + "]"
			self._attr[idx] = obj
			self._attr[idx].meta = Itom.Meta(path_text, idx, True)
			self._attr[idx].meta.core = self.meta.Core("attribute")
			self.meta.active_objects_add_new("attr")

		def attr_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Attr()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._attr:
				self.attr_add(obj, idx)

		@property
		def attr(self):
			if self._attr.keys() == [0] and self.meta.collapse_not_indexed:
				return self._attr[0]
			else:
				return self._attr

		def attrs(self):
			"""Value iterator for attr regardless of meta.collapse_not_indexed"""
			return self._attr.itervalues()

		def attr_indexes(self):
			return self._attr.keys()

		# desc member impt-field methods and properties
		#
		@property
		def desc(self):
			return self._desc

		@desc.setter
		def desc(self, p_value):
			self.set_field("desc", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

		# value member impt-field methods and properties
		#
		@property
		def value(self):
			return self._value

		@value.setter
		def value(self, p_value):
			self.set_field("value", p_value)

	# Degree impt-object defining Degree
	class Degree(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._code = None
			self._record_status = None

		# code member impt-field methods and properties
		#
		@property
		def code(self):
			return self._code

		@code.setter
		def code(self, p_value):
			self.set_field("code", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

	# Edu impt-object defining Education
	class Edu(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._end_date = None
			self._end_day = None
			self._end_month = None
			self._end_year = None
			self._is_foreign = None
			self._record_status = None
			self._start_date = None
			self._start_day = None
			self._start_month = None
			self._start_year = None
			self._type_code = None

			# impt-object members
			self._degree = {}
			self._facil = {}
			self._spe = {}

		#	degree member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Degree
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Degree
		#			      created internally

		def degree_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Degree()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".degree[" + str(idx) + "]"
			self._degree[idx] = obj
			self._degree[idx].meta = Itom.Meta(path_text, idx, False)
			self._degree[idx].meta.core = self.meta.Core("degree")
			self.meta.active_objects_add_new("degree")

		def degree_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Degree()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._degree:
				self.degree_add(obj, idx)

		@property
		def degree(self):
			if self._degree.keys() == [0] and self.meta.collapse_not_indexed:
				return self._degree[0]
			else:
				return self._degree

		def degrees(self):
			"""Value iterator for degree regardless of meta.collapse_not_indexed"""
			return self._degree.itervalues()

		def degree_indexes(self):
			return self._degree.keys()

		#	facil member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Facil
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Facil
		#			      created internally

		def facil_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".facil[" + str(idx) + "]"
			self._facil[idx] = obj
			self._facil[idx].meta = Itom.Meta(path_text, idx, False)
			self._facil[idx].meta.core = self.meta.Core("facility")
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._facil:
				self.facil_add(obj, idx)

		@property
		def facil(self):
			if self._facil.keys() == [0] and self.meta.collapse_not_indexed:
				return self._facil[0]
			else:
				return self._facil

		def facils(self):
			"""Value iterator for facil regardless of meta.collapse_not_indexed"""
			return self._facil.itervalues()

		def facil_indexes(self):
			return self._facil.keys()

		#	spe member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Spe
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Spe
		#			      created internally

		def spe_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".spe[" + str(idx) + "]"
			self._spe[idx] = obj
			self._spe[idx].meta = Itom.Meta(path_text, idx, True)
			self._spe[idx].meta.core = self.meta.Core("field_specialty")
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._spe:
				self.spe_add(obj, idx)

		@property
		def spe(self):
			if self._spe.keys() == [0] and self.meta.collapse_not_indexed:
				return self._spe[0]
			else:
				return self._spe

		def spes(self):
			"""Value iterator for spe regardless of meta.collapse_not_indexed"""
			return self._spe.itervalues()

		def spe_indexes(self):
			return self._spe.keys()

		# end_date member impt-field methods and properties
		#
		@property
		def end_date(self):
			return self._end_date

		@end_date.setter
		def end_date(self, p_value):
			self.set_field("end_date", p_value)

		# end_day member impt-field methods and properties
		#
		@property
		def end_day(self):
			return self._end_day

		@end_day.setter
		def end_day(self, p_value):
			self.set_field("end_day", p_value)

		# end_month member impt-field methods and properties
		#
		@property
		def end_month(self):
			return self._end_month

		@end_month.setter
		def end_month(self, p_value):
			self.set_field("end_month", p_value)

		# end_year member impt-field methods and properties
		#
		@property
		def end_year(self):
			return self._end_year

		@end_year.setter
		def end_year(self, p_value):
			self.set_field("end_year", p_value)

		# is_foreign member impt-field methods and properties
		#
		@property
		def is_foreign(self):
			return self._is_foreign

		@is_foreign.setter
		def is_foreign(self, p_value):
			self.set_field("is_foreign", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# start_date member impt-field methods and properties
		#
		@property
		def start_date(self):
			return self._start_date

		@start_date.setter
		def start_date(self, p_value):
			self.set_field("start_date", p_value)

		# start_day member impt-field methods and properties
		#
		@property
		def start_day(self):
			return self._start_day

		@start_day.setter
		def start_day(self, p_value):
			self.set_field("start_day", p_value)

		# start_month member impt-field methods and properties
		#
		@property
		def start_month(self):
			return self._start_month

		@start_month.setter
		def start_month(self, p_value):
			self.set_field("start_month", p_value)

		# start_year member impt-field methods and properties
		#
		@property
		def start_year(self):
			return self._start_year

		@start_year.setter
		def start_year(self, p_value):
			self.set_field("start_year", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

	# Extid impt-object defining External ID
	class Extid(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._record_status = None
			self._source_code = None
			self._value = None

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# source_code member impt-field methods and properties
		#
		@property
		def source_code(self):
			return self._source_code

		@source_code.setter
		def source_code(self, p_value):
			self.set_field("source_code", p_value)

		# value member impt-field methods and properties
		#
		@property
		def value(self):
			return self._value

		@value.setter
		def value(self, p_value):
			self.set_field("value", p_value)

	# Facil impt-object defining Facility
	class Facil(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._city = None
			self._country = None
			self._facility_id = None
			self._hours = None
			self._is_primary = None
			self._lat = None
			self._long = None
			self._master_id = None
			self._name = None
			self._record_status = None
			self._state = None
			self._status_code = None
			self._type_code = None
			self._zip = None

			# impt-object members
			self._addr = {}
			self._affil = {}
			self._alias = {}
			self._awd = {}
			self._datum = {}
			self._extid = {}
			self._ident = {}
			self._lang = {}
			self._mda = {}
			self._parent = {}

		#	addr member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Addr
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Addr
		#			      created internally

		def addr_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Addr()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".addr[" + str(idx) + "]"
			self._addr[idx] = obj
			self._addr[idx].meta = Itom.Meta(path_text, idx, False)
			self._addr[idx].meta.core = self.meta.Core("address")
			self.meta.active_objects_add_new("addr")

		def addr_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Addr()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._addr:
				self.addr_add(obj, idx)

		@property
		def addr(self):
			if self._addr.keys() == [0] and self.meta.collapse_not_indexed:
				return self._addr[0]
			else:
				return self._addr

		def addrs(self):
			"""Value iterator for addr regardless of meta.collapse_not_indexed"""
			return self._addr.itervalues()

		def addr_indexes(self):
			return self._addr.keys()

		#	affil member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Affil
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Affil
		#			      created internally

		def affil_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Affil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".affil[" + str(idx) + "]"
			self._affil[idx] = obj
			self._affil[idx].meta = Itom.Meta(path_text, idx, True)
			self._affil[idx].meta.core = self.meta.Core("affiliation")
			self.meta.active_objects_add_new("affil")

		def affil_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Affil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._affil:
				self.affil_add(obj, idx)

		@property
		def affil(self):
			if self._affil.keys() == [0] and self.meta.collapse_not_indexed:
				return self._affil[0]
			else:
				return self._affil

		def affils(self):
			"""Value iterator for affil regardless of meta.collapse_not_indexed"""
			return self._affil.itervalues()

		def affil_indexes(self):
			return self._affil.keys()

		#	alias member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Alias
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Alias
		#			      created internally

		def alias_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Alias()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".alias[" + str(idx) + "]"
			self._alias[idx] = obj
			self._alias[idx].meta = Itom.Meta(path_text, idx, False)
			self._alias[idx].meta.core = self.meta.Core("name")
			self.meta.active_objects_add_new("alias")

		def alias_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Alias()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._alias:
				self.alias_add(obj, idx)

		@property
		def alias(self):
			if self._alias.keys() == [0] and self.meta.collapse_not_indexed:
				return self._alias[0]
			else:
				return self._alias

		def aliases(self):
			"""Value iterator for alias regardless of meta.collapse_not_indexed"""
			return self._alias.itervalues()

		def alias_indexes(self):
			return self._alias.keys()

		#	awd member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Awd
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Awd
		#			      created internally

		def awd_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".awd[" + str(idx) + "]"
			self._awd[idx] = obj
			self._awd[idx].meta = Itom.Meta(path_text, idx, True)
			self._awd[idx].meta.core = self.meta.Core("award")
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._awd:
				self.awd_add(obj, idx)

		@property
		def awd(self):
			if self._awd.keys() == [0] and self.meta.collapse_not_indexed:
				return self._awd[0]
			else:
				return self._awd

		def awds(self):
			"""Value iterator for awd regardless of meta.collapse_not_indexed"""
			return self._awd.itervalues()

		def awd_indexes(self):
			return self._awd.keys()

		#	datum member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Datum
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Datum
		#			      created internally

		def datum_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".datum[" + str(idx) + "]"
			self._datum[idx] = obj
			self._datum[idx].meta = Itom.Meta(path_text, idx, True)
			self._datum[idx].meta.core = self.meta.Core("datum")
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._datum:
				self.datum_add(obj, idx)

		@property
		def datum(self):
			if self._datum.keys() == [0] and self.meta.collapse_not_indexed:
				return self._datum[0]
			else:
				return self._datum

		def datums(self):
			"""Value iterator for datum regardless of meta.collapse_not_indexed"""
			return self._datum.itervalues()

		def datum_indexes(self):
			return self._datum.keys()

		#	extid member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Extid
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Extid
		#			      created internally

		def extid_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".extid[" + str(idx) + "]"
			self._extid[idx] = obj
			self._extid[idx].meta = Itom.Meta(path_text, idx, True)
			self._extid[idx].meta.core = self.meta.Core("extid")
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._extid:
				self.extid_add(obj, idx)

		@property
		def extid(self):
			if self._extid.keys() == [0] and self.meta.collapse_not_indexed:
				return self._extid[0]
			else:
				return self._extid

		def extids(self):
			"""Value iterator for extid regardless of meta.collapse_not_indexed"""
			return self._extid.itervalues()

		def extid_indexes(self):
			return self._extid.keys()

		#	ident member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Ident
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Ident
		#			      created internally

		def ident_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".ident[" + str(idx) + "]"
			self._ident[idx] = obj
			self._ident[idx].meta = Itom.Meta(path_text, idx, True)
			self._ident[idx].meta.core = self.meta.Core("identifier")
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._ident:
				self.ident_add(obj, idx)

		@property
		def ident(self):
			if self._ident.keys() == [0] and self.meta.collapse_not_indexed:
				return self._ident[0]
			else:
				return self._ident

		def idents(self):
			"""Value iterator for ident regardless of meta.collapse_not_indexed"""
			return self._ident.itervalues()

		def ident_indexes(self):
			return self._ident.keys()

		#	lang member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Lang
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Lang
		#			      created internally

		def lang_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".lang[" + str(idx) + "]"
			self._lang[idx] = obj
			self._lang[idx].meta = Itom.Meta(path_text, idx, False)
			self._lang[idx].meta.core = self.meta.Core(None)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._lang:
				self.lang_add(obj, idx)

		@property
		def lang(self):
			if self._lang.keys() == [0] and self.meta.collapse_not_indexed:
				return self._lang[0]
			else:
				return self._lang

		def langs(self):
			"""Value iterator for lang regardless of meta.collapse_not_indexed"""
			return self._lang.itervalues()

		def lang_indexes(self):
			return self._lang.keys()

		#	mda member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Mda
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Mda
		#			      created internally

		def mda_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Mda()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".mda[" + str(idx) + "]"
			self._mda[idx] = obj
			self._mda[idx].meta = Itom.Meta(path_text, idx, True)
			self._mda[idx].meta.core = self.meta.Core("media")
			self.meta.active_objects_add_new("mda")

		def mda_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Mda()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._mda:
				self.mda_add(obj, idx)

		@property
		def mda(self):
			if self._mda.keys() == [0] and self.meta.collapse_not_indexed:
				return self._mda[0]
			else:
				return self._mda

		def mdas(self):
			"""Value iterator for mda regardless of meta.collapse_not_indexed"""
			return self._mda.itervalues()

		def mda_indexes(self):
			return self._mda.keys()

		#	parent member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Parent
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Parent
		#			      created internally

		def parent_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Parent()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".parent[" + str(idx) + "]"
			self._parent[idx] = obj
			self._parent[idx].meta = Itom.Meta(path_text, idx, False)
			self._parent[idx].meta.core = self.meta.Core(None)
			self.meta.active_objects_add_new("parent")

		def parent_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Parent()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._parent:
				self.parent_add(obj, idx)

		@property
		def parent(self):
			if self._parent.keys() == [0] and self.meta.collapse_not_indexed:
				return self._parent[0]
			else:
				return self._parent

		def parents(self):
			"""Value iterator for parent regardless of meta.collapse_not_indexed"""
			return self._parent.itervalues()

		def parent_indexes(self):
			return self._parent.keys()

		# city member impt-field methods and properties
		#
		@property
		def city(self):
			return self._city

		@city.setter
		def city(self, p_value):
			self.set_field("city", p_value)

		# country member impt-field methods and properties
		#
		@property
		def country(self):
			return self._country

		@country.setter
		def country(self, p_value):
			self.set_field("country", p_value)

		# facility_id member impt-field methods and properties
		#
		@property
		def facility_id(self):
			return self._facility_id

		@facility_id.setter
		def facility_id(self, p_value):
			self.set_field("facility_id", p_value)

		# hours member impt-field methods and properties
		#
		@property
		def hours(self):
			return self._hours

		@hours.setter
		def hours(self, p_value):
			self.set_field("hours", p_value)

		# is_primary member impt-field methods and properties
		#
		@property
		def is_primary(self):
			return self._is_primary

		@is_primary.setter
		def is_primary(self, p_value):
			self.set_field("is_primary", p_value)

		# lat member impt-field methods and properties
		#
		@property
		def lat(self):
			return self._lat

		@lat.setter
		def lat(self, p_value):
			self.set_field("lat", p_value)

		# long member impt-field methods and properties
		#
		@property
		def long(self):
			return self._long

		@long.setter
		def long(self, p_value):
			self.set_field("long", p_value)

		# master_id member impt-field methods and properties
		#
		@property
		def master_id(self):
			return self._master_id

		@master_id.setter
		def master_id(self, p_value):
			self.set_field("master_id", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# state member impt-field methods and properties
		#
		@property
		def state(self):
			return self._state

		@state.setter
		def state(self, p_value):
			self.set_field("state", p_value)

		# status_code member impt-field methods and properties
		#
		@property
		def status_code(self):
			return self._status_code

		@status_code.setter
		def status_code(self, p_value):
			self.set_field("status_code", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

		# zip member impt-field methods and properties
		#
		@property
		def zip(self):
			return self._zip

		@zip.setter
		def zip(self, p_value):
			self.set_field("zip", p_value)

	# Ident impt-object defining Identifier
	class Ident(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._record_status = None
			self._type_id = None
			self._value = None

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# type_id member impt-field methods and properties
		#
		@property
		def type_id(self):
			return self._type_id

		@type_id.setter
		def type_id(self, p_value):
			self.set_field("type_id", p_value)

		# value member impt-field methods and properties
		#
		@property
		def value(self):
			return self._value

		@value.setter
		def value(self, p_value):
			self.set_field("value", p_value)

	# Insp impt-object defining Insurance Plan
	class Insp(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._desc = None
			self._info = None
			self._ins_plan_id = None
			self._record_status = None

			# impt-object members
			self._affil = {}
			self._awd = {}
			self._datum = {}
			self._extid = {}
			self._ident = {}
			self._ref = {}
			self._spe = {}

		#	affil member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Affil
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Affil
		#			      created internally

		def affil_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Affil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".affil[" + str(idx) + "]"
			self._affil[idx] = obj
			self._affil[idx].meta = Itom.Meta(path_text, idx, True)
			self._affil[idx].meta.core = self.meta.Core("affiliation")
			self.meta.active_objects_add_new("affil")

		def affil_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Affil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._affil:
				self.affil_add(obj, idx)

		@property
		def affil(self):
			if self._affil.keys() == [0] and self.meta.collapse_not_indexed:
				return self._affil[0]
			else:
				return self._affil

		def affils(self):
			"""Value iterator for affil regardless of meta.collapse_not_indexed"""
			return self._affil.itervalues()

		def affil_indexes(self):
			return self._affil.keys()

		#	awd member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Awd
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Awd
		#			      created internally

		def awd_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".awd[" + str(idx) + "]"
			self._awd[idx] = obj
			self._awd[idx].meta = Itom.Meta(path_text, idx, True)
			self._awd[idx].meta.core = self.meta.Core("award")
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._awd:
				self.awd_add(obj, idx)

		@property
		def awd(self):
			if self._awd.keys() == [0] and self.meta.collapse_not_indexed:
				return self._awd[0]
			else:
				return self._awd

		def awds(self):
			"""Value iterator for awd regardless of meta.collapse_not_indexed"""
			return self._awd.itervalues()

		def awd_indexes(self):
			return self._awd.keys()

		#	datum member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Datum
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Datum
		#			      created internally

		def datum_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".datum[" + str(idx) + "]"
			self._datum[idx] = obj
			self._datum[idx].meta = Itom.Meta(path_text, idx, True)
			self._datum[idx].meta.core = self.meta.Core("datum")
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._datum:
				self.datum_add(obj, idx)

		@property
		def datum(self):
			if self._datum.keys() == [0] and self.meta.collapse_not_indexed:
				return self._datum[0]
			else:
				return self._datum

		def datums(self):
			"""Value iterator for datum regardless of meta.collapse_not_indexed"""
			return self._datum.itervalues()

		def datum_indexes(self):
			return self._datum.keys()

		#	extid member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Extid
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Extid
		#			      created internally

		def extid_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".extid[" + str(idx) + "]"
			self._extid[idx] = obj
			self._extid[idx].meta = Itom.Meta(path_text, idx, True)
			self._extid[idx].meta.core = self.meta.Core("extid")
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._extid:
				self.extid_add(obj, idx)

		@property
		def extid(self):
			if self._extid.keys() == [0] and self.meta.collapse_not_indexed:
				return self._extid[0]
			else:
				return self._extid

		def extids(self):
			"""Value iterator for extid regardless of meta.collapse_not_indexed"""
			return self._extid.itervalues()

		def extid_indexes(self):
			return self._extid.keys()

		#	ident member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Ident
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Ident
		#			      created internally

		def ident_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".ident[" + str(idx) + "]"
			self._ident[idx] = obj
			self._ident[idx].meta = Itom.Meta(path_text, idx, True)
			self._ident[idx].meta.core = self.meta.Core("identifier")
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._ident:
				self.ident_add(obj, idx)

		@property
		def ident(self):
			if self._ident.keys() == [0] and self.meta.collapse_not_indexed:
				return self._ident[0]
			else:
				return self._ident

		def idents(self):
			"""Value iterator for ident regardless of meta.collapse_not_indexed"""
			return self._ident.itervalues()

		def ident_indexes(self):
			return self._ident.keys()

		#	ref member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Ref
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Ref
		#			      created internally

		def ref_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ref()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".ref[" + str(idx) + "]"
			self._ref[idx] = obj
			self._ref[idx].meta = Itom.Meta(path_text, idx, True)
			self._ref[idx].meta.core = self.meta.Core("referral")
			self.meta.active_objects_add_new("ref")

		def ref_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ref()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._ref:
				self.ref_add(obj, idx)

		@property
		def ref(self):
			if self._ref.keys() == [0] and self.meta.collapse_not_indexed:
				return self._ref[0]
			else:
				return self._ref

		def refs(self):
			"""Value iterator for ref regardless of meta.collapse_not_indexed"""
			return self._ref.itervalues()

		def ref_indexes(self):
			return self._ref.keys()

		#	spe member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Spe
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Spe
		#			      created internally

		def spe_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".spe[" + str(idx) + "]"
			self._spe[idx] = obj
			self._spe[idx].meta = Itom.Meta(path_text, idx, True)
			self._spe[idx].meta.core = self.meta.Core("field_specialty")
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._spe:
				self.spe_add(obj, idx)

		@property
		def spe(self):
			if self._spe.keys() == [0] and self.meta.collapse_not_indexed:
				return self._spe[0]
			else:
				return self._spe

		def spes(self):
			"""Value iterator for spe regardless of meta.collapse_not_indexed"""
			return self._spe.itervalues()

		def spe_indexes(self):
			return self._spe.keys()

		# desc member impt-field methods and properties
		#
		@property
		def desc(self):
			return self._desc

		@desc.setter
		def desc(self, p_value):
			self.set_field("desc", p_value)

		# info member impt-field methods and properties
		#
		@property
		def info(self):
			return self._info

		@info.setter
		def info(self, p_value):
			self.set_field("info", p_value)

		# ins_plan_id member impt-field methods and properties
		#
		@property
		def ins_plan_id(self):
			return self._ins_plan_id

		@ins_plan_id.setter
		def ins_plan_id(self, p_value):
			self.set_field("ins_plan_id", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

	# Lang impt-object defining Language
	class Lang(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._code = None
			self._name = None
			self._record_status = None

		# code member impt-field methods and properties
		#
		@property
		def code(self):
			return self._code

		@code.setter
		def code(self, p_value):
			self.set_field("code", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

	# Lic impt-object defining License
	class Lic(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._end_date = None
			self._exam_type = None
			self._issue_date = None
			self._last_renewed = None
			self._nbr = None
			self._obtained_by = None
			self._start_date = None
			self._state = None
			self._status_code = None
			self._status_desc = None

			# impt-object members
			self._prof = {}

		#	prof member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Prof
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Prof
		#			      created internally

		def prof_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Prof()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".prof[" + str(idx) + "]"
			self._prof[idx] = obj
			self._prof[idx].meta = Itom.Meta(path_text, idx, False)
			self._prof[idx].meta.core = self.meta.Core("profession")
			self.meta.active_objects_add_new("prof")

		def prof_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Prof()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._prof:
				self.prof_add(obj, idx)

		@property
		def prof(self):
			if self._prof.keys() == [0] and self.meta.collapse_not_indexed:
				return self._prof[0]
			else:
				return self._prof

		def profs(self):
			"""Value iterator for prof regardless of meta.collapse_not_indexed"""
			return self._prof.itervalues()

		def prof_indexes(self):
			return self._prof.keys()

		# end_date member impt-field methods and properties
		#
		@property
		def end_date(self):
			return self._end_date

		@end_date.setter
		def end_date(self, p_value):
			self.set_field("end_date", p_value)

		# exam_type member impt-field methods and properties
		#
		@property
		def exam_type(self):
			return self._exam_type

		@exam_type.setter
		def exam_type(self, p_value):
			self.set_field("exam_type", p_value)

		# issue_date member impt-field methods and properties
		#
		@property
		def issue_date(self):
			return self._issue_date

		@issue_date.setter
		def issue_date(self, p_value):
			self.set_field("issue_date", p_value)

		# last_renewed member impt-field methods and properties
		#
		@property
		def last_renewed(self):
			return self._last_renewed

		@last_renewed.setter
		def last_renewed(self, p_value):
			self.set_field("last_renewed", p_value)

		# nbr member impt-field methods and properties
		#
		@property
		def nbr(self):
			return self._nbr

		@nbr.setter
		def nbr(self, p_value):
			self.set_field("nbr", p_value)

		# obtained_by member impt-field methods and properties
		#
		@property
		def obtained_by(self):
			return self._obtained_by

		@obtained_by.setter
		def obtained_by(self, p_value):
			self.set_field("obtained_by", p_value)

		# start_date member impt-field methods and properties
		#
		@property
		def start_date(self):
			return self._start_date

		@start_date.setter
		def start_date(self, p_value):
			self.set_field("start_date", p_value)

		# state member impt-field methods and properties
		#
		@property
		def state(self):
			return self._state

		@state.setter
		def state(self, p_value):
			self.set_field("state", p_value)

		# status_code member impt-field methods and properties
		#
		@property
		def status_code(self):
			return self._status_code

		@status_code.setter
		def status_code(self, p_value):
			self.set_field("status_code", p_value)

		# status_desc member impt-field methods and properties
		#
		@property
		def status_desc(self):
			return self._status_desc

		@status_desc.setter
		def status_desc(self, p_value):
			self.set_field("status_desc", p_value)

	# Malp impt-object defining Malpractice
	class Malp(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._amount = None
			self._claim = None
			self._date = None
			self._info = None
			self._reason = None
			self._record_status = None
			self._reference = None
			self._state_code = None

		# amount member impt-field methods and properties
		#
		@property
		def amount(self):
			return self._amount

		@amount.setter
		def amount(self, p_value):
			self.set_field("amount", p_value)

		# claim member impt-field methods and properties
		#
		@property
		def claim(self):
			return self._claim

		@claim.setter
		def claim(self, p_value):
			self.set_field("claim", p_value)

		# date member impt-field methods and properties
		#
		@property
		def date(self):
			return self._date

		@date.setter
		def date(self, p_value):
			self.set_field("date", p_value)

		# info member impt-field methods and properties
		#
		@property
		def info(self):
			return self._info

		@info.setter
		def info(self, p_value):
			self.set_field("info", p_value)

		# reason member impt-field methods and properties
		#
		@property
		def reason(self):
			return self._reason

		@reason.setter
		def reason(self, p_value):
			self.set_field("reason", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# reference member impt-field methods and properties
		#
		@property
		def reference(self):
			return self._reference

		@reference.setter
		def reference(self, p_value):
			self.set_field("reference", p_value)

		# state_code member impt-field methods and properties
		#
		@property
		def state_code(self):
			return self._state_code

		@state_code.setter
		def state_code(self, p_value):
			self.set_field("state_code", p_value)

	# Mda impt-object defining Media
	class Mda(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._category_code = None
			self._dest_url = None
			self._orig_source = None
			self._record_status = None
			self._source = None
			self._source_code = None

		# category_code member impt-field methods and properties
		#
		@property
		def category_code(self):
			return self._category_code

		@category_code.setter
		def category_code(self, p_value):
			self.set_field("category_code", p_value)

		# dest_url member impt-field methods and properties
		#
		@property
		def dest_url(self):
			return self._dest_url

		@dest_url.setter
		def dest_url(self, p_value):
			self.set_field("dest_url", p_value)

		# orig_source member impt-field methods and properties
		#
		@property
		def orig_source(self):
			return self._orig_source

		@orig_source.setter
		def orig_source(self, p_value):
			self.set_field("orig_source", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# source member impt-field methods and properties
		#
		@property
		def source(self):
			return self._source

		@source.setter
		def source(self, p_value):
			self.set_field("source", p_value)

		# source_code member impt-field methods and properties
		#
		@property
		def source_code(self):
			return self._source_code

		@source_code.setter
		def source_code(self, p_value):
			self.set_field("source_code", p_value)

	# Parent impt-object defining Parent Facility
	class Parent(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-object members
			self._facil = {}

		#	facil member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Facil
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Facil
		#			      created internally

		def facil_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".facil[" + str(idx) + "]"
			self._facil[idx] = obj
			self._facil[idx].meta = Itom.Meta(path_text, idx, False)
			self._facil[idx].meta.core = self.meta.Core("facility")
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._facil:
				self.facil_add(obj, idx)

		@property
		def facil(self):
			if self._facil.keys() == [0] and self.meta.collapse_not_indexed:
				return self._facil[0]
			else:
				return self._facil

		def facils(self):
			"""Value iterator for facil regardless of meta.collapse_not_indexed"""
			return self._facil.itervalues()

		def facil_indexes(self):
			return self._facil.keys()

	# Parsed impt-object defining Parsed
	class Parsed(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._codes = None
			self._is_validated = None
			self._lat = None
			self._long = None
			self._number = None
			self._po_box = None
			self._postdir = None
			self._predir = None
			self._street = None
			self._suffix = None
			self._unit_full = None
			self._unit_name = None
			self._unit_range = None

		# codes member impt-field methods and properties
		#
		@property
		def codes(self):
			return self._codes

		@codes.setter
		def codes(self, p_value):
			self.set_field("codes", p_value)

		# is_validated member impt-field methods and properties
		#
		@property
		def is_validated(self):
			return self._is_validated

		@is_validated.setter
		def is_validated(self, p_value):
			self.set_field("is_validated", p_value)

		# lat member impt-field methods and properties
		#
		@property
		def lat(self):
			return self._lat

		@lat.setter
		def lat(self, p_value):
			self.set_field("lat", p_value)

		# long member impt-field methods and properties
		#
		@property
		def long(self):
			return self._long

		@long.setter
		def long(self, p_value):
			self.set_field("long", p_value)

		# number member impt-field methods and properties
		#
		@property
		def number(self):
			return self._number

		@number.setter
		def number(self, p_value):
			self.set_field("number", p_value)

		# po_box member impt-field methods and properties
		#
		@property
		def po_box(self):
			return self._po_box

		@po_box.setter
		def po_box(self, p_value):
			self.set_field("po_box", p_value)

		# postdir member impt-field methods and properties
		#
		@property
		def postdir(self):
			return self._postdir

		@postdir.setter
		def postdir(self, p_value):
			self.set_field("postdir", p_value)

		# predir member impt-field methods and properties
		#
		@property
		def predir(self):
			return self._predir

		@predir.setter
		def predir(self, p_value):
			self.set_field("predir", p_value)

		# street member impt-field methods and properties
		#
		@property
		def street(self):
			return self._street

		@street.setter
		def street(self, p_value):
			self.set_field("street", p_value)

		# suffix member impt-field methods and properties
		#
		@property
		def suffix(self):
			return self._suffix

		@suffix.setter
		def suffix(self, p_value):
			self.set_field("suffix", p_value)

		# unit_full member impt-field methods and properties
		#
		@property
		def unit_full(self):
			return self._unit_full

		@unit_full.setter
		def unit_full(self, p_value):
			self.set_field("unit_full", p_value)

		# unit_name member impt-field methods and properties
		#
		@property
		def unit_name(self):
			return self._unit_name

		@unit_name.setter
		def unit_name(self, p_value):
			self.set_field("unit_name", p_value)

		# unit_range member impt-field methods and properties
		#
		@property
		def unit_range(self):
			return self._unit_range

		@unit_range.setter
		def unit_range(self, p_value):
			self.set_field("unit_range", p_value)

	# Phone impt-object defining Phone
	class Phone(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._is_primary = None
			self._number = None
			self._record_status = None
			self._type_code = None

		# is_primary member impt-field methods and properties
		#
		@property
		def is_primary(self):
			return self._is_primary

		@is_primary.setter
		def is_primary(self, p_value):
			self.set_field("is_primary", p_value)

		# number member impt-field methods and properties
		#
		@property
		def number(self):
			return self._number

		@number.setter
		def number(self, p_value):
			self.set_field("number", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

	# Pos impt-object defining Position
	class Pos(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._end_date = None
			self._facil_id = None
			self._facil_name = None
			self._info = None
			self._record_status = None
			self._start_date = None
			self._title = None
			self._type_code = None

		# end_date member impt-field methods and properties
		#
		@property
		def end_date(self):
			return self._end_date

		@end_date.setter
		def end_date(self, p_value):
			self.set_field("end_date", p_value)

		# facil_id member impt-field methods and properties
		#
		@property
		def facil_id(self):
			return self._facil_id

		@facil_id.setter
		def facil_id(self, p_value):
			self.set_field("facil_id", p_value)

		# facil_name member impt-field methods and properties
		#
		@property
		def facil_name(self):
			return self._facil_name

		@facil_name.setter
		def facil_name(self, p_value):
			self.set_field("facil_name", p_value)

		# info member impt-field methods and properties
		#
		@property
		def info(self):
			return self._info

		@info.setter
		def info(self, p_value):
			self.set_field("info", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# start_date member impt-field methods and properties
		#
		@property
		def start_date(self):
			return self._start_date

		@start_date.setter
		def start_date(self, p_value):
			self.set_field("start_date", p_value)

		# title member impt-field methods and properties
		#
		@property
		def title(self):
			return self._title

		@title.setter
		def title(self, p_value):
			self.set_field("title", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

	# Pra impt-object defining Practice
	class Pra(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._apndx = None
			self._dea_expiration = None
			self._dept = None
			self._hours = None
			self._info = None
			self._is_accepting = None
			self._is_medicaid = None
			self._is_medicare = None
			self._is_primary = None
			self._is_principal = None
			self._medicare_carrier_number = None
			self._name = None
			self._record_status = None
			self._title = None
			self._type_desc = None

			# impt-object members
			self._awd = {}
			self._datum = {}
			self._extid = {}
			self._facil = {}
			self._ident = {}
			self._insp = {}
			self._lang = {}

		#	awd member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Awd
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Awd
		#			      created internally

		def awd_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".awd[" + str(idx) + "]"
			self._awd[idx] = obj
			self._awd[idx].meta = Itom.Meta(path_text, idx, True)
			self._awd[idx].meta.core = self.meta.Core("award")
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._awd:
				self.awd_add(obj, idx)

		@property
		def awd(self):
			if self._awd.keys() == [0] and self.meta.collapse_not_indexed:
				return self._awd[0]
			else:
				return self._awd

		def awds(self):
			"""Value iterator for awd regardless of meta.collapse_not_indexed"""
			return self._awd.itervalues()

		def awd_indexes(self):
			return self._awd.keys()

		#	datum member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Datum
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Datum
		#			      created internally

		def datum_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".datum[" + str(idx) + "]"
			self._datum[idx] = obj
			self._datum[idx].meta = Itom.Meta(path_text, idx, True)
			self._datum[idx].meta.core = self.meta.Core("datum")
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._datum:
				self.datum_add(obj, idx)

		@property
		def datum(self):
			if self._datum.keys() == [0] and self.meta.collapse_not_indexed:
				return self._datum[0]
			else:
				return self._datum

		def datums(self):
			"""Value iterator for datum regardless of meta.collapse_not_indexed"""
			return self._datum.itervalues()

		def datum_indexes(self):
			return self._datum.keys()

		#	extid member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Extid
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Extid
		#			      created internally

		def extid_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".extid[" + str(idx) + "]"
			self._extid[idx] = obj
			self._extid[idx].meta = Itom.Meta(path_text, idx, True)
			self._extid[idx].meta.core = self.meta.Core("extid")
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._extid:
				self.extid_add(obj, idx)

		@property
		def extid(self):
			if self._extid.keys() == [0] and self.meta.collapse_not_indexed:
				return self._extid[0]
			else:
				return self._extid

		def extids(self):
			"""Value iterator for extid regardless of meta.collapse_not_indexed"""
			return self._extid.itervalues()

		def extid_indexes(self):
			return self._extid.keys()

		#	facil member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Facil
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Facil
		#			      created internally

		def facil_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".facil[" + str(idx) + "]"
			self._facil[idx] = obj
			self._facil[idx].meta = Itom.Meta(path_text, idx, False)
			self._facil[idx].meta.core = self.meta.Core("facility")
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Facil()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._facil:
				self.facil_add(obj, idx)

		@property
		def facil(self):
			if self._facil.keys() == [0] and self.meta.collapse_not_indexed:
				return self._facil[0]
			else:
				return self._facil

		def facils(self):
			"""Value iterator for facil regardless of meta.collapse_not_indexed"""
			return self._facil.itervalues()

		def facil_indexes(self):
			return self._facil.keys()

		#	ident member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Ident
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Ident
		#			      created internally

		def ident_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".ident[" + str(idx) + "]"
			self._ident[idx] = obj
			self._ident[idx].meta = Itom.Meta(path_text, idx, True)
			self._ident[idx].meta.core = self.meta.Core("identifier")
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._ident:
				self.ident_add(obj, idx)

		@property
		def ident(self):
			if self._ident.keys() == [0] and self.meta.collapse_not_indexed:
				return self._ident[0]
			else:
				return self._ident

		def idents(self):
			"""Value iterator for ident regardless of meta.collapse_not_indexed"""
			return self._ident.itervalues()

		def ident_indexes(self):
			return self._ident.keys()

		#	insp member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Insp
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Insp
		#			      created internally

		def insp_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Insp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".insp[" + str(idx) + "]"
			self._insp[idx] = obj
			self._insp[idx].meta = Itom.Meta(path_text, idx, True)
			self._insp[idx].meta.core = self.meta.Core("ins_plan")
			self.meta.active_objects_add_new("insp")

		def insp_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Insp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._insp:
				self.insp_add(obj, idx)

		@property
		def insp(self):
			if self._insp.keys() == [0] and self.meta.collapse_not_indexed:
				return self._insp[0]
			else:
				return self._insp

		def insps(self):
			"""Value iterator for insp regardless of meta.collapse_not_indexed"""
			return self._insp.itervalues()

		def insp_indexes(self):
			return self._insp.keys()

		#	lang member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Lang
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Lang
		#			      created internally

		def lang_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".lang[" + str(idx) + "]"
			self._lang[idx] = obj
			self._lang[idx].meta = Itom.Meta(path_text, idx, False)
			self._lang[idx].meta.core = self.meta.Core(None)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._lang:
				self.lang_add(obj, idx)

		@property
		def lang(self):
			if self._lang.keys() == [0] and self.meta.collapse_not_indexed:
				return self._lang[0]
			else:
				return self._lang

		def langs(self):
			"""Value iterator for lang regardless of meta.collapse_not_indexed"""
			return self._lang.itervalues()

		def lang_indexes(self):
			return self._lang.keys()

		# apndx member impt-field methods and properties
		#
		@property
		def apndx(self):
			return self._apndx

		@apndx.setter
		def apndx(self, p_value):
			self.set_field("apndx", p_value)

		# dea_expiration member impt-field methods and properties
		#
		@property
		def dea_expiration(self):
			return self._dea_expiration

		@dea_expiration.setter
		def dea_expiration(self, p_value):
			self.set_field("dea_expiration", p_value)

		# dept member impt-field methods and properties
		#
		@property
		def dept(self):
			return self._dept

		@dept.setter
		def dept(self, p_value):
			self.set_field("dept", p_value)

		# hours member impt-field methods and properties
		#
		@property
		def hours(self):
			return self._hours

		@hours.setter
		def hours(self, p_value):
			self.set_field("hours", p_value)

		# info member impt-field methods and properties
		#
		@property
		def info(self):
			return self._info

		@info.setter
		def info(self, p_value):
			self.set_field("info", p_value)

		# is_accepting member impt-field methods and properties
		#
		@property
		def is_accepting(self):
			return self._is_accepting

		@is_accepting.setter
		def is_accepting(self, p_value):
			self.set_field("is_accepting", p_value)

		# is_medicaid member impt-field methods and properties
		#
		@property
		def is_medicaid(self):
			return self._is_medicaid

		@is_medicaid.setter
		def is_medicaid(self, p_value):
			self.set_field("is_medicaid", p_value)

		# is_medicare member impt-field methods and properties
		#
		@property
		def is_medicare(self):
			return self._is_medicare

		@is_medicare.setter
		def is_medicare(self, p_value):
			self.set_field("is_medicare", p_value)

		# is_primary member impt-field methods and properties
		#
		@property
		def is_primary(self):
			return self._is_primary

		@is_primary.setter
		def is_primary(self, p_value):
			self.set_field("is_primary", p_value)

		# is_principal member impt-field methods and properties
		#
		@property
		def is_principal(self):
			return self._is_principal

		@is_principal.setter
		def is_principal(self, p_value):
			self.set_field("is_principal", p_value)

		# medicare_carrier_number member impt-field methods and properties
		#
		@property
		def medicare_carrier_number(self):
			return self._medicare_carrier_number

		@medicare_carrier_number.setter
		def medicare_carrier_number(self, p_value):
			self.set_field("medicare_carrier_number", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# title member impt-field methods and properties
		#
		@property
		def title(self):
			return self._title

		@title.setter
		def title(self, p_value):
			self.set_field("title", p_value)

		# type_desc member impt-field methods and properties
		#
		@property
		def type_desc(self):
			return self._type_desc

		@type_desc.setter
		def type_desc(self, p_value):
			self.set_field("type_desc", p_value)

	# Pro impt-object defining Provider
	class Pro(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._abmsuid = None
			self._birth_date = None
			self._birth_day = None
			self._birth_month = None
			self._birth_year = None
			self._clinical_interest = None
			self._degree_types = None
			self._display_name = None
			self._display_title = None
			self._ethnicity = None
			self._first_name = None
			self._full_name = None
			self._gender = None
			self._last_name = None
			self._master_id = None
			self._middle_name = None
			self._name_unique_in_impt = None
			self._nickname = None
			self._npi = None
			self._record_lock = None
			self._record_status = None
			self._standing_code = None
			self._status_code = None
			self._status_day = None
			self._status_month = None
			self._status_year = None
			self._suffix = None
			self._title = None
			self._type_ids = None

			# impt-object members
			self._alias = {}
			self._asn = {}
			self._awd = {}
			self._datum = {}
			self._degree = {}
			self._edu = {}
			self._extid = {}
			self._ident = {}
			self._insp = {}
			self._lang = {}
			self._lic = {}
			self._malp = {}
			self._mda = {}
			self._pos = {}
			self._pra = {}
			self._prof = {}
			self._sanc = {}
			self._spe = {}

		#	alias member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Alias
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Alias
		#			      created internally

		def alias_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Alias()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".alias[" + str(idx) + "]"
			self._alias[idx] = obj
			self._alias[idx].meta = Itom.Meta(path_text, idx, False)
			self._alias[idx].meta.core = self.meta.Core("name")
			self.meta.active_objects_add_new("alias")

		def alias_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Alias()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._alias:
				self.alias_add(obj, idx)

		@property
		def alias(self):
			if self._alias.keys() == [0] and self.meta.collapse_not_indexed:
				return self._alias[0]
			else:
				return self._alias

		def aliases(self):
			"""Value iterator for alias regardless of meta.collapse_not_indexed"""
			return self._alias.itervalues()

		def alias_indexes(self):
			return self._alias.keys()

		#	asn member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Asn
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Asn
		#			      created internally

		def asn_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Asn()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".asn[" + str(idx) + "]"
			self._asn[idx] = obj
			self._asn[idx].meta = Itom.Meta(path_text, idx, True)
			self._asn[idx].meta.core = self.meta.Core("association")
			self.meta.active_objects_add_new("asn")

		def asn_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Asn()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._asn:
				self.asn_add(obj, idx)

		@property
		def asn(self):
			if self._asn.keys() == [0] and self.meta.collapse_not_indexed:
				return self._asn[0]
			else:
				return self._asn

		def asns(self):
			"""Value iterator for asn regardless of meta.collapse_not_indexed"""
			return self._asn.itervalues()

		def asn_indexes(self):
			return self._asn.keys()

		#	awd member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Awd
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Awd
		#			      created internally

		def awd_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".awd[" + str(idx) + "]"
			self._awd[idx] = obj
			self._awd[idx].meta = Itom.Meta(path_text, idx, True)
			self._awd[idx].meta.core = self.meta.Core("award")
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Awd()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._awd:
				self.awd_add(obj, idx)

		@property
		def awd(self):
			if self._awd.keys() == [0] and self.meta.collapse_not_indexed:
				return self._awd[0]
			else:
				return self._awd

		def awds(self):
			"""Value iterator for awd regardless of meta.collapse_not_indexed"""
			return self._awd.itervalues()

		def awd_indexes(self):
			return self._awd.keys()

		#	datum member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Datum
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Datum
		#			      created internally

		def datum_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".datum[" + str(idx) + "]"
			self._datum[idx] = obj
			self._datum[idx].meta = Itom.Meta(path_text, idx, True)
			self._datum[idx].meta.core = self.meta.Core("datum")
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Datum()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._datum:
				self.datum_add(obj, idx)

		@property
		def datum(self):
			if self._datum.keys() == [0] and self.meta.collapse_not_indexed:
				return self._datum[0]
			else:
				return self._datum

		def datums(self):
			"""Value iterator for datum regardless of meta.collapse_not_indexed"""
			return self._datum.itervalues()

		def datum_indexes(self):
			return self._datum.keys()

		#	degree member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Degree
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Degree
		#			      created internally

		def degree_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Degree()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".degree[" + str(idx) + "]"
			self._degree[idx] = obj
			self._degree[idx].meta = Itom.Meta(path_text, idx, False)
			self._degree[idx].meta.core = self.meta.Core("degree")
			self.meta.active_objects_add_new("degree")

		def degree_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Degree()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._degree:
				self.degree_add(obj, idx)

		@property
		def degree(self):
			if self._degree.keys() == [0] and self.meta.collapse_not_indexed:
				return self._degree[0]
			else:
				return self._degree

		def degrees(self):
			"""Value iterator for degree regardless of meta.collapse_not_indexed"""
			return self._degree.itervalues()

		def degree_indexes(self):
			return self._degree.keys()

		#	edu member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Edu
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Edu
		#			      created internally

		def edu_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Edu()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".edu[" + str(idx) + "]"
			self._edu[idx] = obj
			self._edu[idx].meta = Itom.Meta(path_text, idx, True)
			self._edu[idx].meta.core = self.meta.Core("education")
			self.meta.active_objects_add_new("edu")

		def edu_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Edu()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._edu:
				self.edu_add(obj, idx)

		@property
		def edu(self):
			if self._edu.keys() == [0] and self.meta.collapse_not_indexed:
				return self._edu[0]
			else:
				return self._edu

		def edus(self):
			"""Value iterator for edu regardless of meta.collapse_not_indexed"""
			return self._edu.itervalues()

		def edu_indexes(self):
			return self._edu.keys()

		#	extid member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Extid
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Extid
		#			      created internally

		def extid_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".extid[" + str(idx) + "]"
			self._extid[idx] = obj
			self._extid[idx].meta = Itom.Meta(path_text, idx, True)
			self._extid[idx].meta.core = self.meta.Core("extid")
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Extid()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._extid:
				self.extid_add(obj, idx)

		@property
		def extid(self):
			if self._extid.keys() == [0] and self.meta.collapse_not_indexed:
				return self._extid[0]
			else:
				return self._extid

		def extids(self):
			"""Value iterator for extid regardless of meta.collapse_not_indexed"""
			return self._extid.itervalues()

		def extid_indexes(self):
			return self._extid.keys()

		#	ident member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Ident
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Ident
		#			      created internally

		def ident_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".ident[" + str(idx) + "]"
			self._ident[idx] = obj
			self._ident[idx].meta = Itom.Meta(path_text, idx, True)
			self._ident[idx].meta.core = self.meta.Core("identifier")
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Ident()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._ident:
				self.ident_add(obj, idx)

		@property
		def ident(self):
			if self._ident.keys() == [0] and self.meta.collapse_not_indexed:
				return self._ident[0]
			else:
				return self._ident

		def idents(self):
			"""Value iterator for ident regardless of meta.collapse_not_indexed"""
			return self._ident.itervalues()

		def ident_indexes(self):
			return self._ident.keys()

		#	insp member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Insp
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Insp
		#			      created internally

		def insp_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Insp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".insp[" + str(idx) + "]"
			self._insp[idx] = obj
			self._insp[idx].meta = Itom.Meta(path_text, idx, True)
			self._insp[idx].meta.core = self.meta.Core("ins_plan")
			self.meta.active_objects_add_new("insp")

		def insp_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Insp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._insp:
				self.insp_add(obj, idx)

		@property
		def insp(self):
			if self._insp.keys() == [0] and self.meta.collapse_not_indexed:
				return self._insp[0]
			else:
				return self._insp

		def insps(self):
			"""Value iterator for insp regardless of meta.collapse_not_indexed"""
			return self._insp.itervalues()

		def insp_indexes(self):
			return self._insp.keys()

		#	lang member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Lang
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Lang
		#			      created internally

		def lang_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".lang[" + str(idx) + "]"
			self._lang[idx] = obj
			self._lang[idx].meta = Itom.Meta(path_text, idx, False)
			self._lang[idx].meta.core = self.meta.Core(None)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lang()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._lang:
				self.lang_add(obj, idx)

		@property
		def lang(self):
			if self._lang.keys() == [0] and self.meta.collapse_not_indexed:
				return self._lang[0]
			else:
				return self._lang

		def langs(self):
			"""Value iterator for lang regardless of meta.collapse_not_indexed"""
			return self._lang.itervalues()

		def lang_indexes(self):
			return self._lang.keys()

		#	lic member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Lic
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Lic
		#			      created internally

		def lic_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lic()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".lic[" + str(idx) + "]"
			self._lic[idx] = obj
			self._lic[idx].meta = Itom.Meta(path_text, idx, False)
			self._lic[idx].meta.core = self.meta.Core("license")
			self.meta.active_objects_add_new("lic")

		def lic_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Lic()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._lic:
				self.lic_add(obj, idx)

		@property
		def lic(self):
			if self._lic.keys() == [0] and self.meta.collapse_not_indexed:
				return self._lic[0]
			else:
				return self._lic

		def lics(self):
			"""Value iterator for lic regardless of meta.collapse_not_indexed"""
			return self._lic.itervalues()

		def lic_indexes(self):
			return self._lic.keys()

		#	malp member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Malp
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Malp
		#			      created internally

		def malp_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Malp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".malp[" + str(idx) + "]"
			self._malp[idx] = obj
			self._malp[idx].meta = Itom.Meta(path_text, idx, True)
			self._malp[idx].meta.core = self.meta.Core("malpractice")
			self.meta.active_objects_add_new("malp")

		def malp_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Malp()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._malp:
				self.malp_add(obj, idx)

		@property
		def malp(self):
			if self._malp.keys() == [0] and self.meta.collapse_not_indexed:
				return self._malp[0]
			else:
				return self._malp

		def malps(self):
			"""Value iterator for malp regardless of meta.collapse_not_indexed"""
			return self._malp.itervalues()

		def malp_indexes(self):
			return self._malp.keys()

		#	mda member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Mda
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Mda
		#			      created internally

		def mda_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Mda()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".mda[" + str(idx) + "]"
			self._mda[idx] = obj
			self._mda[idx].meta = Itom.Meta(path_text, idx, True)
			self._mda[idx].meta.core = self.meta.Core("media")
			self.meta.active_objects_add_new("mda")

		def mda_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Mda()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._mda:
				self.mda_add(obj, idx)

		@property
		def mda(self):
			if self._mda.keys() == [0] and self.meta.collapse_not_indexed:
				return self._mda[0]
			else:
				return self._mda

		def mdas(self):
			"""Value iterator for mda regardless of meta.collapse_not_indexed"""
			return self._mda.itervalues()

		def mda_indexes(self):
			return self._mda.keys()

		#	pos member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Pos
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Pos
		#			      created internally

		def pos_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Pos()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".pos[" + str(idx) + "]"
			self._pos[idx] = obj
			self._pos[idx].meta = Itom.Meta(path_text, idx, True)
			self._pos[idx].meta.core = self.meta.Core("position")
			self.meta.active_objects_add_new("pos")

		def pos_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Pos()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._pos:
				self.pos_add(obj, idx)

		@property
		def pos(self):
			if self._pos.keys() == [0] and self.meta.collapse_not_indexed:
				return self._pos[0]
			else:
				return self._pos

		def poses(self):
			"""Value iterator for pos regardless of meta.collapse_not_indexed"""
			return self._pos.itervalues()

		def pos_indexes(self):
			return self._pos.keys()

		#	pra member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Pra
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Pra
		#			      created internally

		def pra_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Pra()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".pra[" + str(idx) + "]"
			self._pra[idx] = obj
			self._pra[idx].meta = Itom.Meta(path_text, idx, True)
			self._pra[idx].meta.core = self.meta.Core("practice")
			self.meta.active_objects_add_new("pra")

		def pra_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Pra()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._pra:
				self.pra_add(obj, idx)

		@property
		def pra(self):
			if self._pra.keys() == [0] and self.meta.collapse_not_indexed:
				return self._pra[0]
			else:
				return self._pra

		def pras(self):
			"""Value iterator for pra regardless of meta.collapse_not_indexed"""
			return self._pra.itervalues()

		def pra_indexes(self):
			return self._pra.keys()

		#	prof member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Prof
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Prof
		#			      created internally

		def prof_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Prof()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".prof[" + str(idx) + "]"
			self._prof[idx] = obj
			self._prof[idx].meta = Itom.Meta(path_text, idx, False)
			self._prof[idx].meta.core = self.meta.Core("profession")
			self.meta.active_objects_add_new("prof")

		def prof_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Prof()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._prof:
				self.prof_add(obj, idx)

		@property
		def prof(self):
			if self._prof.keys() == [0] and self.meta.collapse_not_indexed:
				return self._prof[0]
			else:
				return self._prof

		def profs(self):
			"""Value iterator for prof regardless of meta.collapse_not_indexed"""
			return self._prof.itervalues()

		def prof_indexes(self):
			return self._prof.keys()

		#	sanc member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Sanc
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Sanc
		#			      created internally

		def sanc_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Sanc()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".sanc[" + str(idx) + "]"
			self._sanc[idx] = obj
			self._sanc[idx].meta = Itom.Meta(path_text, idx, True)
			self._sanc[idx].meta.core = self.meta.Core("sanction")
			self.meta.active_objects_add_new("sanc")

		def sanc_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Sanc()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._sanc:
				self.sanc_add(obj, idx)

		@property
		def sanc(self):
			if self._sanc.keys() == [0] and self.meta.collapse_not_indexed:
				return self._sanc[0]
			else:
				return self._sanc

		def sancs(self):
			"""Value iterator for sanc regardless of meta.collapse_not_indexed"""
			return self._sanc.itervalues()

		def sanc_indexes(self):
			return self._sanc.keys()

		#	spe member impt-object methods and properties
		#		Parameters
		#			arg1: instance of impt-object class Impt.Spe
		#			arg2: index for instance, if None, 0 is assumed
		#		- or -
		#			arg1: index for instance, if None, 0 is assumed
		#			      instance of impt-object class Impt.Spe
		#			      created internally

		def spe_add(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			path_text = self.meta.path.text + ".spe[" + str(idx) + "]"
			self._spe[idx] = obj
			self._spe[idx].meta = Itom.Meta(path_text, idx, True)
			self._spe[idx].meta.core = self.meta.Core("field_specialty")
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_arg1, *args):
			if len(args) == 0:
				obj = Impt.Spe()
				idx = p_arg1
			else:
				obj = p_arg1
				idx = args[0]
			if idx is None:
				idx = 0
			if idx not in self._spe:
				self.spe_add(obj, idx)

		@property
		def spe(self):
			if self._spe.keys() == [0] and self.meta.collapse_not_indexed:
				return self._spe[0]
			else:
				return self._spe

		def spes(self):
			"""Value iterator for spe regardless of meta.collapse_not_indexed"""
			return self._spe.itervalues()

		def spe_indexes(self):
			return self._spe.keys()

		# abmsuid member impt-field methods and properties
		#
		@property
		def abmsuid(self):
			return self._abmsuid

		@abmsuid.setter
		def abmsuid(self, p_value):
			self.set_field("abmsuid", p_value)

		# birth_date member impt-field methods and properties
		#
		@property
		def birth_date(self):
			return self._birth_date

		@birth_date.setter
		def birth_date(self, p_value):
			self.set_field("birth_date", p_value)

		# birth_day member impt-field methods and properties
		#
		@property
		def birth_day(self):
			return self._birth_day

		@birth_day.setter
		def birth_day(self, p_value):
			self.set_field("birth_day", p_value)

		# birth_month member impt-field methods and properties
		#
		@property
		def birth_month(self):
			return self._birth_month

		@birth_month.setter
		def birth_month(self, p_value):
			self.set_field("birth_month", p_value)

		# birth_year member impt-field methods and properties
		#
		@property
		def birth_year(self):
			return self._birth_year

		@birth_year.setter
		def birth_year(self, p_value):
			self.set_field("birth_year", p_value)

		# clinical_interest member impt-field methods and properties
		#
		@property
		def clinical_interest(self):
			return self._clinical_interest

		@clinical_interest.setter
		def clinical_interest(self, p_value):
			self.set_field("clinical_interest", p_value)

		# degree_types member impt-field methods and properties
		#
		@property
		def degree_types(self):
			return self._degree_types

		@degree_types.setter
		def degree_types(self, p_value):
			self.set_field("degree_types", p_value)

		# display_name member impt-field methods and properties
		#
		@property
		def display_name(self):
			return self._display_name

		@display_name.setter
		def display_name(self, p_value):
			self.set_field("display_name", p_value)

		# display_title member impt-field methods and properties
		#
		@property
		def display_title(self):
			return self._display_title

		@display_title.setter
		def display_title(self, p_value):
			self.set_field("display_title", p_value)

		# ethnicity member impt-field methods and properties
		#
		@property
		def ethnicity(self):
			return self._ethnicity

		@ethnicity.setter
		def ethnicity(self, p_value):
			self.set_field("ethnicity", p_value)

		# first_name member impt-field methods and properties
		#
		@property
		def first_name(self):
			return self._first_name

		@first_name.setter
		def first_name(self, p_value):
			self.set_field("first_name", p_value)

		# full_name member impt-field methods and properties
		#
		@property
		def full_name(self):
			return self._full_name

		@full_name.setter
		def full_name(self, p_value):
			self.set_field("full_name", p_value)

		# gender member impt-field methods and properties
		#
		@property
		def gender(self):
			return self._gender

		@gender.setter
		def gender(self, p_value):
			self.set_field("gender", p_value)

		# last_name member impt-field methods and properties
		#
		@property
		def last_name(self):
			return self._last_name

		@last_name.setter
		def last_name(self, p_value):
			self.set_field("last_name", p_value)

		# master_id member impt-field methods and properties
		#
		@property
		def master_id(self):
			return self._master_id

		@master_id.setter
		def master_id(self, p_value):
			self.set_field("master_id", p_value)

		# middle_name member impt-field methods and properties
		#
		@property
		def middle_name(self):
			return self._middle_name

		@middle_name.setter
		def middle_name(self, p_value):
			self.set_field("middle_name", p_value)

		# name_unique_in_impt member impt-field methods and properties
		#
		@property
		def name_unique_in_impt(self):
			return self._name_unique_in_impt

		@name_unique_in_impt.setter
		def name_unique_in_impt(self, p_value):
			self.set_field("name_unique_in_impt", p_value)

		# nickname member impt-field methods and properties
		#
		@property
		def nickname(self):
			return self._nickname

		@nickname.setter
		def nickname(self, p_value):
			self.set_field("nickname", p_value)

		# npi member impt-field methods and properties
		#
		@property
		def npi(self):
			return self._npi

		@npi.setter
		def npi(self, p_value):
			self.set_field("npi", p_value)

		# record_lock member impt-field methods and properties
		#
		@property
		def record_lock(self):
			return self._record_lock

		@record_lock.setter
		def record_lock(self, p_value):
			self.set_field("record_lock", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# standing_code member impt-field methods and properties
		#
		@property
		def standing_code(self):
			return self._standing_code

		@standing_code.setter
		def standing_code(self, p_value):
			self.set_field("standing_code", p_value)

		# status_code member impt-field methods and properties
		#
		@property
		def status_code(self):
			return self._status_code

		@status_code.setter
		def status_code(self, p_value):
			self.set_field("status_code", p_value)

		# status_day member impt-field methods and properties
		#
		@property
		def status_day(self):
			return self._status_day

		@status_day.setter
		def status_day(self, p_value):
			self.set_field("status_day", p_value)

		# status_month member impt-field methods and properties
		#
		@property
		def status_month(self):
			return self._status_month

		@status_month.setter
		def status_month(self, p_value):
			self.set_field("status_month", p_value)

		# status_year member impt-field methods and properties
		#
		@property
		def status_year(self):
			return self._status_year

		@status_year.setter
		def status_year(self, p_value):
			self.set_field("status_year", p_value)

		# suffix member impt-field methods and properties
		#
		@property
		def suffix(self):
			return self._suffix

		@suffix.setter
		def suffix(self, p_value):
			self.set_field("suffix", p_value)

		# title member impt-field methods and properties
		#
		@property
		def title(self):
			return self._title

		@title.setter
		def title(self, p_value):
			self.set_field("title", p_value)

		# type_ids member impt-field methods and properties
		#
		@property
		def type_ids(self):
			return self._type_ids

		@type_ids.setter
		def type_ids(self, p_value):
			self.set_field("type_ids", p_value)

	# Prof impt-object defining Profession
	class Prof(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._code = None
			self._record_status = None

		# code member impt-field methods and properties
		#
		@property
		def code(self):
			return self._code

		@code.setter
		def code(self, p_value):
			self.set_field("code", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

	# Ref impt-object defining Referral
	class Ref(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._desc = None
			self._name = None
			self._record_status = None
			self._type_code = None

		# desc member impt-field methods and properties
		#
		@property
		def desc(self):
			return self._desc

		@desc.setter
		def desc(self, p_value):
			self.set_field("desc", p_value)

		# name member impt-field methods and properties
		#
		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, p_value):
			self.set_field("name", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

	# Sanc impt-object defining Sanction
	class Sanc(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._action = None
			self._action_type_code = None
			self._authority = None
			self._end_date = None
			self._info = None
			self._reason = None
			self._record_status = None
			self._start_date = None
			self._state_code = None
			self._term = None
			self._type_code = None

		# action member impt-field methods and properties
		#
		@property
		def action(self):
			return self._action

		@action.setter
		def action(self, p_value):
			self.set_field("action", p_value)

		# action_type_code member impt-field methods and properties
		#
		@property
		def action_type_code(self):
			return self._action_type_code

		@action_type_code.setter
		def action_type_code(self, p_value):
			self.set_field("action_type_code", p_value)

		# authority member impt-field methods and properties
		#
		@property
		def authority(self):
			return self._authority

		@authority.setter
		def authority(self, p_value):
			self.set_field("authority", p_value)

		# end_date member impt-field methods and properties
		#
		@property
		def end_date(self):
			return self._end_date

		@end_date.setter
		def end_date(self, p_value):
			self.set_field("end_date", p_value)

		# info member impt-field methods and properties
		#
		@property
		def info(self):
			return self._info

		@info.setter
		def info(self, p_value):
			self.set_field("info", p_value)

		# reason member impt-field methods and properties
		#
		@property
		def reason(self):
			return self._reason

		@reason.setter
		def reason(self, p_value):
			self.set_field("reason", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# start_date member impt-field methods and properties
		#
		@property
		def start_date(self):
			return self._start_date

		@start_date.setter
		def start_date(self, p_value):
			self.set_field("start_date", p_value)

		# state_code member impt-field methods and properties
		#
		@property
		def state_code(self):
			return self._state_code

		@state_code.setter
		def state_code(self, p_value):
			self.set_field("state_code", p_value)

		# term member impt-field methods and properties
		#
		@property
		def term(self):
			return self._term

		@term.setter
		def term(self, p_value):
			self.set_field("term", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

	# Spe impt-object defining Field Specialty
	class Spe(Itom):

		def __init__(self, p_path=None, p_index=None):
			Itom.__init__(self)

			# impt-field members
			self._apndx = None
			self._desc = None
			self._field_specialty_id = None
			self._is_primary = None
			self._is_principal = None
			self._record_status = None
			self._role_code = None
			self._self_rept_cert = None
			self._status_code = None
			self._type_code = None

		# apndx member impt-field methods and properties
		#
		@property
		def apndx(self):
			return self._apndx

		@apndx.setter
		def apndx(self, p_value):
			self.set_field("apndx", p_value)

		# desc member impt-field methods and properties
		#
		@property
		def desc(self):
			return self._desc

		@desc.setter
		def desc(self, p_value):
			self.set_field("desc", p_value)

		# field_specialty_id member impt-field methods and properties
		#
		@property
		def field_specialty_id(self):
			return self._field_specialty_id

		@field_specialty_id.setter
		def field_specialty_id(self, p_value):
			self.set_field("field_specialty_id", p_value)

		# is_primary member impt-field methods and properties
		#
		@property
		def is_primary(self):
			return self._is_primary

		@is_primary.setter
		def is_primary(self, p_value):
			self.set_field("is_primary", p_value)

		# is_principal member impt-field methods and properties
		#
		@property
		def is_principal(self):
			return self._is_principal

		@is_principal.setter
		def is_principal(self, p_value):
			self.set_field("is_principal", p_value)

		# record_status member impt-field methods and properties
		#
		@property
		def record_status(self):
			return self._record_status

		@record_status.setter
		def record_status(self, p_value):
			self.set_field("record_status", p_value)

		# role_code member impt-field methods and properties
		#
		@property
		def role_code(self):
			return self._role_code

		@role_code.setter
		def role_code(self, p_value):
			self.set_field("role_code", p_value)

		# self_rept_cert member impt-field methods and properties
		#
		@property
		def self_rept_cert(self):
			return self._self_rept_cert

		@self_rept_cert.setter
		def self_rept_cert(self, p_value):
			self.set_field("self_rept_cert", p_value)

		# status_code member impt-field methods and properties
		#
		@property
		def status_code(self):
			return self._status_code

		@status_code.setter
		def status_code(self, p_value):
			self.set_field("status_code", p_value)

		# type_code member impt-field methods and properties
		#
		@property
		def type_code(self):
			return self._type_code

		@type_code.setter
		def type_code(self, p_value):
			self.set_field("type_code", p_value)

