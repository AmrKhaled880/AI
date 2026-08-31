import pandas as pd
from config.config import DROP_COLUMNS

def drop_col(df: pd.DataFrame, drop_columns : list[str]) -> pd.DataFrame :
    '''
    drop specific columns from df

    parameter
    --------
    df : pd.DataFrame
    columns : list[str]

    return
    ------
    pd.DataFrame

    '''
    return df.drop(columns= drop_columns)

def get_chk_dtypes(df : pd.DataFrame) -> pd.DataFrame :
    return pd.DataFrame({'Dtype : ': df.dtypes , 'Num_unique': df.nunique()}).T
