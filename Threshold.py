import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

def main():

    img = cv2.imread("HappyFish.jpg")

    cv2.imshow('Untampered', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_type = 2
    threshold_value = 128
    ret,dst = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_TRUNC)
    cv2.imshow("Thresholded Image",dst)
    cv2.imwrite('thresholded.jpg', dst)

    current_threshold = 128
    max_threshold = 255
    ret,threshold = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY)
    cv2.imshow("Binary threshold",threshold)
    cv2.imwrite('binary_thresholded.jpg', threshold)

    threshold1 = 27
    threshold2 = 125
    ret, binary_image1 = cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY)
    ret, binary_image2 = cv2.threshold(gray, threshold2, max_threshold, cv2.THRESH_BINARY_INV)
    band_thresholded_image = np.bitwise_and(binary_image1, binary_image2)
    cv2.imshow("Band Thresholding", band_thresholded_image)
    cv2.imwrite('band_thresholded.jpg', band_thresholded_image)

    ret,semi_thresholded_image = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    semi_thresholded_image = np.bitwise_and( gray, semi_thresholded_image)
    cv2.imshow("Semi Thresholding",semi_thresholded_image )
    cv2.imwrite('semi_thresholded.png',semi_thresholded_image)

    adaptive_thresh = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 )
    cv2.imshow("Adaptive Thresholding",adaptive_thresh)
    cv2.imwrite('adaptive_thresholded.png', adaptive_thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
