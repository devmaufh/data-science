import pandas as pd
import csv
import urllib3
dataset_url="http://winterolympicsmedals.com/medals.csv"
http=urllib3.PoolManager()
response=http.request('GET',dataset_url).data.decode().split('\n') #Save csv in response 
main_dict={}
cols=response[0].replace(' ',',').split(',')
for i in cols:
    main_dict[i]=[]
cols=[keys for keys in main_dict]
counter=0
for lines in response:
    if counter==0:
        pass
    else:
        value=lines.split(",")
        for i in range(len(main_dict)):
            main_dict[cols[i]].append(value[i])
    counter+=1
df=pd.DataFrame(main_dict)
print(df.head(10)) 
print(df.tail(10))
df.to_csv("medals.csv")