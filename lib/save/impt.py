# From mdx_lib.impt_generate_itom_py()
# Impt class ORM based on the Import Template Object Model (iTOM) generated on 2017-02-15 17:34:41.984559-05
from itom import *

# Import Template object
class Impt(Itom):

	def __init__(self, p_index=None, p_path=None):
		Itom.__init__(self, p_index, p_path)

		# field-type members
		self.date = None
		self.facility_id = None
		self.fail_msg = None
		self.id = None
		self.provider_id = None
		self.seq = None
		self.source_date = None
		self.status = None

		# object-type members
		self._facil = {}
		self._pro = {}

	def facil_add(self, p_facil, p_index, p_path=None):
		self._facil[p_index] = p_facil
		self._facil[p_index].meta = Itom.Meta(p_index, p_path)
		self.meta.active_objects_add_new("facil")

	def facil_add_new(self, p_facil, p_index, p_path=None):
		if p_index not in self._facil:
			self.facil_add(p_facil, p_index, p_path)

	@property
	def facil(self):
		return self._facil

	def facil_indexes(self):
		return self._facil.keys()

	def pro_add(self, p_pro, p_index, p_path=None):
		self._pro[p_index] = p_pro
		self._pro[p_index].meta = Itom.Meta(p_index, p_path)
		self.meta.active_objects_add_new("pro")

	def pro_add_new(self, p_pro, p_index, p_path=None):
		if p_index not in self._pro:
			self.pro_add(p_pro, p_index, p_path)

	@property
	def pro(self):
		return self._pro

	def pro_indexes(self):
		return self._pro.keys()


	# Address object
	class Addr(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.department = None
			self.identifier = None
			self.is_primary = None
			self.lat = None
			self.line1 = None
			self.line2 = None
			self.location_id = None
			self.long = None
			self.name = None
			self.type_code = None

			# object-type members
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

		def awd_add(self, p_awd, p_index, p_path=None):
			self._awd[p_index] = p_awd
			self._awd[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_awd, p_index, p_path=None):
			if p_index not in self._awd:
				self.awd_add(p_awd, p_index, p_path)

		@property
		def awd(self):
			return self._awd

		def awd_indexes(self):
			return self._awd.keys()

		def datum_add(self, p_datum, p_index, p_path=None):
			self._datum[p_index] = p_datum
			self._datum[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_datum, p_index, p_path=None):
			if p_index not in self._datum:
				self.datum_add(p_datum, p_index, p_path)

		@property
		def datum(self):
			return self._datum

		def datum_indexes(self):
			return self._datum.keys()

		def extid_add(self, p_extid, p_index, p_path=None):
			self._extid[p_index] = p_extid
			self._extid[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_extid, p_index, p_path=None):
			if p_index not in self._extid:
				self.extid_add(p_extid, p_index, p_path)

		@property
		def extid(self):
			return self._extid

		def extid_indexes(self):
			return self._extid.keys()

		def ident_add(self, p_ident, p_index, p_path=None):
			self._ident[p_index] = p_ident
			self._ident[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_ident, p_index, p_path=None):
			if p_index not in self._ident:
				self.ident_add(p_ident, p_index, p_path)

		@property
		def ident(self):
			return self._ident

		def ident_indexes(self):
			return self._ident.keys()

		def insp_add(self, p_insp, p_index, p_path=None):
			self._insp[p_index] = p_insp
			self._insp[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("insp")

		def insp_add_new(self, p_insp, p_index, p_path=None):
			if p_index not in self._insp:
				self.insp_add(p_insp, p_index, p_path)

		@property
		def insp(self):
			return self._insp

		def insp_indexes(self):
			return self._insp.keys()

		def lang_add(self, p_lang, p_index, p_path=None):
			self._lang[p_index] = p_lang
			self._lang[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_lang, p_index, p_path=None):
			if p_index not in self._lang:
				self.lang_add(p_lang, p_index, p_path)

		@property
		def lang(self):
			return self._lang

		def lang_indexes(self):
			return self._lang.keys()

		def mda_add(self, p_mda, p_index, p_path=None):
			self._mda[p_index] = p_mda
			self._mda[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("mda")

		def mda_add_new(self, p_mda, p_index, p_path=None):
			if p_index not in self._mda:
				self.mda_add(p_mda, p_index, p_path)

		@property
		def mda(self):
			return self._mda

		def mda_indexes(self):
			return self._mda.keys()

		def parsed_add(self, p_parsed, p_index, p_path=None):
			self._parsed[p_index] = p_parsed
			self._parsed[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("parsed")

		def parsed_add_new(self, p_parsed, p_index, p_path=None):
			if p_index not in self._parsed:
				self.parsed_add(p_parsed, p_index, p_path)

		@property
		def parsed(self):
			return self._parsed

		def parsed_indexes(self):
			return self._parsed.keys()

		def phone_add(self, p_phone, p_index, p_path=None):
			self._phone[p_index] = p_phone
			self._phone[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("phone")

		def phone_add_new(self, p_phone, p_index, p_path=None):
			if p_index not in self._phone:
				self.phone_add(p_phone, p_index, p_path)

		@property
		def phone(self):
			return self._phone

		def phone_indexes(self):
			return self._phone.keys()

		def spe_add(self, p_spe, p_index, p_path=None):
			self._spe[p_index] = p_spe
			self._spe[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_spe, p_index, p_path=None):
			if p_index not in self._spe:
				self.spe_add(p_spe, p_index, p_path)

		@property
		def spe(self):
			return self._spe

		def spe_indexes(self):
			return self._spe.keys()

	# Affiliation object
	class Affil(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.dept = None
			self.desc = None
			self.info = None
			self.is_practicing = None
			self.name = None
			self.position = None
			self.record_status = None
			self.start_date = None

			# object-type members
			self._facil = {}

		def facil_add(self, p_facil, p_index, p_path=None):
			self._facil[p_index] = p_facil
			self._facil[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_facil, p_index, p_path=None):
			if p_index not in self._facil:
				self.facil_add(p_facil, p_index, p_path)

		@property
		def facil(self):
			return self._facil

		def facil_indexes(self):
			return self._facil.keys()

	# Alias object
	class Alias(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.first_name = None
			self.last_name = None
			self.middle_name = None
			self.name = None
			self.suffix = None

	# Association object
	class Asn(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.association_id = None
			self.end_year = None
			self.institution = None
			self.record_status = None
			self.start_year = None
			self.title = None
			self.type_code = None

	# Award object
	class Awd(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.end_year = None
			self.institution = None
			self.name = None
			self.record_status = None
			self.start_year = None
			self.type_code = None
			self.value = None
			self.website_url = None

	# Data object
	class Datum(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.desc = None
			self.record_status = None
			self.type_code = None
			self.value = None

	# Degree object
	class Degree(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.code = None
			self.record_status = None

	# Education object
	class Edu(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.end_date = None
			self.end_day = None
			self.end_month = None
			self.end_year = None
			self.is_foreign = None
			self.record_status = None
			self.start_date = None
			self.start_day = None
			self.start_month = None
			self.start_year = None
			self.type_code = None

			# object-type members
			self._degree = {}
			self._facil = {}
			self._spe = {}

		def degree_add(self, p_degree, p_index, p_path=None):
			self._degree[p_index] = p_degree
			self._degree[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("degree")

		def degree_add_new(self, p_degree, p_index, p_path=None):
			if p_index not in self._degree:
				self.degree_add(p_degree, p_index, p_path)

		@property
		def degree(self):
			return self._degree

		def degree_indexes(self):
			return self._degree.keys()

		def facil_add(self, p_facil, p_index, p_path=None):
			self._facil[p_index] = p_facil
			self._facil[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_facil, p_index, p_path=None):
			if p_index not in self._facil:
				self.facil_add(p_facil, p_index, p_path)

		@property
		def facil(self):
			return self._facil

		def facil_indexes(self):
			return self._facil.keys()

		def spe_add(self, p_spe, p_index, p_path=None):
			self._spe[p_index] = p_spe
			self._spe[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_spe, p_index, p_path=None):
			if p_index not in self._spe:
				self.spe_add(p_spe, p_index, p_path)

		@property
		def spe(self):
			return self._spe

		def spe_indexes(self):
			return self._spe.keys()

	# External ID object
	class Extid(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.record_status = None
			self.source_code = None
			self.value = None

	# Facility object
	class Facil(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.city = None
			self.country = None
			self.facility_id = None
			self.hours = None
			self.is_primary = None
			self.lat = None
			self.long = None
			self.master_id = None
			self.name = None
			self.record_status = None
			self.state = None
			self.status_code = None
			self.type_code = None
			self.zip = None

			# object-type members
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

		def addr_add(self, p_addr, p_index, p_path=None):
			self._addr[p_index] = p_addr
			self._addr[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("addr")

		def addr_add_new(self, p_addr, p_index, p_path=None):
			if p_index not in self._addr:
				self.addr_add(p_addr, p_index, p_path)

		@property
		def addr(self):
			return self._addr

		def addr_indexes(self):
			return self._addr.keys()

		def affil_add(self, p_affil, p_index, p_path=None):
			self._affil[p_index] = p_affil
			self._affil[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("affil")

		def affil_add_new(self, p_affil, p_index, p_path=None):
			if p_index not in self._affil:
				self.affil_add(p_affil, p_index, p_path)

		@property
		def affil(self):
			return self._affil

		def affil_indexes(self):
			return self._affil.keys()

		def alias_add(self, p_alias, p_index, p_path=None):
			self._alias[p_index] = p_alias
			self._alias[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("alias")

		def alias_add_new(self, p_alias, p_index, p_path=None):
			if p_index not in self._alias:
				self.alias_add(p_alias, p_index, p_path)

		@property
		def alias(self):
			return self._alias

		def alias_indexes(self):
			return self._alias.keys()

		def awd_add(self, p_awd, p_index, p_path=None):
			self._awd[p_index] = p_awd
			self._awd[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_awd, p_index, p_path=None):
			if p_index not in self._awd:
				self.awd_add(p_awd, p_index, p_path)

		@property
		def awd(self):
			return self._awd

		def awd_indexes(self):
			return self._awd.keys()

		def datum_add(self, p_datum, p_index, p_path=None):
			self._datum[p_index] = p_datum
			self._datum[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_datum, p_index, p_path=None):
			if p_index not in self._datum:
				self.datum_add(p_datum, p_index, p_path)

		@property
		def datum(self):
			return self._datum

		def datum_indexes(self):
			return self._datum.keys()

		def extid_add(self, p_extid, p_index, p_path=None):
			self._extid[p_index] = p_extid
			self._extid[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_extid, p_index, p_path=None):
			if p_index not in self._extid:
				self.extid_add(p_extid, p_index, p_path)

		@property
		def extid(self):
			return self._extid

		def extid_indexes(self):
			return self._extid.keys()

		def ident_add(self, p_ident, p_index, p_path=None):
			self._ident[p_index] = p_ident
			self._ident[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_ident, p_index, p_path=None):
			if p_index not in self._ident:
				self.ident_add(p_ident, p_index, p_path)

		@property
		def ident(self):
			return self._ident

		def ident_indexes(self):
			return self._ident.keys()

		def lang_add(self, p_lang, p_index, p_path=None):
			self._lang[p_index] = p_lang
			self._lang[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_lang, p_index, p_path=None):
			if p_index not in self._lang:
				self.lang_add(p_lang, p_index, p_path)

		@property
		def lang(self):
			return self._lang

		def lang_indexes(self):
			return self._lang.keys()

		def mda_add(self, p_mda, p_index, p_path=None):
			self._mda[p_index] = p_mda
			self._mda[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("mda")

		def mda_add_new(self, p_mda, p_index, p_path=None):
			if p_index not in self._mda:
				self.mda_add(p_mda, p_index, p_path)

		@property
		def mda(self):
			return self._mda

		def mda_indexes(self):
			return self._mda.keys()

		def parent_add(self, p_parent, p_index, p_path=None):
			self._parent[p_index] = p_parent
			self._parent[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("parent")

		def parent_add_new(self, p_parent, p_index, p_path=None):
			if p_index not in self._parent:
				self.parent_add(p_parent, p_index, p_path)

		@property
		def parent(self):
			return self._parent

		def parent_indexes(self):
			return self._parent.keys()

	# Identifier object
	class Ident(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.record_status = None
			self.type_id = None
			self.value = None

	# Insurance Plan object
	class Insp(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.desc = None
			self.info = None
			self.ins_plan_id = None
			self.record_status = None

			# object-type members
			self._affil = {}
			self._awd = {}
			self._datum = {}
			self._extid = {}
			self._ident = {}
			self._ref = {}
			self._spe = {}

		def affil_add(self, p_affil, p_index, p_path=None):
			self._affil[p_index] = p_affil
			self._affil[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("affil")

		def affil_add_new(self, p_affil, p_index, p_path=None):
			if p_index not in self._affil:
				self.affil_add(p_affil, p_index, p_path)

		@property
		def affil(self):
			return self._affil

		def affil_indexes(self):
			return self._affil.keys()

		def awd_add(self, p_awd, p_index, p_path=None):
			self._awd[p_index] = p_awd
			self._awd[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_awd, p_index, p_path=None):
			if p_index not in self._awd:
				self.awd_add(p_awd, p_index, p_path)

		@property
		def awd(self):
			return self._awd

		def awd_indexes(self):
			return self._awd.keys()

		def datum_add(self, p_datum, p_index, p_path=None):
			self._datum[p_index] = p_datum
			self._datum[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_datum, p_index, p_path=None):
			if p_index not in self._datum:
				self.datum_add(p_datum, p_index, p_path)

		@property
		def datum(self):
			return self._datum

		def datum_indexes(self):
			return self._datum.keys()

		def extid_add(self, p_extid, p_index, p_path=None):
			self._extid[p_index] = p_extid
			self._extid[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_extid, p_index, p_path=None):
			if p_index not in self._extid:
				self.extid_add(p_extid, p_index, p_path)

		@property
		def extid(self):
			return self._extid

		def extid_indexes(self):
			return self._extid.keys()

		def ident_add(self, p_ident, p_index, p_path=None):
			self._ident[p_index] = p_ident
			self._ident[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_ident, p_index, p_path=None):
			if p_index not in self._ident:
				self.ident_add(p_ident, p_index, p_path)

		@property
		def ident(self):
			return self._ident

		def ident_indexes(self):
			return self._ident.keys()

		def ref_add(self, p_ref, p_index, p_path=None):
			self._ref[p_index] = p_ref
			self._ref[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("ref")

		def ref_add_new(self, p_ref, p_index, p_path=None):
			if p_index not in self._ref:
				self.ref_add(p_ref, p_index, p_path)

		@property
		def ref(self):
			return self._ref

		def ref_indexes(self):
			return self._ref.keys()

		def spe_add(self, p_spe, p_index, p_path=None):
			self._spe[p_index] = p_spe
			self._spe[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_spe, p_index, p_path=None):
			if p_index not in self._spe:
				self.spe_add(p_spe, p_index, p_path)

		@property
		def spe(self):
			return self._spe

		def spe_indexes(self):
			return self._spe.keys()

	# Language object
	class Lang(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.code = None
			self.name = None
			self.record_status = None

	# License object
	class Lic(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.end_date = None
			self.exam_type = None
			self.issue_date = None
			self.last_renewed = None
			self.nbr = None
			self.obtained_by = None
			self.start_date = None
			self.state = None
			self.status_code = None
			self.status_desc = None

			# object-type members
			self._prof = {}

		def prof_add(self, p_prof, p_index, p_path=None):
			self._prof[p_index] = p_prof
			self._prof[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("prof")

		def prof_add_new(self, p_prof, p_index, p_path=None):
			if p_index not in self._prof:
				self.prof_add(p_prof, p_index, p_path)

		@property
		def prof(self):
			return self._prof

		def prof_indexes(self):
			return self._prof.keys()

	# Malpractice object
	class Malp(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.amount = None
			self.claim = None
			self.date = None
			self.info = None
			self.reason = None
			self.record_status = None
			self.reference = None
			self.state_code = None

	# Media object
	class Mda(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.category_code = None
			self.dest_url = None
			self.orig_source = None
			self.record_status = None
			self.source = None
			self.source_code = None

	# Parent Facility object
	class Parent(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# object-type members
			self._facil = {}

		def facil_add(self, p_facil, p_index, p_path=None):
			self._facil[p_index] = p_facil
			self._facil[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_facil, p_index, p_path=None):
			if p_index not in self._facil:
				self.facil_add(p_facil, p_index, p_path)

		@property
		def facil(self):
			return self._facil

		def facil_indexes(self):
			return self._facil.keys()

	# Parsed object
	class Parsed(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.codes = None
			self.is_validated = None
			self.lat = None
			self.long = None
			self.number = None
			self.po_box = None
			self.postdir = None
			self.predir = None
			self.street = None
			self.suffix = None
			self.unit_full = None
			self.unit_name = None
			self.unit_range = None

	# Phone object
	class Phone(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.is_primary = None
			self.number = None
			self.record_status = None
			self.type_code = None

	# Position object
	class Pos(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.end_date = None
			self.facil_id = None
			self.facil_name = None
			self.info = None
			self.record_status = None
			self.start_date = None
			self.title = None
			self.type_code = None

	# Practice object
	class Pra(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.apndx = None
			self.dea_expiration = None
			self.dept = None
			self.hours = None
			self.info = None
			self.is_accepting = None
			self.is_medicaid = None
			self.is_medicare = None
			self.is_primary = None
			self.is_principal = None
			self.medicare_carrier_number = None
			self.record_status = None
			self.title = None
			self.type_desc = None

			# object-type members
			self._awd = {}
			self._datum = {}
			self._extid = {}
			self._facil = {}
			self._ident = {}
			self._insp = {}
			self._lang = {}

		def awd_add(self, p_awd, p_index, p_path=None):
			self._awd[p_index] = p_awd
			self._awd[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_awd, p_index, p_path=None):
			if p_index not in self._awd:
				self.awd_add(p_awd, p_index, p_path)

		@property
		def awd(self):
			return self._awd

		def awd_indexes(self):
			return self._awd.keys()

		def datum_add(self, p_datum, p_index, p_path=None):
			self._datum[p_index] = p_datum
			self._datum[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_datum, p_index, p_path=None):
			if p_index not in self._datum:
				self.datum_add(p_datum, p_index, p_path)

		@property
		def datum(self):
			return self._datum

		def datum_indexes(self):
			return self._datum.keys()

		def extid_add(self, p_extid, p_index, p_path=None):
			self._extid[p_index] = p_extid
			self._extid[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_extid, p_index, p_path=None):
			if p_index not in self._extid:
				self.extid_add(p_extid, p_index, p_path)

		@property
		def extid(self):
			return self._extid

		def extid_indexes(self):
			return self._extid.keys()

		def facil_add(self, p_facil, p_index, p_path=None):
			self._facil[p_index] = p_facil
			self._facil[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("facil")

		def facil_add_new(self, p_facil, p_index, p_path=None):
			if p_index not in self._facil:
				self.facil_add(p_facil, p_index, p_path)

		@property
		def facil(self):
			return self._facil

		def facil_indexes(self):
			return self._facil.keys()

		def ident_add(self, p_ident, p_index, p_path=None):
			self._ident[p_index] = p_ident
			self._ident[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_ident, p_index, p_path=None):
			if p_index not in self._ident:
				self.ident_add(p_ident, p_index, p_path)

		@property
		def ident(self):
			return self._ident

		def ident_indexes(self):
			return self._ident.keys()

		def insp_add(self, p_insp, p_index, p_path=None):
			self._insp[p_index] = p_insp
			self._insp[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("insp")

		def insp_add_new(self, p_insp, p_index, p_path=None):
			if p_index not in self._insp:
				self.insp_add(p_insp, p_index, p_path)

		@property
		def insp(self):
			return self._insp

		def insp_indexes(self):
			return self._insp.keys()

		def lang_add(self, p_lang, p_index, p_path=None):
			self._lang[p_index] = p_lang
			self._lang[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_lang, p_index, p_path=None):
			if p_index not in self._lang:
				self.lang_add(p_lang, p_index, p_path)

		@property
		def lang(self):
			return self._lang

		def lang_indexes(self):
			return self._lang.keys()

	# Provider object
	class Pro(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.abmsuid = None
			self.birth_date = None
			self.birth_day = None
			self.birth_month = None
			self.birth_year = None
			self.clinical_interest = None
			self.degree_types = None
			self.display_name = None
			self.display_title = None
			self.ethnicity = None
			self.first_name = None
			self.full_name = None
			self.gender = None
			self.last_name = None
			self.master_id = None
			self.middle_name = None
			self.name_unique_in_impt = None
			self.nickname = None
			self.npi = None
			self.record_lock = None
			self.record_status = None
			self.standing_code = None
			self.status_code = None
			self.status_day = None
			self.status_month = None
			self.status_year = None
			self.suffix = None
			self.title = None
			self.type_ids = None

			# object-type members
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

		def alias_add(self, p_alias, p_index, p_path=None):
			self._alias[p_index] = p_alias
			self._alias[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("alias")

		def alias_add_new(self, p_alias, p_index, p_path=None):
			if p_index not in self._alias:
				self.alias_add(p_alias, p_index, p_path)

		@property
		def alias(self):
			return self._alias

		def alias_indexes(self):
			return self._alias.keys()

		def asn_add(self, p_asn, p_index, p_path=None):
			self._asn[p_index] = p_asn
			self._asn[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("asn")

		def asn_add_new(self, p_asn, p_index, p_path=None):
			if p_index not in self._asn:
				self.asn_add(p_asn, p_index, p_path)

		@property
		def asn(self):
			return self._asn

		def asn_indexes(self):
			return self._asn.keys()

		def awd_add(self, p_awd, p_index, p_path=None):
			self._awd[p_index] = p_awd
			self._awd[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("awd")

		def awd_add_new(self, p_awd, p_index, p_path=None):
			if p_index not in self._awd:
				self.awd_add(p_awd, p_index, p_path)

		@property
		def awd(self):
			return self._awd

		def awd_indexes(self):
			return self._awd.keys()

		def datum_add(self, p_datum, p_index, p_path=None):
			self._datum[p_index] = p_datum
			self._datum[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("datum")

		def datum_add_new(self, p_datum, p_index, p_path=None):
			if p_index not in self._datum:
				self.datum_add(p_datum, p_index, p_path)

		@property
		def datum(self):
			return self._datum

		def datum_indexes(self):
			return self._datum.keys()

		def degree_add(self, p_degree, p_index, p_path=None):
			self._degree[p_index] = p_degree
			self._degree[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("degree")

		def degree_add_new(self, p_degree, p_index, p_path=None):
			if p_index not in self._degree:
				self.degree_add(p_degree, p_index, p_path)

		@property
		def degree(self):
			return self._degree

		def degree_indexes(self):
			return self._degree.keys()

		def edu_add(self, p_edu, p_index, p_path=None):
			self._edu[p_index] = p_edu
			self._edu[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("edu")

		def edu_add_new(self, p_edu, p_index, p_path=None):
			if p_index not in self._edu:
				self.edu_add(p_edu, p_index, p_path)

		@property
		def edu(self):
			return self._edu

		def edu_indexes(self):
			return self._edu.keys()

		def extid_add(self, p_extid, p_index, p_path=None):
			self._extid[p_index] = p_extid
			self._extid[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("extid")

		def extid_add_new(self, p_extid, p_index, p_path=None):
			if p_index not in self._extid:
				self.extid_add(p_extid, p_index, p_path)

		@property
		def extid(self):
			return self._extid

		def extid_indexes(self):
			return self._extid.keys()

		def ident_add(self, p_ident, p_index, p_path=None):
			self._ident[p_index] = p_ident
			self._ident[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("ident")

		def ident_add_new(self, p_ident, p_index, p_path=None):
			if p_index not in self._ident:
				self.ident_add(p_ident, p_index, p_path)

		@property
		def ident(self):
			return self._ident

		def ident_indexes(self):
			return self._ident.keys()

		def insp_add(self, p_insp, p_index, p_path=None):
			self._insp[p_index] = p_insp
			self._insp[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("insp")

		def insp_add_new(self, p_insp, p_index, p_path=None):
			if p_index not in self._insp:
				self.insp_add(p_insp, p_index, p_path)

		@property
		def insp(self):
			return self._insp

		def insp_indexes(self):
			return self._insp.keys()

		def lang_add(self, p_lang, p_index, p_path=None):
			self._lang[p_index] = p_lang
			self._lang[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("lang")

		def lang_add_new(self, p_lang, p_index, p_path=None):
			if p_index not in self._lang:
				self.lang_add(p_lang, p_index, p_path)

		@property
		def lang(self):
			return self._lang

		def lang_indexes(self):
			return self._lang.keys()

		def lic_add(self, p_lic, p_index, p_path=None):
			self._lic[p_index] = p_lic
			self._lic[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("lic")

		def lic_add_new(self, p_lic, p_index, p_path=None):
			if p_index not in self._lic:
				self.lic_add(p_lic, p_index, p_path)

		@property
		def lic(self):
			return self._lic

		def lic_indexes(self):
			return self._lic.keys()

		def malp_add(self, p_malp, p_index, p_path=None):
			self._malp[p_index] = p_malp
			self._malp[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("malp")

		def malp_add_new(self, p_malp, p_index, p_path=None):
			if p_index not in self._malp:
				self.malp_add(p_malp, p_index, p_path)

		@property
		def malp(self):
			return self._malp

		def malp_indexes(self):
			return self._malp.keys()

		def mda_add(self, p_mda, p_index, p_path=None):
			self._mda[p_index] = p_mda
			self._mda[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("mda")

		def mda_add_new(self, p_mda, p_index, p_path=None):
			if p_index not in self._mda:
				self.mda_add(p_mda, p_index, p_path)

		@property
		def mda(self):
			return self._mda

		def mda_indexes(self):
			return self._mda.keys()

		def pos_add(self, p_pos, p_index, p_path=None):
			self._pos[p_index] = p_pos
			self._pos[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("pos")

		def pos_add_new(self, p_pos, p_index, p_path=None):
			if p_index not in self._pos:
				self.pos_add(p_pos, p_index, p_path)

		@property
		def pos(self):
			return self._pos

		def pos_indexes(self):
			return self._pos.keys()

		def pra_add(self, p_pra, p_index, p_path=None):
			self._pra[p_index] = p_pra
			self._pra[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("pra")

		def pra_add_new(self, p_pra, p_index, p_path=None):
			if p_index not in self._pra:
				self.pra_add(p_pra, p_index, p_path)

		@property
		def pra(self):
			return self._pra

		def pra_indexes(self):
			return self._pra.keys()

		def prof_add(self, p_prof, p_index, p_path=None):
			self._prof[p_index] = p_prof
			self._prof[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("prof")

		def prof_add_new(self, p_prof, p_index, p_path=None):
			if p_index not in self._prof:
				self.prof_add(p_prof, p_index, p_path)

		@property
		def prof(self):
			return self._prof

		def prof_indexes(self):
			return self._prof.keys()

		def sanc_add(self, p_sanc, p_index, p_path=None):
			self._sanc[p_index] = p_sanc
			self._sanc[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("sanc")

		def sanc_add_new(self, p_sanc, p_index, p_path=None):
			if p_index not in self._sanc:
				self.sanc_add(p_sanc, p_index, p_path)

		@property
		def sanc(self):
			return self._sanc

		def sanc_indexes(self):
			return self._sanc.keys()

		def spe_add(self, p_spe, p_index, p_path=None):
			self._spe[p_index] = p_spe
			self._spe[p_index].meta = Itom.Meta(p_index, p_path)
			self.meta.active_objects_add_new("spe")

		def spe_add_new(self, p_spe, p_index, p_path=None):
			if p_index not in self._spe:
				self.spe_add(p_spe, p_index, p_path)

		@property
		def spe(self):
			return self._spe

		def spe_indexes(self):
			return self._spe.keys()

	# Profession object
	class Prof(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.code = None
			self.record_status = None

	# Referral object
	class Ref(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.desc = None
			self.name = None
			self.record_status = None
			self.type_code = None

	# Sanction object
	class Sanc(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.action = None
			self.action_type_code = None
			self.authority = None
			self.end_date = None
			self.info = None
			self.reason = None
			self.record_status = None
			self.start_date = None
			self.state_code = None
			self.term = None
			self.type_code = None

	# Field Specialty object
	class Spe(Itom):

		def __init__(self, p_index=None, p_path=None):
			Itom.__init__(self)

			# field-type members
			self.apndx = None
			self.desc = None
			self.field_specialty_id = None
			self.is_primary = None
			self.is_principal = None
			self.record_status = None
			self.self_rept_cert = None
			self.status_code = None

