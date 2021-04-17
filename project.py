from time import strptime

import matplotlib
import pandas as pd
import numpy as np
import matplotlib as plt


# Supplementary functions for data parsing and tidying

# Month to int function
from matplotlib.pyplot import plot, xlabel, ylabel, title, show


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

#Correlation creator
## This function shall be used for numeric features only

def plot_correlations(feature1, feature2):
    plot(df[feature1], df[feature2],)
    xlabel(feature1)
    ylabel(feature2)
    title(("The correlation between {} and {}".format(feature1, feature2)))
    show()
    return


# Main build

df = csv_load("Data/feature_data.csv") #Reading the CSV data file
features = df.columns

# Data manipulations

df["order_month"] = convert_column_to_num_month(df, "order_month")

# Plotting



