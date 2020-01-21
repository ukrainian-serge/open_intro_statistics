### SOME FUNCS
def get_funcs(thing):
  """
  Prints available functions
  """
     for i in dir(thing):
         if not i.startswith('_'):
             print(i)


### Chapter 1: introduction to data

### combine data to make like in the book
import pandas as pd

p_30 = pd.read_csv("./open_intro_data/stent30.csv", header=0)
p_365 = pd.read_csv("./open_intro_data/stent365.csv", header=0)

df = pd.merge(p_30, p_365, left_index=True, right_index=True)
df.index = pd.RangeIndex(start=1, stop=452)
###

### trying
df.pivot_table(index='group',columns=['0-30_days', '0-365_days'], aggfunc=len)
###

## still goofy looking
df.groupby('group').agg({'0-30_days': 'value_counts','0-365_days':'value_counts'})
###

## tried this but its goofy
pd.crosstab(df.group,[df['0-30_days'], df['0-365_days']])
###


## ALMOST THERE Pregrouped them individually
grouped_30 = p_30.groupby(['group', '0-30_days']).agg('size').unstack()
grouped_365 = p_365.groupby(['group', '0-365_days']).agg('size').unstack()

grouped_30.merge(grouped_365, left_index=True, right_index=True, suffixes=('_30_days','_365_days'))
###


###################################################
###################################################
### ONE WAY OF FORMING THE TABLE ##################
###################################################

import pandas as pd, numpy as np

p_30 = pd.read_csv("./stent30.csv", header=0)
p_365 = pd.read_csv("./stent365.csv", header=0)


grouped_30 = p_30.groupby(['group', 'outcome']).agg('size').unstack()
grouped_365 = p_365.groupby(['group', 'outcome']).agg('size').unstack()

concatted = pd.concat([grouped_30, grouped_365], axis=1).sort_index(ascending=False)
## concatted.columns.names = [None, None]

## for multi index columns
columns = [('0-30_days', 'no_event'),('0-30_days', 'stroke'),('0-365_days', 'no_event'),('0-365_days', 'stroke')]
concatted.columns = pd.MultiIndex.from_tuples(columns)

###################################################
###################################################
### ANOTHER, SIMPLER WAY OF FORMING THE TABLE #####
###################################################
## Transpose over, then transpose back

import pandas as pd, numpy as np


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

### GREAT WAY TO SELECT MULTIINDEX STUFF ######
###############################################

##            0-30_days         0-365_days
##            no_event stroke   no_event stroke
## group
## treatment       191     33        179     45
## control         214     13        199     28



## concatted['30']['stroke']['control']
## >> 13
