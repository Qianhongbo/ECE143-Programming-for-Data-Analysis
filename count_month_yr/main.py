import pandas as pd

# def add_month_yr(x):
#     """
#
#     :param x: survey dataframe
#     :return: the same pd.DataFrame with the new column
#     """
#     assert isinstance(x, pd.DataFrame)
#
#     df = x[['ID','Timestamp']]
#     df['Timestamp'] = pd.to_datetime(df['Timestamp'])
#     df['year'] = df['Timestamp'].dt.strftime('%Y')
#     df['month'] = df['Timestamp'].dt.month_name().str[:3]
#     df["month-yr"] = df["month"] + "-" + df['year']
#     df = df.drop(['Timestamp', 'year', 'month'], axis=1)
#     return df

def add_month_yr(x):
    """

    :param x: survey dataframe
    :return: the same pd.DataFrame with the new column
    """
    assert isinstance(x, pd.DataFrame)

    df = x
    df['month-yr'] = pd.to_datetime(df['Timestamp']).dt.strftime('%b-%Y')
    return df

def count_month_yr(x):
    """

    :param x: a pd.DataFrame
    :return: a pd.DataFrame
    """
    assert isinstance(x, pd.DataFrame)
    df = x['month-yr'].value_counts().sort_index(ascending=True)
    df = pd.DataFrame(data=df, columns=["month-yr"])
    return df


if __name__ == "__main__":
    df = pd.read_csv("survey_data.csv")
    print(count_month_yr(add_month_yr(df)))