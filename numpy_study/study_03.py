#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

import numpy as np


array1 = np.arange(1, 11)
print(array1)

#设置步长
array2 = np.arange(1, 11, 3)
print(array2)

#设置dtype
array3 = np.arange(1, 11, 3, dtype=float)
print(array3)