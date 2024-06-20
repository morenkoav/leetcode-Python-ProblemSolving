'''
Write a solution to concatenate these two DataFrames vertically into one DataFrame.
'''

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    conc_df = pd.concat([df1, df2])
    return conc_df