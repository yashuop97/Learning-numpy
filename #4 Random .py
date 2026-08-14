import numpy as np


matrix = np.random.rand(2, 3) # this creates a matrix which give us values which is random and we can specify a size of values we want and it will return random values between 0 to 1 by default

print(matrix)

matrix2 = np.random.randn(3,3) # this will give us a matrix with values this is similar to the first cmd but it gives us values from -1 to 1 center is zero we can specify the size

print(matrix2)

matrix3 = np.random.randint(1, 100, size = (2, 3)) # this will give us a random integer from the range we specify for example .random.randint(start*, end*)

print(matrix3)

print(matrix3.dtype) # this will print the type of the matrix .dtype is the syntax