import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from typing import List


def standardize(df: pd.DataFrame, columns: List[str] = None):
    """
    Standardizes columns of a DataFrame using StandardScaler(). Columns must be numerical.
    :param df: pd.Dataframe - DataFrame
    :param columns: List[str] - Optional. A list of the column names. If none provided,
    all columns will be standardized.
    :return: df - df with standardized columns.
    """
    df[columns if columns else df.select_dtypes(['float64', 'int64']).columns.values] = ColumnTransformer([
        ('StandardScaler', StandardScaler(), columns if columns else df.columns.values)
    ]).fit_transform(df)

    return df


