'''
Created on Tue Sep 17 18:26:46 2019

@author: 谢帅宇

@description: 基于python，opencv实现灰度图像比特平面分层
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''           
    00000001  0-2
    00000010  3-4
    00000100  5-8
    00001000  9-16
    00010000  17-32
    00100000  33-64
    01000000  65-128
    10000000  129-255
'''
levels = {
        0: [0,2],
        1: [3,4],
        2: [5,8],
        3: [9,16],
        4: [17,32],
        5: [33,64],
        6: [65,128],
        7: [129, 255]      
}


# 导入图片，并将图片转化为灰度图片
def getGrayImg(path):
    img = cv2.imread(path)                                  #导入图片
    grayimg= np.zeros((img.shape[0], img.shape[1]))         #创建灰度图片
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            grayimg[i,j] = max(img[i,j][0], img[i,j][1], img[i,j][2])  #平均法求灰度值
    return grayimg




# 灰度级分层
def cut_layer(img, level):
    m, n = img.shape
    newImg = np.zeros([m,n])
    start, end = levels[level][0], levels[level][1]
    for i in range(m):
        for j in range(n):
            if (img[i][j] >= start and img[i][j] <= end):   #在此灰度级内，则颜色加深，否则变成黑色
                newImg[i][j] = 255
            else:
                newImg[i][j] = 0
    
    plt.imshow(newImg,cmap='gray')  
    plt.show() 



# 展示高4bit层和低4bit层的图片
def displayHeigh4AndLow4(img):
    #高四层
    start = levels[4][0]
    end = levels[7][1]
    m, n = img.shape
    newImg = np.zeros([m,n])
    for i in range(m):
        for j in range(n):
            if (img[i][j] >= start and img[i][j] <= end):   #在此灰度级内，则颜色加深，否则变成黑色
                newImg[i][j] = 255
            else:
                newImg[i][j] = 0
    plt.imshow(newImg,cmap='gray')  
    plt.show() 
    
    #低4层
    start = levels[0][0]
    end = levels[3][1]
    m, n = img.shape
    for i in range(m):
        for j in range(n):
            if (img[i][j] >= start and img[i][j] <= end):   #在此灰度级内，则颜色加深，否则变成黑色
                newImg[i][j] = 255
            else:
                newImg[i][j] = 0
    plt.imshow(newImg,cmap='gray')  
    plt.show() 

if __name__ == '__main__':
    img = getGrayImg("kebi.jpeg")  #灰度处理

	#灰度级分层
    for i in range(8):
    	cut_layer(img, i)


    #展示高4bit层和低4bit层的图片
    displayHeigh4AndLow4(img)



    



    
    
