import numpy as np
import random

# lesson 1:
# (1) numpy.array()
# (2) numpy.array([],dtype='')指定数据类型
# (3) print(a.dtype)查看数组中的数据类型
# (4) a = a.astype('数据类型')修改数据类型
# (5) a = np.round(a,2)保留数据的前两位小数
# a = np.array([1,2,3])
# print(a)
# a = np.array(range(10))
# print(a)
# a = np.arange(10)
# print(a)
# print(type(a)) #数组的类型是ndarray
# print(a.dtype) #数组.属性看数组中数据类型，是int32位
#
# a1 = np.array(range(10),dtype='float64') #生成数组时可以指定类型
# print(a1)
# print(a1.dtype)
#
# a1 = a1.astype('int64') #使用数组.astype方法可以修改存放的数据类型，需要接收
# print(a1)
# print(a1.dtype)
#
# a2 = np.array([random.random() for i in range(10)])
# print(a2)
# a2 = np.round(a2,2) #np.round方法可以保留小数，需要接收
# print(a2)

a = np.array(range(10))
print(a)