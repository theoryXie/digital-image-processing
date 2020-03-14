'''
    添加高斯噪声
'''

import numpy as np
import cv2 as cv
import random
import matplotlib.pyplot as plt

'''
    高斯噪声
    means: 均值
    sigma：标准差
    percetage：比例
'''
def addGaussNoise(img, means, sigma, percetage):
    noiseImg = img.copy().astype(np.int16)
    rows, cols = img.shape
    num = int(percetage*rows*cols)#添加噪声的数量
    noise = np.random.normal(means, sigma, num)
    for i in range(num):
        randX=random.randint(0,rows-1)
        randY=random.randint(0,cols-1)
        noiseImg[randX, randY]= noiseImg[randX,randY] + int(noise[i])#添加高斯噪声
        np.clip(noiseImg,0,255)
    return noiseImg


'''
    网上的高斯噪声
'''
# def gauss_noise(image, mean=20, sigma=10):
#     ''' 
#         添加高斯噪声
#         mean : 均值 
#         var : 方差
#     '''
#     image = np.array(image/255, dtype=float)
#     noise = np.random.normal(mean, sigma, image.shape)
#     out = image + noise
#     if out.min() < 0:
#         low_clip = -1.
#     else:
#         low_clip = 0.
#     out = np.clip(out, low_clip, 1.0)
#     out = np.uint8(out*255)
#     #cv.imshow("gasuss", out)
#     return out

img = cv.imread("gray.jpg",0) #单通道！
noiseImg_ans = addGaussNoise(img,20,10,1) #添加高斯噪声
# plt.imshow(noiseImg, cmap='gray')#plt的imshow会自动弄成三通道，所以要加cmap='gray'
# plt.show()
cv.imwrite("gaussNoise/gauss_ans.jpg",noiseImg_ans)

