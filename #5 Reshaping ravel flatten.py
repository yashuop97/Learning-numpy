import numpy as np

matrix = np.array([1,2,3,4,5,6,7,8,9])

matrix = matrix.reshape(3,3) # reshapes the array to the size we specify for example .reshape(3,3)

print(matrix)



matrix2 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

matrixnew = matrix.ravel() # this reshapes any array to 1D it reflects the value in orignal too 

print(matrixnew)



matrix3 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

matrix3new = matrix3.flatten() # this also reshapes any array to 1D but it creates a copy instead of reflecting to orignical array too

print(matrix3new)

matrixnew = matrix3.transpose()

print(matrixnew)