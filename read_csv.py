import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "cities.csv"
df = pd.read_csv(filename)

data_array = df.iloc[:,:-1].values #all columns except the last 
last_column_data = df.iloc[:, -1] 

x = data_array[:, 0]
y = data_array[:, 1]

plt.scatter(x,y, color="blue", alpha= 0.7)
plt.xlabel("Column 1")
plt.ylabel("Column 2")
plt.title("BAsic Scatter graph ")
plt.grid(True)
plt.show()