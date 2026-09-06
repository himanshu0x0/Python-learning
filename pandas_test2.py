import pandas as pd

data = {
    "Name" : ["Himanshu", "Lucifer", "Kartik"],
    "Age" : [19,23,20],
    "Cities" : ["Delhi", "Kolkata", "Mumbai"]
}

df = pd.DataFrame(data)
print(df[["Name","Age"]])

print(df.loc[0:1:2])
