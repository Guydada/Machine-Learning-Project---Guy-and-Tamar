import pandas as pd
from time import strptime
import matplotlib as plt


def month_str_to_int(month):  # convert a month's name to a float number
    try:
        month_num = strptime(month, '%B').tm_mon
    except:
        return None
    return month_num


def week_str_to_int(week):  # convert a month's name to a float number
    try:
        week_num = week.strip("week_")
    except:
        return None
    return week_num


def convert_column_to_num_month(df, column_name):  # apply month_str_to_int to a whole column
    df = df[column_name]
    df = df.apply(month_str_to_int)
    df = df.apply(lambda x: "{:.0f}".
                  format(x) if not pd.isnull(x) else x)  # format as int
    df = df.apply(lambda x: int(x) if not pd.isnull(x) else x)
    return df


def strip_week_column(df, column_name):
    df = df.apply(week_str_to_int)
    df = df.apply(lambda x: "{:.0f}".
                  format(x) if not pd.isnull(x) else x)  # format as int
    df = df.apply(lambda x: int(x) if not pd.isnull(x) else x)
    return df


def month_num_season(mon): # returns a season number by month number
    trans = {1: [3, 4, 5], 2: [6, 7, 8] , 3:[9, 10, 11] , 4: [12, 1, 2]}
    for i in trans.keys():
        if mon in trans[i]:
            return i


# Correlation creator


def plot_correlations(feature1, feature2):
    plt.plot(df[feature1], df[feature2])
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.title(("The correlation between {} and {}".format(feature1, feature2)))
    plt.show()
    return


def plot_scatter(df, feature1, feature2):
    plt.scatter(df[feature1], df[feature2])
    plt.grid()
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.title(("The correlation between {} and {}".format(feature1, feature2)))
    plt.show()
    pass



