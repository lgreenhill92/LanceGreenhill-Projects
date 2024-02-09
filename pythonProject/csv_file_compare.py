import pandas as pd


def compare_csv(file1, file2):
    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        if df1.equals(df2):
            print("File validation passed.")
            return "Pass"
        else:
            diff_df = df1.compare(df2)
            print("Differences between files:")
            print(diff_df)
            return "Fail"
    except:
        print("An error occurred. If you are sure that your file location is correct the data file may have failed "
              "testing.\n" + "Example of file path: C:/temp/HourlyExport.csv")



compare_csv("C:/temp/HourlyExport.csv", "C:/temp/HourlyExport6.csv")