from matplotlib import pyplot as plt
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]
# 调整画图的尺寸和dpi清晰度
fig1 = plt.figure(figsize=(20,8),dpi=80)
# 画图
plt.plot(x,y)
# 保存图片，注意要写在show前，否则保存的是空白图片
plt.savefig('./fig1.png')
plt.show()