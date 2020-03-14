
import numpy as np
import cv2
import matplotlib.pyplot as plt



'''
    均值滤波器
    filter_size -- 滤波器大小
'''
def MeansFilter(img, filter_size):
    tempImg1 = img.copy()
    pad_num = int((filter_size-1)/2)#中点距离边界的长度
    tempImg1 = np.pad(tempImg1, (pad_num, pad_num), mode="constant", constant_values=0)
    tempImg2 = tempImg1.copy()
    m, n = tempImg1.shape
    for i in range(pad_num, m-pad_num):
        for j in range(pad_num, n-pad_num):
            #滤波矩阵中心点 = 滤波矩阵的算术平均值
            tempImg1[i,j] = np.sum(tempImg2[i-pad_num:i+1+pad_num,j-pad_num:j+1+pad_num]) / (filter_size **2)
    return tempImg1


img = cv2.imread("gaussNoise/gauss_ans.jpg",0)
filterImg = MeansFilter(img, 3)
# plt.imshow(filterImg, cmap='gray')
# plt.show()
cv2.imwrite("meansFilter/meansFilter.jpg",filterImg)