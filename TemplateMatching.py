import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0
    var_t = 0
    location = [0, 0]
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------

    #rows, columns = temp.shape
    mean_t = np.mean(temp)
    var_t = np.var(temp)

    numerator = 0
    max_corr = 0
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0
            var_s = 0
            corr = 0
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------
            mean_s = np.mean(src[i:i+temp.shape[0],j:j+temp.shape[1]])
            var_s = np.var(src[i:i+temp.shape[0],j:j+temp.shape[1]])

            window = src[i:i + temp.shape[0], j:j + temp.shape[1]]

            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------
            denominator = (temp.shape[0]*temp.shape[1]*var_t*var_s)
            for k in range(0, temp.shape[0]):
                for l in range(0, temp.shape[1]):
                    corr += ((window[k,l] - mean_s)*(temp[k,l] - mean_t))
            corr = corr/denominator

            if corr > max_corr:
                max_corr = corr
                location = [i, j]
    print(max_corr)
    return location

# load source and template images
source = cv2.imread('source_img.jpg')
source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
temp_color = cv2.imread('template.jpg')
temp = cv2.imread('template.jpg',0) # read image in grayscale
location = TemplateMatching(source_img, temp, 20)
print(location)
x , y = location
#match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------
cv2.rectangle(source,(y,x),(y+temp.shape[1],x+temp.shape[0]),(0,255,0),2)

# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------
cv2.imwrite('matched.jpg', source)
cv2.imshow('matched', source)


# Display the template image and the matching result
#cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
#cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp_color)
#cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
