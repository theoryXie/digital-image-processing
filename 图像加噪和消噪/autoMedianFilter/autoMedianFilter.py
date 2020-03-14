import numpy as np
import cv2
import matplotlib.pyplot as plt

'''
    自适应中值滤波器 -- 针对椒盐噪声
    filter_size     -- 初始滤波尺寸
    Smax            -- 窗口允许的最大尺寸
'''
def autoMedianFilter(img, filter_size, Smax):
    tempImg1 = tempImg2 = img.copy().astype(np.int16)
    pad_num = int((filter_size-1)/2)#中点距离边界的长度
    pad_max = int((Smax - 1) /2)
    tempImg1 = np.pad(tempImg1, (pad_num, pad_num), mode="constant", constant_values=0)
    m, n = tempImg1.shape
    for i in range(pad_max+1, m-pad_max-1): #此处加Smax减Smax是为了防止扩大窗口尺寸造成滤波器溢出图像
        for j in range(pad_max+1, n-pad_max-1):
            tempImg1[i,j] = A(filter_size,Smax,tempImg2, i, j)
    return tempImg1

# A过程
def A(filter_size,Smax,tempImg2,x,y):
    ans = 0
    while(filter_size <= Smax):
        pad_num = int((filter_size-1)/2)
        data_matrix = tempImg2[x-pad_num:x+pad_num+1, y-pad_num:y+pad_num+1]
        A1 = np.median(data_matrix)-np.min(data_matrix)
        A2 = np.median(data_matrix)-np.max(data_matrix)
        if(A1 > 0 and A2 < 0):
            return B(data_matrix, pad_num, pad_num)
        else:
            filter_size = filter_size + 2
            ans = np.median(data_matrix)
    return ans




# B过程
def B(data_matrix,x,y):
    B1 = data_matrix[x,y] - np.min(data_matrix) # B1 = Zxy-min
    B2 = data_matrix[x,y] - np.max(data_matrix) # B2 = Zxy-max
    if(B1>0 and B2<0):
        return data_matrix[x,y]
    else:
        return np.median(data_matrix)


img = cv2.imread("PepperAndSalt/reinforce_saltAndPepper.jpg",0)#重度盐噪声图片
newImg = autoMedianFilter(img, 3,7)
newImg = autoMedianFilter(newImg, 3,7)
newImg = autoMedianFilter(newImg, 3,7)
newImg = autoMedianFilter(newImg, 3,7)

cv2.imwrite("autoMedianFilter/reinforce_autoMedianFilter.jpg",newImg)