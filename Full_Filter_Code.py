import cv2
import numpy as np

img = cv2.imread('opencv_frame_4.jpg')

width,height,channels = img.shape

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

croppedImg = grayImg[181:328, 185:622]


width,height = croppedImg.shape

scale = 1
delta = 0
ddepth = cv2.CV_16S

grad_x = cv2.Sobel(croppedImg, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

abs_grad_x = np.zeros((width,height),np.uint8 )

for col in range(width):
    for lig in range(height):
        grad_x[col,lig] = abs(grad_x[col,lig])
        if grad_x[col,lig] > 255:
            abs_grad_x[col,lig] = 255
        else:
            abs_grad_x[col,lig] = grad_x[col,lig]



grad_y = cv2.Sobel(croppedImg, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
abs_grad_y = np.zeros((width,height),np.uint8 )


for col in range(width):
    for lig in range(height):
        grad_y[col,lig] = abs(grad_y[col,lig])
        if grad_y[col,lig] > 255:
            abs_grad_y[col,lig] = 255
        else: abs_grad_y[col,lig] = grad_y[col,lig]


grad = np.zeros((width,height),np.uint8 )
grad = abs_grad_x //2 + abs_grad_y//2 # attention div entière

cv2.imshow('mon image',croppedImg)
cv2.waitKey(0)

cv2.imshow('mon image',abs_grad_x)
cv2.waitKey(0)

cv2.imshow('mon image',abs_grad_y)
cv2.waitKey(0)

cv2.imshow('mon image',grad)
cv2.waitKey(0)

cv2.destroyAllWindows()