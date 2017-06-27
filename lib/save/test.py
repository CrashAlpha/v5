from impt import * 
from base import *
from db import *

def process_obj(p_obj, depth=0):
   name = p_obj.meta.name
   indent = ("|  " * depth)
   echo("%s(Path: %s" % (indent, p_obj.meta.path))
   echo("%s(Processing: %s)" % (indent, name))
   depth += 1
   indent = ("|  " * depth)   
   active_fields = p_obj.meta.active_fields
   active_objects = p_obj.meta.active_objects

   echo("%s(Active fields=%s)" % (indent, active_fields))

   for member in active_fields:
      exec_str = "val = p_obj.%s" % member
      exec exec_str      
      echo("%s%s: %s" % (indent, member, val))

   echo("%s(Active objects=%s)" % (indent, active_objects))

   for member in active_objects:
      echo("%s(active member obj=%s)" % (indent, member))
      exec_str = "indexes = p_obj.%s_indexes()" % (member)
      exec exec_str
      echo("%s(Indexes: %s)" % (indent, indexes))
      for idx in indexes:
         exec_str = "next_obj = p_obj.%s[%i]" % (member, idx)
         exec exec_str
         process_obj(next_obj, depth)
   
#   ____________________________________________________________________________
#   ____________________________________________________________________________
#
#   M A I N
#   ____________________________________________________________________________
#   ____________________________________________________________________________
def main(p_impt_table, p_base_obj = "impt"):

   conn_str = \
       "host='zeta.mdx.med' dbname='mdx_m5_devel' user='mdx' password='mdx'"
   print("Connecting to database\n     ->%s" % (conn_str))
   Db.open(conn_str)
   print("Connected!\n")

   echo("\nImport table...")
   Db.sql("""
          SELECT * FROM mdx_lib.impt_table_parse_elements(%(imptTable)s)
          ORDER BY ordinal_position, element_ordinal_position""",
         {"imptTable": p_impt_table}
   )

   impt = Impt(0, p_base_obj)
   load_map = {}
   skip_row = False
   is_error = False

   for row in Db.select():
      # echo(row['column_name'], row['element_code'], row['element_index'])

      # First element? New path off of base
      if row['element_ordinal_position'] == 1:
         # Release persistent skip
         skip_row = False
         prv_path = p_base_obj

      # Element should skip? Configure from reason
      if not row['is_valid'] or row['element_code'] == "extra":
         # Skip persists until this path is done
         skip_row = True

         if not row['is_valid']:
            is_error = True
            msg = "Failing"
         else:
            msg = "Ignoring"
            
      
      if skip_row:
         echo("%s %s for %s" % (msg, row['column_name'], row['element_code']))
         continue

      if row['element_type_code'] == "object":

         if row['element_code'] <> "impt":
            obj = row['element_code']
            inst = "Impt.%s()" % row['element_code'].capitalize()
            idx = row['element_index']
            path = prv_path + ".%s[%d]" % (obj, idx)
            add_obj = '%s_add_new(%s, %d, "%s")' % (obj, inst, idx, path)
            exec_str = "%s.%s" % (prv_path, add_obj)
            prv_path = path

            # echo(exec_str)
            exec exec_str
      else:
         load_map[row['column_name']] = "%s.%s" % (prv_path, row['element_code'])
         exec_str = '%s.meta.active_fields_add_new("%s")' % (prv_path, row['element_code'])
         exec exec_str

   exec_load_impt = ""
   for col, path in load_map.iteritems():
      exec_load_impt += "%s = row['%s']\r\n" % (path, col)
      
   Db.sql("SELECT * FROM %s LIMIT 5" % p_impt_table)   
   for row in Db.select():
      exec exec_load_impt
      echo("\nImport row: %d" % row['impt_id'])
      process_obj(impt)

      #for obj in impt.meta.active_objects:
      #   echo("Active object:%s" % obj)
         
      #echo("impt_id=%d: %s, %s %s at %s %s %s %s %s"
      #      % (row['impt_id'],
      #         impt.pro[0].last_name,
      #         impt.pro[0].middle_name, impt.pro[0].first_name,
      #         impt.pro[0].pra[1].facil[0].name,
      #         impt.pro[0].pra[1].facil[0].addr[0].line1,
      #         impt.pro[0].pra[1].facil[0].city,
      #         impt.pro[0].pra[1].facil[0].state,
      #         impt.pro[0].pra[1].facil[0].zip))

   echo("End")

if __name__ == "__main__":
   main("mdx_import.bcbsnc_20160303_pro_address")
