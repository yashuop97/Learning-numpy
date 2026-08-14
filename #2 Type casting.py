import numpy as np


matrix = np.array([1,2,3])

matrixnew = matrix.astype(np.str_) # this convers the value to different for example str_ stands for string int32 or int64 for integers and float32 and float64 for floating values

print(matrixnew.dtype) 