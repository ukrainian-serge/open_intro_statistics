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

p_30 = pd.read_csv("./stent30.csv", header=0)
p_365 = pd.read_csv("./stent365.csv", header=0)

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


##############################
### I THINK THIS DOES IT!! ###
import pandas as pd
import numpy as np

p_30 = pd.read_csv("./stent30.csv", header=0)
p_365 = pd.read_csv("./stent365.csv", header=0)


grouped_30 = p_30.groupby(['group', 'outcome']).agg('size').unstack()
grouped_365 = p_365.groupby(['group', 'outcome']).agg('size').unstack()

## column_titles = ['stroke', 'no event']
## grouped_30 = grouped_30[column_titles]
## grouped_365 = grouped_365[column_titles]

concatted = pd.concat([grouped_30, grouped_365], axis=1).sort_index(ascending=False)
## concatted.columns.names = [None, None]

## for multi index columns
columns = [('0-30_days', 'no_event'),('0-30_days', 'stroke'),('0-365_days', 'no_event'),('0-365_days', 'stroke')]
concatted.columns = pd.MultiIndex.from_tuples(columns)

###############################################
### ANOTHER ATTEMPT AND FORMING THE TABLE #####

p_30.pivot_table(index='group', columns='outcome', aggfunc=len)
p_365.pivot_table(index='group', columns='outcome', aggfunc=len)




oncatted['0-30_days']['stroke']['control'] ### GREAT WAY TO SELECT MULTIINDEX STUFF
