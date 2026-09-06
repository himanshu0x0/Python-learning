import matplotlib.pyplot as plt
import numpy as np

#generating random 1000 values
data = np.random.randn(1000)

plt.hist(data, bins=30, color="skyblue",edgecolor='black', alpha=0.7)
plt.xlabel("value")
plt.ylabel("Frequency")
plt.title("Random histograph of 1000 values")
plt.grid(True)
plt.show()