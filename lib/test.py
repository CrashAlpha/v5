class Test(object):
   def __init__(self):
      self._v = [1, 2, 3, 4]
   
   @property
   def v(self, i=None):
      print i
      if i is None:
         return self._v
      else:
         return self.v[i]
   
     
if __name__ == "__main__":
   t = Test()
   print t.v[1]