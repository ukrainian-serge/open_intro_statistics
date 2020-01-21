### SOME FUNCS
def get_funcs(thing):
  """
  Prints available functions
  """
     for i in dir(thing):
         if not i.startswith('_'):
             print(i)


### Chapter 1: introduction to data
###################################################

### ONE WAY OF FORMING THE TABLE ##################
import pandas as pd, numpy as np

p_30 = pd.read_csv("./stent30.csv", header=0)
p_365 = pd.read_csv("./stent365.csv", header=0)

grouped_30 = p_30.groupby(['group', 'outcome']).agg('size').unstack()
grouped_365 = p_365.groupby(['group', 'outcome']).agg('size').unstack()

concatted = pd.concat([grouped_30, grouped_365], axis=1).sort_index(ascending=False)

columns = [('0-30_days', 'no_event'),('0-30_days', 'stroke'),('0-365_days', 'no_event'),('0-365_days', 'stroke')]
concatted.columns = pd.MultiIndex.from_tuples(columns)


### ANOTHER, SIMPLER WAY OF FORMING THE TABLE #####
## Transpose over, then transpose back .T

import pandas as pd

pieces = {
    '30':(pd.read_csv("./open_intro_data/stent30.csv")
            .pivot_table(index='group', 
            columns=['outcome'], 
            aggfunc=len)[::-1].T[::-1]),
            
    '365':(pd.read_csv("./open_intro_data/stent365.csv")
            .pivot_table(index='group', 
            columns=['outcome'], 
            aggfunc=len)[::-1].T[::-1])
    
} # [::-1] * 2 to exact replicate R table in the book

df = pd.concat(
    pieces, 
    names=['days', 'outcome'],
    ).T
df