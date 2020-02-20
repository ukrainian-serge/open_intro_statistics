import matplotlib.pyplot as plt

### SOME FUNCS
def get_funcs(thing):
    """
    Prints available functions
    """
    for i in dir(thing):
        if not i.startswith('_'):
            print(i)

# def outliers_df(df, x, y, upper_q=0.0, lower_q=1):
#     return df[(df[x] > df[x].quantile(upper_q) &
#                 df[y] < df[y].quantile(lower_q))]



def plot_ouliers_annotate(df, x, y, alpha=0.7, s=60, c='salmon', offset_text=1, txt_1=None, txt_2=None):

    plt.scatter(data=df, x=x, y=y, alpha=alpha, s=s, c=c)

    df_range = range(df.shape[0])

    x, y = df[x].tolist(), df[y].tolist()

    if txt_1: 
        names = df[txt_1].to_list()
    else: 
        names = ['' for i in df_range]

    if txt_2: 
        states = df[txt_2].to_list()
    else:
        states = ['' for i in df_range]
    
    for i in df_range:
        text = f"{names[i]} {states[i]}"

        plt.annotate(text, (x[i], y[i]), xytext=(x[i]+offset_text, y[i]+offset_text))

        