from time import strptime
import pandas as pd
import numpy as np
import matplotlib as plt


## Supllemntry functions for data parsing and tidying

def month_str_to_int(month): # convert a month's name to a float number
    try:
        month_num = strptime(month, '%B').tm_mon
    except:
        return None
    return month_num


def convert_column_to_num_month(df, column_name): #apply month_str_to_int to a whole column
    df = df[column_name]
    df = df.apply(month_str_to_int)
    df = df.apply(lambda x: "{:.0f}".
                  format(x) if not pd.isnull(x) else x) # format as int
    return df


def csv_load(file): # suuplementry to load a CSV file and return as df, in the future to be extended
    df = pd.read_csv(file)
    return df


df = csv_load("Data/feature_data.csv")
df = convert_column_to_num_month(df, "order_month")
print(df)
