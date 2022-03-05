import pandas as pd

def split_count(x):
    """

    :param x: x is a pd.Series object
    :return: a pd.DataFrame object
    """
    assert isinstance(x, pd.Series)

    df = x.to_frame()
    df = df["Is there anything in particular you want to use Python for?"].str.split(', ', expand=True)
    print(df)
    print(type(df))
    df_new = df[0].value_counts()
    for i in range(1, 7):
        temp = df[i].value_counts()
        df_new = df_new.add(temp, fill_value=0)
    df_new = df_new.astype(int)
    df_new = pd.DataFrame(data = df_new, columns = ["count"])
    return df_new


# if __name__ == "__main__":
    # series = pd.read_csv("survey_data.csv", usecols=[1,8], squeeze=True)
    # print(series)
    # print(type(series))
    # print(series)
    # print(split_count(series))
    # df = series.to_frame()
    # print(df)

