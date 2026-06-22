import pandas as pd 

data_set = pd.read_csv("./dataset.csv")
print("====================== raw data ======================")
print(data_set)
# 


# filtered_data = data_set[data_set["Study_Hours"] > 6.0]
# print("====================== filtered data ======================")
# print(filtered_data)


# add new column
data_set["Passed"] = data_set["Test_Score"] > 80
print("====================== added passed column ======================")
print(data_set)