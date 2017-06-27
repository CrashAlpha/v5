"""
   Code examples to illustrate the iTOM Document concept and
   the support library prototypes.
   
   This script has several examples illustrating
   various iTOM object processing scenarios,
   with every example cycling through 2 rows
   of a sample impt table as sample data.
"""

from impt import * 
from base import *
from db import *

#  Process a provider via a pro object instance
#  Note that the object instance is passed,
#  not the collection, which would be a dictionary
#  of object instances, with the keys being
#  the impt section index
def process_pro(p_pro):
   echo("First name: %s" % p_pro.first_name)
   echo("Middle name: %s" % p_pro.middle_name)
   echo("Last name %s" % p_pro.last_name)
   echo("Suffix %s" % p_pro.last_name)

   # Iterate through every practice instance
   for i_pra, pra in p_pro.pra.iteritems():
      echo("pra index %s" % i_pra)
      process_pra(pra)
   
   return


#  Process a provider practice via a pra object instance
def process_pra(p_pra):

   # An example using a more explicit path with
   # indexes. The classic impt model only has
   # one facil per pra, so it defaults to index zero
   # but it may have NONE so we check for it
   if 0 in p_pra.facil_indexes():
      process_facil(p_pra.facil[0])

   # Iterate through every pra's ins plan instance
   for i_insp, insp in p_pra.insp.iteritems():
      echo(">>> insp index %s" % i_insp)
      process_insp(insp)
   
   return


#  Process a facility via a facil object instance
def process_facil(p_facil):   
   echo(">>> facil context: %s" % p_facil.meta_.context)

   # Special actions based on the context of the call
   if p_facil.meta_.context == "impt.facil":
      echo(">>> This must be a facility import!")
   elif p_facil.meta_.context == "impt.pro.pra.facil":
      echo(">>> This must be a provider import!")
   else:
      echo(">>> I have no idea what this is!!!")
      
   echo("Facility name: %s" % p_facil.name)

   # This could raise an error,
   # we are assuming a facility address has been declared
   # but sometimes it isn't
   process_addr(p_facil.addr[0])
   
   echo("Facility city: %s" % p_facil.city)
   echo("Facility state: %s" % p_facil.state)
   echo("Facility zip: %s" % p_facil.zip)  

   return


#  Process an address (typically, facility addrress via an addr
#  object instance
def process_addr(p_addr):   
   echo(">>> addr context: %s" % p_addr.meta_.context)

   echo("Address line 1: %s" % p_addr.line1)
   echo("Address line 2: %s" % p_addr.line2)

   # Iterate through ins plan instances
   for i_insp, insp in p_addr.insp.iteritems():
      echo(">>> insp index %s" % i_insp)
      process_insp(insp)

   return


#  Process an ins plan provider practice via an insp object instance
def process_insp(p_insp):

   # Special actions based on the context of the call
   # but using relative contexts (i.e. we don't need
   # the absolute path) with pattern matching
   context = p_insp.meta_.context
   echo(">>> insp context: %s" % context)
   re_facil_addr = re.compile("^.*\.facil\.addr\.insp$")
   re_pra = re.compile("^.*\.pra\.insp$")

   if re_facil_addr.match(context):
      echo(">>> Ins Plan for facility address!")
   elif re_pra.match(context):
      echo(">>> Ins Plan for a practice!")
   else:
      echo(">>> Where did this Ins Plan come from???")

   echo("Ins plan id: %s" % p_insp.ins_plan_id)   
   return


