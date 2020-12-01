""""Lambdata - a collection """""


import pandas as pd
import numpy as np 


def train_test_split(df, frac):
    """"Train_test_split of data frame """""
    #TODO -implement 
    arr_rand = np.random.rand(df.shape[0])
    split = arr_rand < np.percentile(arr_rand, (frac*100))
    df_test = df[split]
    df_train = df[~split]
    return df_test, df_train

def df_summary (dataframe,upper=False):
  nrows = dataframe.shape[0]
  ncolumns= dataframe.shape[1]
  missing = dataframe.isnull().sum().to_dict()
  #converting to nested dictionary for cleaner output
  if(upper==False):
    labels= list(dataframe.columns)
  else:
    labels = [x.upper() for x in dataframe.columns]
  dict = {
      'nrows':nrows,
      'ncolumns':ncolumns,
      'missing':missing,
      'labels':labels
  }
  for k,v in dict.items():
    print(k)
    print(v)    