from time import strptime
import pandas as pd
import numpy as np
import matplotlib as plt


def month_str_to_int(month):
    try:
        month_num = strptime(month, '%B').tm_mon
    except:
        return None
    return month_num


def convert_column_to_num_month(df, column_name):
    df = df[column_name]
    df = df.apply(month_str_to_int)
    df = df.apply(lambda x: "{:.0f}".
             format(x) if not pd.isnull(x) else x)
    return df


def csv_load(file):
    df = pd.read_csv(file)
    return df


df = csv_load("feature_data.csv")
df = convert_column_to_num_month(df, "order_month")
print(df)
