#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

import numpy as np
import math

a = np.arange(10)
print(a)
print(type(a))

#numpy中对ndarray类型的向量开平方方法

print(np.sqrt(a))




#列表方式对其中的数据开平方并储存

result = []
b = [3,5,9]

for i in b :
    result.append(math.sqrt(i))

print(result)