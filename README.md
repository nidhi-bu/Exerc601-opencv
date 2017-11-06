# Exerc601-opencv
assignment for opencv - EC601

4.1 EXERCISE 1
  1) The cvMat object is read in the order of row and then coloumn. This implies that when acessing pixels, the y coordinate is read first and then the x coordinate. (y,x)

5.1 EXERCISE 2
  1) The output of ColorImage.cpp is: 
     (i) The conversion of colorspaces between BGR to YCrCb and from BGR to HSV using cvtColor and CV_BGR2YCrCb.
     (ii) After conversion the program splits the converted image to its components or channels using Mat vector input_planes. The BGR image is split into Blue, Red and Green components. The YcrCb image is split into Y(luminance) and Cr and Cb (the chrominance values). The HSV image is split into its Hue, Saturation and Value images.
     (iii) The converted images are stored as Mat objects and displayed separately.
