'''
Created on Tue Sep 17 20:57:46 2019

@author: 谢帅宇

@description: 基于python，matplotlib实现直方图均衡化
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


# 导入图片，并将图片转化为灰度图片
def getGrayImg(path):
    img = cv2.imread(path,)                                  #导入图片
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return img


# 展示图片的直方图，返还相关信息
def showImgHistogram(img_gray_1D):
    plt.hist(img_gray_1D,bins=256 ,density=1)
    plt.show()



#直方图均衡化
def averageImg(img):
    nk = np.zeros(256)                         #各灰度值数量
    tk = np.zeros(256)                         #映射关系
    m,n = img.shape 
    #求各灰度值数量  
    for i in range(m):
        for j in range(n):
            nk[img[i][j]] = nk[img[i][j]] + 1

    #求各灰度值累计比例，并取整扩展
    for i in range(256):
        sk = 0
        for j in range(i+1):
            sk = sk + (nk[j] / (m*n))
        tk[i] = math.floor((256 - 1) * sk + 0.5)   # 根据公式tk=int[(N-1)*tk+0.5]灰度值i->灰度值tk[i]
    
    #均衡化图像
    newImg = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            newImg[i][j] = tk[img[i][j]]
    
    return newImg

    

    





if __name__ == '__main__':
    img = getGrayImg("flower.jpeg")                                         #将图像转化为灰度图像
    img_gray_1D = img.flatten()                                             #压缩二维矩阵为一维
    plt.imshow(img, cmap='gray')                                            #展示原图
    plt.show()
    showImgHistogram(img_gray_1D)                                           #展示原来灰度图的直方图
    
    newImg = averageImg(img)                                                #均衡化图片
    plt.imshow(newImg, cmap='gray')                                         #展示均衡化后的图片
    plt.show()
    showImgHistogram(newImg.flatten())                                      #展示均衡化后的直方图


    