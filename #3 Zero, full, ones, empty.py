import numpy as np


matrix = np.zeros([10, 10]) # creates matrix with X numbers of zeroes which we specify and we can also specify the shape instead of number of zeroes eg [x, y]

print(matrix)

matrix2 = np.full(5,10000) # create matrix with X element which we specifiy X amount of time which we also specifiy for example we put .full(*no of time*, *value*)

print(matrix2)

matrix3 = np.ones([10, 10]) # exact same as zeros just with ones

print(matrix3)

matrix4 = np.empty([5]) # exact same as zeros and ones it just contain no vlaues at all

print(matrix4)