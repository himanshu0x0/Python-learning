import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

#generating an array with a range of numbers 
range_arr = np.arange(10,20,2)

#generating an array with random numbers 
random_arr = np.random.randint(1,100,(3,3))

#perform some operation
mean_value = np.mean(arr)
max_value = np.max(arr)
sum_value = np.sum(arr)

print(arr)
print(range_arr)
print(random_arr)
print(mean_value)
print(max_value)
print(sum_value)