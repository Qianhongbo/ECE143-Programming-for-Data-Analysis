import pandas as pd

def add_month_yr(x):
    """

    :param x: survey dataframe
    :return: the same pd.DataFrame with the new column
    """
    assert isinstance(x, pd.DataFrame)

    df = x[['ID','Timestamp']]
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['year'] = df['Timestamp'].dt.strftime('%Y')
    df['month'] = df['Timestamp'].dt.month_name().str[:3]
    df["month-yr"] = df["month"] + "-" + df['year']
    df = df.drop(['Timestamp', 'year', 'month'], axis=1)
    return df

# if __name__ == "__main__":
#     df = pd.read_csv("survey_data.csv")
#     print(add_month_yr(df))
#     print(add_month_yr(df)['month-yr'] )