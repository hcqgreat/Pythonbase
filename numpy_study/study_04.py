#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

import numpy as np
import pandas as pd
#使用random创建一维数组
array1 = np.random.random(size=5)
print(array1)
print(type(array1))

#使用random创建二维数组
array2 = np.random.random(size=(3, 4))
print(array2)