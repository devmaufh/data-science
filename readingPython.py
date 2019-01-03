path_file="des.csv"
data2= open(path_file,"r")
cols=data2.readline().strip().split(",")
files_count= sum(1 for line in data2)
print(files_count)

main_dict={}
for col in cols:
    main_dict[col]=[]


with open(path_file,"r") as dataset:
    for lines in dataset:
        value=lines.strip().split(",")
        for i in range(len(cols)):
            main_dict[cols[i]].append(value[i])
