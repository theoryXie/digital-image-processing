

import numpy as np
import cv2
import matplotlib.pyplot as plt

'''
    最大值滤波器 -- 针对椒噪声
    filter_size -- 滤波器大小
'''
def maxFilter(img, filter_size):
    tempImg1 = img.copy().astype(np.int16)
    filterMat = np.ones((filter_size, filter_size)) #滤波器模板
    pad_num = int((filter_size-1)/2)#中点距离边界的长度
    tempImg1 = np.pad(tempImg1, (pad_num, pad_num), mode="constant", constant_values=0)
    tempImg2 = tempImg1.copy()
    m, n = tempImg1.shape
    for i in range(pad_num+1, m-pad_num-1): #此处加1减1是为了防止0对结果的影响
        for j in range(pad_num+1, n-pad_num-1):
            data_matrix = tempImg2[i-pad_num:i+pad_num+1, j-pad_num:j+pad_num+1]
            tempImg1[i,j] = np.max(data_matrix)
    return tempImg1



img = cv2.imread("PepperAndSalt/pepper.jpg",0)#椒噪声图片
newImg = maxFilter(img, 3)
cv2.imwrite("maxFilter/manFilter.jpg",newImg)