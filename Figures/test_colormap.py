import cv2;
import numpy as np;

I=cv2.imread('144_10_ml.png',-1);

gamma = 0.7
I = I/255.0
I = cv2.pow(I,gamma)

#I = (I+1)/1.0;
#I = 2/I;

#COLORMAP_JET COLORMAP_HSV
J=cv2.applyColorMap(I,cv2.COLORMAP_BONE)
cv2.imshow('tada',J);
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('144_10_ml2.png',J*255);
