import numpy as np 

matrix = np.array([1,2,3]) # formation of array 1D

print(matrix) 
print(matrix.ndim)

matrix2d = np.array([[1,2,3],[4,5,6]]) # formation of array 2D

print(matrix2d)
print(matrix2d.ndim)

matrix3d = np.array([[[1,2,3],[4,5,6],[7,8,9]], # formation of array 3D
                     [[10,11,12],[13,14,15],[16,17,18]],
                     [[19,20,21],[22,23,24],[25,26,27]]])

print(matrix3d)
print(matrix3d.ndim) # no of dimension cmd .ndim
print(matrix3d.shape) # shows the shape of matrix/array