import numpy as np


matrix = np.linspace(1,10,3, dtype = int) # .linspace creates a matrix with valaues between 2 numbers we put .linspace(*start*, *end*, *no of values*)

print(matrix)


matrix2 = np.logspace(1, 3, 6) # .logspacce creates a matrix with values which are based on log for example log(1) = 10, log(2) = 100 we put .logspace(*start*, *end*, *no of values)

print(matrix2)


matrix3 = np.arange(1, 10, 2) # .arange creates a matrix with values which are in specific ranges we put .arange(*start*,*end*,*step up*)

print(matrix3)