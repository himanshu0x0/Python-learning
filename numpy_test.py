import numpy as np

arr = np.array([1,2,3,4,5,6,7])

#generating an array with a range of numbers

range_arr = np.arange(10,20)

random_arr = np.random.randint(10,100,(3,3))

random_arr1 = np.random.randn(1000)

print(f"original array : {arr}")

#operation on array

sum_arr = np.sum(arr)
mean_arr = np.mean(arr)
max_arr = np.max(arr)

print(sum_arr)