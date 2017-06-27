import re
class Itom(object):

   def __init__(self, p_index=None, p_path=None):
      if p_index is None and p_path is None:
         self.meta = None
      else:
         self.meta = Itom.Meta(p_index, p_path)

   class Meta(object):

      def __init__(self, p_index, p_path):
         self.index = p_index
         self.path = p_path
         self.context = re.sub(r"\[[0-9]\]", "", p_path)
         self.name = re.sub(r"(.*)\.(.*)", r"\2", self.context)
         self.active_objects = []
         self.active_fields = []
      
      def active_objects_add(self, p_member_code):
         self.active_objects.append(p_member_code)
         
      def active_objects_add_new(self, p_member_code):
         if p_member_code not in self.active_objects:
            self.active_objects_add(p_member_code)

      def active_fields_add(self, p_member_code):
         self.active_fields.append(p_member_code)
         
      def active_fields_add_new(self, p_member_code):
         if p_member_code not in self.active_fields:
            self.active_fields_add(p_member_code)

      def parent_path(self):
         return parent_path(self.path)
 
# Return the parent path of a path
def parent_path(p_path):
   return re.sub(r"(.*)\.(.*)", r"\1", p_path)