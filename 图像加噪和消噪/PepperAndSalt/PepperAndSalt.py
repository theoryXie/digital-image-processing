import numpy as np
import cv2
import random
import matplotlib.pyplot as plt

'''
    添加椒噪声或盐噪声
    img -- 需要添加噪声的图像
    percetage -- 添加噪声的比例
    type -- 0为盐噪声
            1为椒噪声
            2为椒盐噪声
'''
def addPepperOrSalt(img, percetage, type=0):
    rows = img.shape[0]
    cols = img.shape[1]
    noiseImg = img.copy()
    num = int(percetage * rows * cols) #添加噪声的数量
    #盐噪声
    if(type == 0):
        for i in range(num):
            randX = random.randint(0, rows-1)
            randY = random.randint(0, cols-1)
            noiseImg[randX, randY] = 255
    #椒噪声
    elif (type == 1) :
        for i in range(num):
            randX = random.randint(0, rows-1)
            randY = random.randint(0, cols-1)
            noiseImg[randX, randY] = 0
    #椒盐噪声
    elif (type == 2):
        for i in range(num):
            randX = random.randint(0, rows-1)
            randY = random.randint(0, cols-1)
            temp = random.random()
            if(temp>0.5):
                noiseImg[randX, randY] = 0
            else:
                noiseImg[randX,randY] = 255
    return noiseImg



img = cv2.imread("gray.jpg",0) #单通道！
noiseImg = addPepperOrSalt(img,0.1,0) #添加盐噪声
cv2.imwrite("PepperAndSalt/salt.jpg",noiseImg)
# plt.imshow(noiseImg, cmap='gray')#plt的imshow会自动弄成三通道，所以要加cmap='gray'
# plt.show()

noiseImg = addPepperOrSalt(img,0.1,1)#添加椒噪声
# plt.imshow(noiseImg, cmap='gray')#plt的imshow会自动弄成三通道，所以要加cmap='gray'
# plt.show()
cv2.imwrite("PepperAndSalt/pepper.jpg",noiseImg)

noiseImg = addPepperOrSalt(img,0.05,2)#添加椒盐噪声
# plt.imshow(noiseImg, cmap='gray')#plt的imshow会自动弄成三通道，所以要加cmap='gray'
# plt.show()
cv2.imwrite("PepperAndSalt/saltAndPepper.jpg",noiseImg)


noiseImg = addPepperOrSalt(img,0.5,2)#添加重度椒盐噪声
# plt.imshow(noiseImg, cmap='gray')#plt的imshow会自动弄成三通道，所以要加cmap='gray'
# plt.show()
cv2.imwrite("PepperAndSalt/reinforce_SaltAndPepper.jpg",noiseImg)