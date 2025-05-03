import pandas as pd

df=pd.read_parquet("C:\\Users\\shiel\\Downloads\\Sample_data_2.parquet", engine="pyarrow")
number_of_columns = len(df.columns)

print(number_of_columns)