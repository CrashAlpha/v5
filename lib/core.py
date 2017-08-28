#!/usr/bin/env python
from base import *
from db import *

class CoreRecord(object):
   """
   Attributes common  to all core record classes
   """
   def __init__(self, p_impt_rec):
      self.impt_record = p_impt_rec
      self.meta = self.impt_record.meta.core.meta
      self.id = None

class CoreTarget(object):
   """
   Attributes common  to all core record targets
   A Target is a a core object which contains the properties
   and methods required to find one or more rows in a core table,
   and if found, one or more result objects with row id and other data
   from the target rows found.
   """

   def __init__(self, p_core_record):
      self.core_record = p_core_record
      self.impt_record = p_core_record.impt_record
      self.found = False


class Core(object):
   """
   Class that handles targeting, reading from and writing to a MILO
   warehouse's core schema objects.
   """

   
   class Address(CoreRecord):
      """
      Locale specifics of a facility address
      """

      def __init__(self, p_impt_rec, p_address=None, p_city=None,
                   p_state=None, p_postal_code=None, p_country="US"):
         """Address constructor"""
         CoreRecord.__init__(self, p_impt_rec)
         self.address_id
         self.location_id
         self.location_unit_id
         self.address = p_address
         self.line1 = None
         self.line2 = None
         self.city = p_city
         self.state_code = p_state
         self.postal_code = p_postal_code
         self.country_code = p_country
         self.county = None
         self.unit = None
         self.address_display = p_address
         self.city_display = p_address
         if not p_postal_code is None:
            self.zip_base = p_postal_code[0:5]
         #self.zip_plus4 = p_postal_code[-3]
         #self.zip = "%s-%s" % (zip_base, zip_plus4)


   class Parsed(CoreRecord):
      """
      Parsed locale details of a facility address
      """

      def __init(self):
         self.street_number = None
         self.street_pre_direction = None
         self.street_name = None
         self.street_suffix = None
         self.street_post_direction = None
         self.unit_name = None
         self.unit_range = None
         self.unit = ("%s %s" % (unit_name, unit_range)).strip()


   class Facility(CoreRecord):
      """
      Facility where practices and institutions may be found
      """

      def __init__(self, p_impt_rec):
         """ Facility constructor"""
         CoreRecord.__init__(self, p_impt_rec)
         pass
         # self.impt_record = p_impt_rec
         # self.meta = self.impt_record.meta.core.meta

      class Target(CoreTarget):
         """
         Container for facility Target terms and results
         """

         def __init__(self, p_facility):
            CoreTarget.__init__(self, p_facility)
            # self.facility = p_facility
            self.address = None
            self.city = None
            self.state_code = None
            self.postal_code = None
            self.zip_base = None
            #self.zip_plus4 = None
            #self.zip = None
            self.country_code = "US"
            # self.found = False
            self.exclude = None
            self.result = None
            self.results = []

         class Result(object):
            """
            Container for a single facility Target result
            """

            def __init__(self):
               self.name = None
               self.facility_id = None
               self.facility_address_id = None
               self.provider_practice_id = None;
               self.id = None
               self.method = None
               self.distance = None
               self.score = None
               self.via_identity = False

         class Exclude(object):
            """
            Define what should be excluded from a facility Target
            """

            def __init__(self):
               self.facility_ids = []

            #def add_facility_id(self, p_facility_id):
            #   self.facility_ids.add(p_facility_id)


         def match(self):
            """
            Get the top ranking facility Target result
            """
            
            core_facility = self.core_record
            impt_facil = self.impt_record
            self.result = self.Result()
            self.result.found = False
            
            #
            # Identity value targeting
            #
            
            # Facility-related Identifier targeting
            for ident in impt_facil.idents():
               identifier = Core().Identifier(ident)
               target = identifier.new_target()
               target.also_return = "facility_id"

               if target.match():
                  self.found = True
                  self.found = True
                  self.result.name = None
                  self.result.facility_id = target.return_values["facility_id"]
                  self.result.facility_address_id = None
                  self.result.provider_practice_id = None;
                  self.result.method = "identity.facility.identifier"
                  self.result.distance = None
                  self.result.score = None
                  self.result.via_identity = True

            #
            # Facility name and location geo-targeting
            #
            if not self.found:
   
               if not self.postal_code is None:
                  self.zip_base = self.postal_code[0:5]
   
               Db.sql("""
                     SELECT *
                     FROM mdx_lib.core_facility_name_geo_match(
                           %s::text,
                           %s::text,
                           %s::text,
                           %s::text,
                           %s::text,
                           %s::text
                     )""",
                     (self.name, self.address, self.city, self.state_code,
                      self.zip_base, self.country_code)
               )
   
               row = Db.select_top()
               if not row['facility_id'] == None:
                  self.found = True
                  self.result.name = None
                  self.result.facility_id = row['facility_id']
                  self.result.facility_address_id = row['facility_address_id']
                  self.result.provider_practice_id = None;
                  self.result.method = row['method']
                  self.result.distance = row['distance']
                  self.result.score = row['score']
                  self.result.via_identity = False

            if self.found:
               self.id = self.result.facility_id
               self.results.append(self.result)

               if is_empty(self.result.name):
                  self.result.name = Db.select_value("""
                        SELECT name
                        FROM mdx_core.facility
                        WHERE facility_id = %s""",
                        (self.result.facility_id,))

            return self.found

      def new_target(self):
         """
         New Target() instantiation with the CoreRecord instance passed to
         the new CoreTarget instance as Python doesn't support nested classes
         accessing the outer class
         """
         return self.Target(self)


   class Identifier(CoreRecord):
      """
      Identity values to locate entities, locations and insurance plans
      """

      def __init__(self, p_impt_rec):
         """ Identifier constructor"""
         CoreRecord.__init__(self, p_impt_rec)
         self.identifier_id = None
         self.identifier_type_id = None
         self.value = None

      def get_ident_type_id(self):
         """
         Get the impt ident type_id, if not declared, get the default from the
         impt document loaded at ItomDoc.open() from input source.
         """
         impt_rec = self.impt_record
         result = impt_rec.type_id
         if is_empty(result):
            result = impt_rec.document.meta.ident_type_id
            
         if is_empty(result):
            raise ValueError("Could not determine identifier_type_id for %s"
                             % (impt_rec.meta.path.text))

         return result
         
      def new_target(self):
         """
         New Target() instantiation with the CoreRecord instance passed to
         the new CoreTarget instance as Python doesn't support nested classes
         accessing the outer class
         """
         return self.Target(self)

      class Target(CoreTarget):
         """
         Container for identifier Target terms and results
         """

         def __init__(self, p_identifier):
            CoreTarget.__init__(self, p_identifier)
            # self.identifier = p_identifier
            # self.found = False
            self.also_return = []
            self.return_values = {}
            self.exclude = None
            self.result = None
            self.results = []

         def match(self):
            """
            Get the top ranking identifier Target result
            """
            impt_ident = self.impt_record
            core_identifier = self.core_record

            # Make sure "also return" columns are a list
            if self.also_return is None:
               self.also_return = {}
            elif type(self.also_return) is not list:
               self.also_return = [self.also_return]

            pkey_col = core_identifier.meta.pkey_column_name
            columns = self.also_return[:]
            columns.append(pkey_col)

            self.found = False
            self.result = self.Result()
            self.results = []

            # Find the identifier primary key value
            # and any other columns we have requested
            # in this search
            ident_type_id = core_identifier.get_ident_type_id()
            table_name = core_identifier.meta.table_name
            row = Db.select_top("""
                  SELECT """ + ",".join(columns) + """
                  FROM mdx_core.""" + table_name + """
                  WHERE
                     identifier_type_id = %s
                     AND value = %s
                  LIMIT 1
                  """,
                  (ident_type_id, impt_ident.value))
            if row is not None:
               core_identifier.id = row[pkey_col]
               self.found = True
               self.result.id = core_identifier.id
               self.result.found = True
               self.results.append(self.result)
               
            for col in columns:
               if self.found:
                  val = row[col]
               else:
                  val = None
               self.return_values[col] = val

            return self.found


         class Result(object):
            """
            Container for a single identifier Target result
            """

            def __init__(self):
               self.id = None

         class Exclude(object):
            """
            Define what should be excluded from an identifier Target
            """

            def __init__(self):
               pass

