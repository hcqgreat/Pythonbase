#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

import numpy as np

array = np.array([1,2,3,4,5])
print(array)
print(type(array))

array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2)
print(type(array2))

array3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(array3)
print(type(array3))

#array结合dtype的使用

array4 = np.array([[1, 2, 3], [4, 5, 6]], dtype= float)
print(array4)
print(type(array4))
print(type(array4[1][1]))

#array的ndmin使用
array5 = np.array([1, 2, 3], dtype=float, ndmin=3)
print(array5)
print(type(array5))



