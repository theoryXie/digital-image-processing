
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import random
import cv2

'''
    将y轴转化为概率
'''
def to_percent(y, position):
    return str(100 * y) + '%'

'''
    添加均匀噪声
    means：均值
    sigma：方差
    percetage：比例
'''
def addAverageNoise(img, low, high, percetage=1):
    row,col = img.shape
    num = int(percetage * row * col)
    s = np.random.uniform(low,high,num) #均匀生成num个上界为high，下界为low的随机数
    '''
        显示均匀分布的柱状图
    '''
    plt.hist(s,bins=256 ,weights= [1./ len(s)] * len(s))
    formatter = FuncFormatter(to_percent)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()

    '''
        将噪声添加到图像中
    '''
    noiseImg = img.copy().astype(np.int16)
    for i in range(num):
        randX = random.randint(0, row-1)
        randY = random.randint(0, col-1)
        # print(noiseImg[randX, randY])
        noiseImg[randX, randY] = noiseImg[randX, randY] + int(s[i])
        # print(noiseImg[randX, randY])
        np.clip(noiseImg,0,255)
    return noiseImg


img = cv2.imread("gray.jpg",0)
noiseImg = addAverageNoise(img, -70, 70, 0.6)
# plt.imshow(noiseImg,cmap = 'gray')
# plt.show()
cv2.imwrite("averageNoise/avgNoise.jpg", noiseImg)