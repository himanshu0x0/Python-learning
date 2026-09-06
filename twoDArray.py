import matplotlib.pyplot as plt
import numpy as np 

foods = ["Meat", "Banana", "Avocados", "Sweet Potatoes", "Spinach", "Watermelon", "Coconut Water", "Beans", "Legumes", "Tomato"]
calories = [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]
potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]

plt.figure(figsize=(10,5))

bar_width = 0.25

x = np.arange(len(foods))

plt.bar(x-bar_width, calories, width = bar_width, label = "Calories", color = "red")
plt.bar(x, potassium, width = bar_width, label = "Potassium", color = "blue")
plt.bar(x+bar_width, fat, width = bar_width, label = "Fat", color = "green")

plt.xticks(ticks=x,labels=foods, rotation= 45)
plt.xlabel("Food Items")
plt.ylabel("Nutrient Values")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()