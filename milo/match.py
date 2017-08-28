import datetime
import sys
import getopt
from impt import * 
from base import *
from db import *
from core import *

#  Process an impt facil record
def process_facil_rec(p_facil):
   name = p_facil.name
   addr = p_facil.addr.line1
   city = p_facil.city
   state = p_facil.state
   post = p_facil.zip
   cntry = p_facil.country
   acro = Db.select_value("mdx_lib.lex_acronym(%s)", (name,))
   impt = p_facil.document
   impt_table = impt.meta.table
   if cntry is None:
      cntry = "US"
   core = Core()
   facility = core.Facility(p_facil)
   target = facility.new_target()
   target.name = name
   target.address = addr
   target.city = city
   target.state_code = state
   target.postal_code = post
   target.country = cntry
   if target.match():
      echo("Facility m=%s s=%s n=%s f=%s fa=%s"
           % (target.result.method, target.result.score,
              name, target.result.facility_id,
              target.result.facility_address_id))
   else:
      echo("Facility NOT found")
   
   return

#  Utility to emulate the dynamic processing of
#  the members of an iTOM document. This procedure
#  reads the active members and prints the member
#  object paths and the member field names and values,
#  then recurses into each member object in turn
#  until the entire document tree is read.
def process_obj(p_obj, p_depth=0):
   depth = p_depth
   indent = ("|  " * depth)   
   
   if p_depth == 0:
      indent = ""
   else:
      p_obj.echo(indent)
      indent = ("|  " * (depth - 1)) + "+--"

   p_obj.echo("%s%s" % (indent, p_obj.meta.path.text))

   depth += 1
   indent = ("|  " * (depth - 1)) + "+--"
   p_obj.echo("%scontext: %s" % (indent, p_obj.meta.context))   

   if p_obj.meta.core is not None:
      p_obj.echo("%score.context: %s" % (indent, p_obj.meta.core.meta.context))
      p_obj.echo("%score.class_code: %s" % (indent, p_obj.meta.core.meta.class_code))   
   else:
      p_obj.echo("%score: N/A" % (indent))
      
   # Display member fields
   active_fields = p_obj.meta.active_fields   
   for member_name in active_fields:
      val = p_obj.get_member(member_name)
      p_obj.echo("%s%s: %s" % (indent, member_name, val))

   if p_obj.meta.name == "facil":
      process_facil_rec(p_obj)

   # Display member objects, dive into each member's indexed record then
   # process it as an object, causing recursion until all member objects
   # are traversed
   active_objects = p_obj.meta.active_objects
   for member_name in active_objects:
      member_obj = p_obj.get_active_object(member_name)
      indexes = member_obj.keys()

      for idx in indexes:
         next_obj = member_obj[idx]
         process_obj(next_obj, depth)

   # Zero depth means we are finished recursion, back at the root and done
   if p_depth == 0:
      p_obj.echo("")

   return

#   ____________________________________________________________________________
#   ____________________________________________________________________________
#
#   M A I N
#   ____________________________________________________________________________
#   ____________________________________________________________________________
def main(argv):

   # Command line arguments as parameters program parameter
   p_host = ""
   p_db = ""
   p_impt_table = ""
   p_rows = ""
   p_offset = 0
   p_limit = None
   p_echo = False
   help_msg= '<app_name>.py -h <host> -d <db> -t <table> -o <offset> -l <limit> -e <echo>'
   try:
      opts, args = getopt.getopt(
            argv,"h:d:t:r:o:l:e:",
            ["host=","db=","table=","rows=","offset=","limit=","echo="])
   except getopt.GetoptError:
      echo(help_msg)
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--host"):
         p_host = arg
      elif opt in ("-d", "--db"):
         p_db = arg
      elif opt in ("-t", "--table"):
         p_impt_table = arg
      elif opt in ("-r", "--rows"):
         p_rows = arg
      elif opt in ("-o", "--offset"):
         p_offset = arg
      elif opt in ("-l", "--limit"):
         p_limit = arg
      elif opt in ("-e", "--echo"):
         if arg in ("1", "true", "on"):
            p_echo = True

   if p_host == "" or p_db == "" or p_impt_table == "":
      echo(help_msg)
      sys.exit(2)

   # Db connection to impt table
   conn_str = \
       "host='%s' dbname='%s' user='mdx' password='mdx'" \
       % (p_host, p_db)
   print("Connecting to database\n\t->%s" % (conn_str))
   Db.open(conn_str)
   print("Connected!\n")

   # Program metrics and feedback
   dt_start = datetime.datetime.now()
   Itom.echo_status = p_echo

   # Create and open the impt table as an iTOM document
   impt = Impt()
   impt.set_collapse_not_indexed(True)
   impt.open(p_impt_table)

   echo("")
   echo("Importing table %s" % p_impt_table)

   # Scroll through the impt table and display each
   # row with a visual representation of the iTOM document
   # tree by using object reflection to discover its
   # member_name objects and recurse into them, and when each
   # object terminates in a field, displays each field
   # and its values.
   if p_limit is not None:
      limit_expr = "LIMIT %s" % p_limit
   else:
      limit_expr = ""
      
   if p_rows <> "":
      scope_expr = "WHERE impt_id %s" % (Db.int_scope_expr(p_rows),)
   else:
      scope_expr = ""

   Db.sql("""
         SELECT *
         FROM %s %s        
         ORDER BY impt_id OFFSET %s %s"""
         %(impt.meta.table, scope_expr, p_offset, limit_expr))
   n_rows = 0
   for row in Db.select():
      n_rows += 1
      impt.read(row)
      echo("(%d) rows id=%d" % (n_rows, row['impt_id']))
      process_obj(impt)

   impt.close()
   echo("End %s" % (datetime.datetime.now() - dt_start))
   return

if __name__ == "__main__":
   main(sys.argv[1:])
