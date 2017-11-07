# Exerc601-opencv
assignment for opencv - EC601

4.1 EXERCISE 1
  1) The cvMat object is read in the order of row and then coloumn. This implies that when acessing pixels, the y coordinate is read first and then the x coordinate. (y,x)
  
   | Blue 				| Green 			  	| Red 				|
|:-----------------:|:---------------------:|:-----------------:|
| ![blue](/ColorImages-saved/blue_channel.jpg) | ![green](/ColorImages-saved/green_channel.jpg) 	| ![red](/ColorImages-saved/red_channel.jpg) 	|

| Y 				| Cb 			  		| Cr 				|
|:-----------------:|:---------------------:|:-----------------:|
| ![y](/ColorImages-saved/Y.jpg) 		| ![cb](/ColorImages-saved/Cb.jpg) 		| ![cr](/ColorImages-saved/Cr.jpg) 	|

| Hue 				| Saturation 			| Value 			|
|:-----------------:|:---------------------:|:-----------------:|
| ![hue](/ColorImages-saved/hue.jpg) | ![sat](/ColorImages-saved/saturation_channel.jpg)  | ![val](/ColorImages-saved/value_channel.jpg) |
  

5.1 EXERCISE 2
  1) The output of ColorImage.cpp is: 
     (i) The conversion of colorspaces between BGR to YCrCb and from BGR to HSV using cvtColor and CV_BGR2YCrCb.
     (ii) After conversion the program splits the converted image to its components or channels using Mat vector input_planes. The BGR image is split into Blue, Red and Green components. The YcrCb image is split into Y(luminance) and Cr and Cb (the chrominance values). The HSV image is split into its Hue, Saturation and Value images.
     (iii) The converted images are stored as Mat objects and displayed separately.
 2) [248 255 255]  -  BGR
 
    [ 30   7 255]  -  HSV
 
    [ 30   7 255]  -  YCrCb
    
 
 6.1 EXERCISE 3
   1) On running the program, the values of noise for different mean, sigma values and pa, pb values will get printed. 
   2) As the size of the kernel increases, the 'blur' of the image also increases. Thus, smaller kernel gives lower error.
   --> Based on the output images, we can see that the median filter works best for images with Gaussian noise. the median filter also works better for images with salt and pepper noise. 
   
   
 7.1 EXERCISE 4
   1) Observing the output images for the different threshold types, we see that Adaptive Thresholding conserves the maximum amount of data from the original image. Semi Threshold looses most data from the original representation. The order of performance in respect of conserving most data of the original is Adaptive > Binary > Band > Semi
   2) Though binary thresholding the next in terms of preserving original image information, it lacks in preserving the small changes in pixel values and thus leads to over darkening of certain regions. 
   3) Adaptive thresholding is useful when the pixel value changes of neighbouring pixels are very small and there are chances that such small changes will be lost with ordinary thresholding. In such cases Adaptive threshold can be used and manipulated to retain the most amount of information of the original image and give as accurate a representation of the image as possible.
   
