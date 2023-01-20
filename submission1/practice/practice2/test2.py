import numpy as np

arr = np.array([1,2,3,4,5,4,5])
print(arr.dtype)
arr.dtype = "S"
# print(arr)


names = np.array(["a","b","a"])
a = (names == "b")
print(a)

