import pandas as pd
import numpy as np
import openpyxl

import pandas as pd


def compare_csv(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Merge the DataFrames based on a common column or index
    merged = pd.merge(df1, df2, left_index=True, right_index=True, how='outer', suffixes=('_1', '_2'))

    if merged.isnull().values.all():
        return "Pass"
    else:
        diff_df = merged[merged.notnull().any(axis=1)]
        print("Differences between files:")
        print(diff_df)
        return "Fail"


compare_csv("C:/temp/HourlyExport.csv", "C:/temp/HourlyExport2.csv")
