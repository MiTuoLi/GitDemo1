import numpy as np
# lesson2：
# (1) 数组的维度，一维，二维，三维
# (2) print(a.shape)可以查看数组的形状，这个结果是一个元祖
# (3) a.reshape(24,)-把a变一维；a.reshape(4,6)-把a编程4行6列的二维；a.reshape(2,3,4)-把a变成2块3行4列的三维
# (4) 要注意a.reshape(24,)和a.reshape(1,24)的区别
# (5) 不清楚一个数组具体元素个数时，把他变成一维的两种方法
# (6) 数组和数字的计算，广播机制，数组中的每个数都进行计算。其中，除以0时：0/0得到nan这个数据（不存在），其他数/0得到inf（无穷大）
#     数组和数组进行计算：（1）如果2个数组形状完全相同，每个位置的元素对应进行计算
#                      (2) 二维数组可以跟行同列1的数组，或者行1列同的数组算
#                      (3)三维数组在某个方向上一样也可计算



# a1 = np.array(range(12)) #一维数组，一个单列表
# a2 = np.array([[1,2,3],[4,5,6]]) #二维数组，列表里套列表，这里这个是2行3列
# a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #三维数组，列表里套列表再套列表
# print(a1.shape)
# print(a2.shape)
# print(a3.shape)
#
# a = np.array(range(24)) #生成一个元素个数24的一维数组
# print(a)
# print(a.shape)
# a = a.reshape(4,6) #将数组a的形状改为4行6列的数组
# print(a)
# print(a.shape)
# a = a.reshape(2,3,4) #将数组a的形状改为2块，3行，4列的数组
# print(a)
# print(a.shape)
#
# a = a.reshape(24,) #将数组a变回1维数组
#
# # 注意下面2者区别！一个是一维数组，一个是二维数组，二维数组多嵌套了个中括号！
# a = a.reshape(24,)
# print(a)
# print(a.shape)
# a = a.reshape(1,24)
# print(a)
# print(a.shape)
#
# # 如何在不清楚一个数组的元素个数时把他变成一维数组？
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# # 方法一：
# a = a.reshape(a.shape[0]*a.shape[1],) # 这里假设知道了a是2维的，这样shape[0]就是行，shape[1]就是列，俩一乘再用reshape
# print(a)
#
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# # 方法二：
# a = a.flatten() # 此方法吧数组a展开成一个一维的
# print(a)
#
# # 数组和数字的计算
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a)
# a = a + 2
# print(a)
# print(a.dtype)
# a = a*2
# print(a)
# print(a.dtype)
# a = a/2
# print(a)
# print(a.dtype)
# # a = a/0
# # print(a)
# # print(a.dtype)
#
# # 数组和数组计算
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print('a:\n',a)
# a1 = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3]])
# a2 = np.array([1,2,3,4])
# a3 = np.array([[1],[2],[3]])
# print('a+a1:\n',a+a1)
# print('a+a2:\n',a+a2)
# print('a+a3:\n',a+a3)
a = np.array([1,2,3])
print(a.shape)
a2 = np.array([[1,2,3],[4,5,6]])
print(a2.shape)
a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a3.shape)
a3 = a3.flatten()
print(a3)
print(a3.shape)
a3 = a3.astype('float64')
print(a3.dtype)

