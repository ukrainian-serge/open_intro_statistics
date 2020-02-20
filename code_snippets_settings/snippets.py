### SOME FUNCS
def get_funcs(thing):
  """
  Prints available functions
  """
     for i in dir(thing):
         if not i.startswith('_'):
             print(i)


