import pandas as pd
dataset_url="http://winterolympicsmedals.com/medals.csv"
dataset=pd.read_csv(dataset_url)
print(dataset.head())
