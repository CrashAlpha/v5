import datetime
import sys
import getopt
from impt import * 
from base import *
from db import *

#  Utility to emulate the dynamic processing of
#  the members of an iTOM document. This procedure
#  reads the active members and prints the member
#  object paths and the member field names and values,
#  then recurses into each member object in turn
#  until the entire document tree is read.
def process_obj(p_obj, p_depth=0):
   depth = p_depth
   indent = ("|  " * depth)   
   
   if (p_depth == 0):
      indent = ""
   else:
      p_obj.echo(indent)
      indent = ("|  " * (depth - 1)) + "+--"

   p_obj.echo("%s%s" % (indent, p_obj.meta_.path.text))   

   depth += 1
   indent = ("|  " * (depth - 1)) + "+--"
   p_obj.echo("%scontext: %s" % (indent, p_obj.meta_.context))   

   if p_obj.meta_.core is not None:
      p_obj.echo("%score.context: %s" % (indent, p_obj.meta_.core.meta_.context))
      p_obj.echo("%score.class_code: %s" % (indent, p_obj.meta_.core.meta_.class_code))   
   else:
      p_obj.echo("%score: N/A" % (indent))
      
   # Display member fields
   active_fields = p_obj.meta_.active_fields   
   for member_name in active_fields:
      #val = p_obj.__dict__["_" + member_name]
      val = p_obj.get_member(member_name)
      p_obj.echo("%s%s: %s" % (indent, member_name, val))

   # Display member objects, dive into each member's indexed instance then
   # process it as an object, causing recursion until all member objects
   # are traversed
   active_objects = p_obj.meta_.active_objects
   for member_name in active_objects:
      member_obj = p_obj.get_active_object(member_name)
      indexes = member_obj.keys()

      for idx in indexes:
         next_obj = member_obj[idx]
         process_obj(next_obj, depth)

   # Zero depth means we are finished recursion, back at the root and done
   if (p_depth == 0):
      p_obj.echo("")

   return

#   ____________________________________________________________________________
#   ____________________________________________________________________________
#
#   M A I N
#   ____________________________________________________________________________
#   ____________________________________________________________________________
def main(argv):

   # Command line arguments as parameters program parameters
   p_impt_table = ""
   p_limit = 10
   p_echo = True
   help_msg= '<app_name>.py -t <table> -l <limit> -e <echo>'
   try:
      opts, args = getopt.getopt(argv,"t:l:e:",["table=","limit=","echo="])
   except getopt.GetoptError:
      echo(help_msg)
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-t", "--table"):
         p_impt_table = arg
      elif opt in ("-l", "--limit"):
         p_limit = arg
      elif opt in ("-e", "--echo"):
         if arg in ("0", "false", "off"):
            p_echo = False

   if p_impt_table == "":
      echo(help_msg)
      sys.exit(2)

   # Db connection to impt table
   conn_str = \
       "host='zeta.mdx.med' dbname='mdx_v5_lib_devel' user='mdx' password='mdx'"
   print("Connecting to database\n     ->%s" % (conn_str))
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
   Db.sql("SELECT * FROM %s LIMIT %s" % (impt.meta_.table, p_limit))
   n_rows = 0
   for row in Db.select():
      n_rows += 1
      impt.read(row)
      echo("(%d) rows id=%d" % (n_rows, row['impt_id']))

      if n_rows == 1:
         echo("--> setting ad-hoc fields")
         impt.pro.full_name = "XXXXX"
         if impt.pro.has("mda"):
            impt.pro.mda[0].dest_url = "YYYYY"
         else:
            impt.pro.mda_add_new(impt.Mda(), 0)
            impt.pro.mda.dest_url = "ZZZZZ"
         
      echo("impt.id=%s impt.pro.full_name=%s, mda.dest_url=%s" % (impt.id, impt.pro.full_name, impt.pro.mda.dest_url))
      process_obj(impt)

   impt.close()
   echo("End %s" % (datetime.datetime.now() - dt_start))
   return

if __name__ == "__main__":
   main(sys.argv[1:])
