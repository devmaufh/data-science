import pandas as pd
dataset_url="https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/titanic/titanic3.csv"
dataset=pd.read_csv(dataset_url)
print(dataset.describe()) #Describe all numeric variables
print(dataset.dtypes) #Returns column types
pd.isnull(dataset["body"]).values.ravel().sum() #Count all missing values from body
