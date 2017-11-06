import cv2
import numpy as np

img1 = cv2.imread('HappyFish.jpg')
b,g,r = cv2.split(img1)

cv2.imwrite('blue_channel.jpg', b)
cv2.imwrite('green_channel.jpg', g)
cv2.imwrite('red_channel.jpg', r)

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)

# Convert BGR to HSV
hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_img)

cv2.imwrite('hue.jpg', h)
cv2.imwrite('saturation_channel.jpg', s)
cv2.imwrite('value_channel.jpg', v)

cv2.imshow('hue', h)
cv2.imshow('saturation', s)
cv2.imshow('value', v)

#Convert BGR to Ycrcb
ycrcb_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
y,cr,cb = cv2.split(ycrcb_img)

cv2.imwrite('Y.jpg', y)
cv2.imwrite('Cr.jpg', cr)
cv2.imwrite('Cb.jpg', cb)

cv2.imshow('Y', y)
cv2.imshow('Cr', cr)
cv2.imshow('Cb', cb)

cv2.waitKey(0)
cv2.destroyAllWindows()
