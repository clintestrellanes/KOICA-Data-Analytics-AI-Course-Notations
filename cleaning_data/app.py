import pandas as pd


data = pd.read_csv("./raw_employee_data.csv")

print(data)
print("======================= Raw Data =======================")

print("======================= Standardize Name =======================")
data["Name"] = data["Name"].str.upper()
# print(data)

print("======================= Standardize Age =======================")
data["Age"] = pd.to_numeric(data["Age"], errors='coerce')
print(data)