#  ____________________________________________________________________________
#  ____________________________________________________________________________
#
#  M A I N
#  ____________________________________________________________________________
#  ____________________________________________________________________________
def main(argv):

   # Db connection to impt tables
   conn_str = \
       "host='zeta.mdx.med' dbname='mdx_v5_lib_devel' user='mdx' password='mdx'"
   print("Connecting to database\n     ->%s" % (conn_str))
   Db.open(conn_str)
   print("Connected!\n")

   draw_line = ('-' * 60)

   #  ____________________________________________________________________________
   #  EXAMPLE #1: pro import with practice addresses
   #  Create and open the impt table as an iTOM document
   impt_table = "mdx_import.bcbsnc_20160303_pro_address"
   echo("")
   echo(draw_line)
   echo("EXAMPLE #1 %s" % impt_table)
   impt = Impt()
   impt.open(impt_table)
   echo("- import type is '%s'" % impt.meta_.type)
   echo(draw_line)

   # Note that we don't need to remember the impt table name any more,
   # it's now in the iTOM document as .meta_.table.
   Db.sql("SELECT * FROM %s LIMIT 2" % (impt.meta_.table))
   for row in Db.select():
      impt.read(row)
      path_obj1 = impt.path_obj("impt.pro[0].pra[1].facil[0].addr[0].line1")
      path_obj2 = impt.path_obj("impt.pro[0].pra[1].facil[0].addr[0]")
      path_obj3 = impt.path_obj("impt.pro[0].pra[1].facil[0].addr")
      path_obj4 = impt.path_obj("impt.pro[0].first_name")
      path_obj5 = impt.path_obj("impt.pro[0]")
      path_obj6 = impt.path_obj("impt.pro")      
      path_obj7 = impt.path_obj("impt.id")
      path_obj8 = impt.path_obj("impt")

      process_pro(impt.pro[0])
      echo("")

   impt.close()

   #  ____________________________________________________________________________
   #  EXAMPLE #2: pro import with pra insp
   impt_table = "mdx_import.bcbsnc_20160303_pro_eli"
   echo("")
   echo(draw_line)
   echo("EXAMPLE #2 %s" % impt_table)
   impt = Impt()
   impt.open(impt_table)
   echo("- import type is '%s'" % impt.meta_.type)
   echo(draw_line)
   
   Db.sql("SELECT * FROM %s LIMIT 2" % (impt.meta_.table))
   for row in Db.select():
      impt.read(row)
      process_pro(impt.pro[0])
      echo("")
   
   impt.close()

   #  EXAMPLE #3: facil import with address
   impt_table = "mdx_import.bcbsnc_20160303_facil_address"
   echo("")
   echo(draw_line)
   echo("EXAMPLE #3 %s" % impt_table)
   impt = Impt()
   impt.open(impt_table)
   echo("- import type is '%s'" % impt.meta_.type)
   echo(draw_line)
   
   Db.sql("SELECT * FROM %s LIMIT 2" % (impt.meta_.table))
   for row in Db.select():
      impt.read(row)
      process_facil(impt.facil[0])
      echo("")
   
   impt.close()

   #  EXAMPLE #4: facil import with insp
   impt_table = "mdx_import.bcbsnc_20160303_facil_eli"
   echo("")
   echo(draw_line)
   echo("EXAMPLE #4 %s" % impt_table)
   impt = Impt()
   impt.open(impt_table)
   echo("- import type is '%s'" % impt.meta_.type)
   echo(draw_line)
   
   Db.sql("SELECT * FROM %s LIMIT 2" % (impt.meta_.table))
   for row in Db.select():
      impt.read(row)
      process_facil(impt.facil[0])
      echo("")
   
   impt.close()

   #   ____________________________________________________________________________
   #  EXAMPLE #5: pro import with practice addresses
   #  but this time with explicit fulls paths into the iTOM document
   #  to illustrate the document hieararchy   
   impt_table = "mdx_import.bcbsnc_20160303_pro_address"
   echo("")
   echo(draw_line)
   echo("EXAMPLE #5 %s" % impt_table)
   impt = Impt()
   impt.open(impt_table)
   echo("- import type is '%s'" % impt.meta_.type)
   echo(draw_line)
   
   Db.sql("SELECT * FROM %s LIMIT 2" % (impt.meta_.table))
   for row in Db.select():
      impt.read(row)
      # Note, we know the impt columns exist
      # so it's safe to hard-code the iTOM objects and
      # indexes here
      echo("impt.status:", impt.status)
      echo("impt.date:", impt.date)
      echo("impt.fail_msg:", impt.fail_msg)
      # identifier failed in the iTOM open, check self.open_fail_messages
      # for the error. The identifier section was hastily designed
      # and has been replaced by a new ident impt section for M5
      # along with a corresponding iTOM ident class.
      # echo("impt.pro[0].identifier:", impt.pro[0].identifier)
      echo("impt.pro[0].npi:", impt.pro[0].npi)
      echo("impt.pro[0].record_status:", impt.pro[0].record_status)
      echo("impt.pro[0].display_name:", impt.pro[0].display_name)
      echo("impt.pro[0].suffix:", impt.pro[0].suffix)
      echo("impt.pro[0].last_name:", impt.pro[0].last_name)
      echo("impt.pro[0].first_name:", impt.pro[0].first_name)
      echo("impt.pro[0].middle_name:", impt.pro[0].middle_name)
      echo("impt.pro[0].title:", impt.pro[0].title)
      echo("impt.pro[0].degree_types:", impt.pro[0].degree_types)      
      # Having trouble with this syntax with the parser as
      # prof is also an object, so this should have been
      # rejected. The stored proc parsing the impt table needs to be fixed
      # echo("impt.pro[0].lic[0].prof:", impt.pro[0].lic[0].prof)      
      # echo("impt.pro[0].prof[0].code:", prof[0].code)
      echo("impt.pro[0].type_ids:", impt.pro[0].type_ids)
      echo("impt.pro[0].gender:", impt.pro[0].gender)
      # echo("impt.pro[0].pra[1].identifier:", impt.pro[0].pra[1].identifier)
      echo("impt.pro[0].pra[1].facil[0].name:", impt.pro[0].pra[1].facil[0].name)
      echo("impt.pro[0].pra[1].facil[0].addr[0].name:", impt.pro[0].pra[1].facil[0].addr[0].name)
      echo("impt.pro[0].pra[1].facil[0].addr[0].line1:", impt.pro[0].pra[1].facil[0].addr[0].line1)
      echo("impt.pro[0].pra[1].facil[0].city:", impt.pro[0].pra[1].facil[0].city)
      echo("impt.pro[0].pra[1].facil[0].state:", impt.pro[0].pra[1].facil[0].state)
      echo("impt.pro[0].pra[1].facil[0].zip:", impt.pro[0].pra[1].facil[0].zip)
      echo("impt.pro[0].pra[1].record_status:", impt.pro[0].pra[1].record_status)
      echo("impt.pro[0].pra[1].facil[0].record_status:", impt.pro[0].pra[1].facil[0].record_status)
      echo("impt.pro[0].pra[1].facil[0].addr[0].is_primary", impt.pro[0].pra[1].facil[0].addr[0].is_primary)
      echo("impt.pro[0].pra[1].facil[0].addr[0].phone[1].type_code:", impt.pro[0].pra[1].facil[0].addr[0].phone[1].type_code)
      echo("impt.pro[0].pra[1].facil[0].addr[0].phone[1].number:", impt.pro[0].pra[1].facil[0].addr[0].phone[1].number)
      echo("impt.pro[0].pra[1].facil[0].addr[0].phone[1].is_primary:", impt.pro[0].pra[1].facil[0].addr[0].phone[1].is_primary)
      echo("impt.pro[0].pra[1].facil[0].addr[0].phone[1].record_status:", impt.pro[0].pra[1].facil[0].addr[0].phone[1].record_status)
      echo("impt.pro[0].pra[1].facil[0].addr[0].phone[2].type_code:", impt.pro[0].pra[1].facil[0].addr[0].phone[2].type_code)
      echo("impt.pro[0].pra[1].facil[0].addr[0].phone[2].number:", impt.pro[0].pra[1].facil[0].addr[0].phone[2].number)
      echo("impt.pro[0].pra[1].facil[0].addr[0].phone[2].record_status:", impt.pro[0].pra[1].facil[0].addr[0].phone[2].record_status)
      echo("")

   impt.close()
   
   #  EXAMPLE #6: pro import with practice addresses
   #  but this time with explicit fulls paths using collapsed indexes,
   #  to illustrate the document hieararchy. Note that impt sections
   #  which do not normally have indexes must have [0] as an index.
   #  by using set_collapse_not_indexed(true) we can remove that
   #  requirement and use V4-like syntax
   impt_table = "mdx_import.bcbsnc_20160303_pro_address"
   echo("")
   echo(draw_line)
   echo("EXAMPLE #6 %s" % impt_table)
   impt = Impt()
   impt.set_collapse_not_indexed(True)
   impt.open(impt_table)
   echo("- import type is '%s'" % impt.meta_.type)
   echo(draw_line)
   
   Db.sql("SELECT * FROM %s LIMIT 2" % (impt.meta_.table))
   for row in Db.select():
      impt.read(row)
      echo("impt.status:", impt.status)
      echo("impt.date:", impt.date)
      echo("impt.fail_msg:", impt.fail_msg)
      echo("impt.pro.npi:", impt.pro.npi)
      echo("impt.pro.record_status:", impt.pro.record_status)
      echo("impt.pro.display_name:", impt.pro.display_name)
      echo("impt.pro.suffix:", impt.pro.suffix)
      echo("impt.pro.last_name:", impt.pro.last_name)
      echo("impt.pro.first_name:", impt.pro.first_name)
      echo("impt.pro.middle_name:", impt.pro.middle_name)
      echo("impt.pro.title:", impt.pro.title)
      echo("impt.pro.degree_types:", impt.pro.degree_types)
      # echo("impt.pro.lic.prof:", impt.pro.lic.prof)     
      # echo("impt.pro.prof.code:", prof.code)
      echo("impt.pro.type_ids:", impt.pro.type_ids)
      echo("impt.pro.gender:", impt.pro.gender)      
      # echo("impt.pro.pra[1].identifier:", impt.pro.pra[1].identifier)
      echo("impt.pro.pra[1].facil.name:", impt.pro.pra[1].facil.name)
      echo("impt.pro.pra[1].facil.addr.name:", impt.pro.pra[1].facil.addr.name)
      echo("impt.pro.pra[1].facil.addr.line1:", impt.pro.pra[1].facil.addr.line1)
      echo("impt.pro.pra[1].facil.city:", impt.pro.pra[1].facil.city)
      echo("impt.pro.pra[1].facil.state:", impt.pro.pra[1].facil.state)
      echo("impt.pro.pra[1].facil.zip:", impt.pro.pra[1].facil.zip)
      echo("impt.pro.pra[1].record_status:", impt.pro.pra[1].record_status)
      echo("impt.pro.pra[1].facil.record_status:", impt.pro.pra[1].facil.record_status)
      echo("impt.pro.pra[1].facil.addr.is_primary", impt.pro.pra[1].facil.addr.is_primary)
      echo("impt.pro.pra[1].facil.addr.phone[1].type_code:", impt.pro.pra[1].facil.addr.phone[1].type_code)
      echo("impt.pro.pra[1].facil.addr.phone[1].number:", impt.pro.pra[1].facil.addr.phone[1].number)
      echo("impt.pro.pra[1].facil.addr.phone[1].is_primary:", impt.pro.pra[1].facil.addr.phone[1].is_primary)
      echo("impt.pro.pra[1].facil.addr.phone[1].record_status:", impt.pro.pra[1].facil.addr.phone[1].record_status)
      echo("impt.pro.pra[1].facil.addr.phone[2].type_code:", impt.pro.pra[1].facil.addr.phone[2].type_code)
      echo("impt.pro.pra[1].facil.addr.phone[2].number:", impt.pro.pra[1].facil.addr.phone[2].number)
      echo("impt.pro.pra[1].facil.addr.phone[2].record_status:", impt.pro.pra[1].facil.addr.phone[2].record_status)
      echo("")

   impt.close()

   #  EXAMPLE #7: facil import with addresses
   #  using explicit fulls and collapsed indexes
   impt_table = "mdx_import.bcbsnc_20160303_facil_address"
   echo("")
   echo(draw_line)
   echo("EXAMPLE #7 %s" % impt_table)
   impt = Impt()
   impt.set_collapse_not_indexed(True)
   impt.open(impt_table)
   echo("- import type is '%s'" % impt.meta_.type)
   echo(draw_line)
   
   Db.sql("SELECT * FROM %s LIMIT 2" % (impt.meta_.table))
   for row in Db.select():
      impt.read(row)
      echo("impt.id:", impt.id)
      echo("impt.status:", impt.status)
      echo("impt.date:", impt.date)
      echo("impt.fail_msg:", impt.fail_msg)
      # echo("impt.facil.identifier:", impt.facil.identifier)
      echo("impt.facil.master_id:", impt.facil.master_id)
      echo("impt.facil.addr.identifier:", impt.facil.addr.identifier)
      echo("impt.facil.type_code:", impt.facil.type_code)
      echo("impt.facil.record_status:", impt.facil.record_status)
      echo("impt.facil.name:", impt.facil.name)
      echo("impt.facil.addr.line1:", impt.facil.addr.line1)
      echo("impt.facil.city:", impt.facil.city)
      echo("impt.facil.state:", impt.facil.state)
      echo("impt.facil.zip:", impt.facil.zip)
      echo("impt.facil.addr.is_primary:", impt.facil.addr.is_primary)
      echo("impt.facil.addr.phone[1].type_code:", impt.facil.addr.phone[1].type_code)
      echo("impt.facil.addr.phone[1].number:", impt.facil.addr.phone[1].number)
      echo("impt.facil.addr.phone[1].is_primary:", impt.facil.addr.phone[1].is_primary)
      echo("impt.facil.addr.phone[1].record_status:", impt.facil.addr.phone[1].record_status)
      echo("impt.facil.addr.phone[2].type_code:", impt.facil.addr.phone[2].type_code)
      echo("impt.facil.addr.phone[2].number:", impt.facil.addr.phone[2].number)
      echo("impt.facil.addr.phone[2].record_status:", impt.facil.addr.phone[2].record_status)
      echo("")

   impt.close()

   echo("End")
   return


if __name__ == "__main__":
   main(sys.argv[1:])
