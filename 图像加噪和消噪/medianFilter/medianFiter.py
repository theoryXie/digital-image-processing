import numpy as np
import cv2
import matplotlib.pyplot as plt

'''
    中值滤波器 -- 针对椒盐盐噪声
    filter_size -- 滤波器大小
'''
def medianFilter(img, filter_size):
    tempImg1 = tempImg2 = img.copy().astype(np.int16)
    pad_num = int((filter_size-1)/2)#中点距离边界的长度
    tempImg1 = np.pad(tempImg1, (pad_num, pad_num), mode="constant", constant_values=0)
    m, n = tempImg1.shape
    for i in range(pad_num+1, m-pad_num-1): #此处加1减1是为了防止0对结果的影响
        for j in range(pad_num+1, n-pad_num-1):
            data_matrix = tempImg2[i-pad_num:i+pad_num+1, j-pad_num:j+pad_num+1]
            tempImg1[i,j] = np.median(data_matrix)
    return tempImg1





img = cv2.imread("PepperAndSalt/saltAndPepper.jpg",0)#轻度椒盐噪声图片
newImg = medianFilter(img, 3)
cv2.imwrite("medianFilter/medianFilter.jpg",newImg)


img = cv2.imread("PepperAndSalt/reinforce_SaltAndPepper.jpg",0)#重度椒盐噪声噪声图片
newImg = medianFilter(img, 7)
cv2.imwrite("medianFilter/reinforce_MedianFilter.jpg",newImg)