import pandas as pd
from pandas.api.types import CategoricalDtype

def add_month_yr(x):
    """

    :param x: survey dataframe
    :return: the same pd.DataFrame with the new column
    """
    assert isinstance(x, pd.DataFrame)

    df = x
    df['month-yr'] = pd.to_datetime(df['Timestamp']).dt.strftime('%b-%Y')
    return df


def fix_categorical(x):
    """

    :param x: x is a pd.DataFrame with the required "month-yr" column
    :return: output is a pd.DataFrame with the "month-yr" column having the categorical dtype
    """
    assert isinstance(x, pd.DataFrame)

    df = x
    t = CategoricalDtype(categories=['Sep-2017', 'Jan-2018', 'Feb-2018', 'Mar-2018', 'Apr-2018', 'Sep-2018', 'Oct-2018', 'Jan-2019'], ordered=True)
    df['month-yr'] = df['month-yr'].astype(t)
    return df


# if __name__ == "__main__":
#     df = pd.read_csv("survey_data.csv")
#     x = fix_categorical(add_month_yr(df))
#     print(x)
#     print(x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())

