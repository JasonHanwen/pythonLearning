import numpy as np
#when I learn this, I konw that numpy is actually a good package just like matlab
#this is a very easy way to turn the list to array in numpy package
data = [6,7.5,8,0,1]
arr1 = np.array(data)
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print arr1
#this is to print the type of the data in the matrix, so in the future we can use this to do some math manipulation
print arr1.dtype
print arr2

print arr2.shape
