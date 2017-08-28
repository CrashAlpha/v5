#!/usr/bin/env python
def echo(*args):
   print " ".join(map(str, args))

def is_empty(p_str):
   """
   Is a string empty?
   """
   return not bool(p_str and str(p_str).strip())