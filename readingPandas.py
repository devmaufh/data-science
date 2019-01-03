import pandas as pd
path_file="des.csv"
encoding_file="latin-1"
data = pd.read_csv(path_file,encoding=encoding_file)
print(data.head())
