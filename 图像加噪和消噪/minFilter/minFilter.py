
import numpy as np
import cv2
import matplotlib.pyplot as plt

'''
    最小值滤波器 -- 针对盐噪声
    filter_size -- 滤波矩阵大小
'''
def minFilter(img, filter_size):
    tempImg1 = img.copy().astype(np.int16)#避免溢出
    pad_num = int((filter_size-1)/2)#中点距离边界的长度
    tempImg1 = np.pad(tempImg1, (pad_num, pad_num), mode="constant", constant_values=0)
    tempImg2 = tempImg1.copy()
    m, n = tempImg1.shape
    for i in range(pad_num+1, m-pad_num-1): #此处加1减1是为了防止0对结果的影响
        for j in range(pad_num+1, n-pad_num-1):
            data_matrix = tempImg2[i-pad_num:i+pad_num+1, j-pad_num:j+pad_num+1]
            tempImg1[i,j] = np.min(data_matrix)#中心值 = 滤波矩阵最小值
    return tempImg1



img = cv2.imread("PepperAndSalt/salt.jpg",0)#盐噪声图片
newImg = minFilter(img, 3)
cv2.imwrite("minFilter/minFilter.jpg",newImg)