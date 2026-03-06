import numpy as np
import cv2 
import time 
def Calculte_time(str):

 image=cv2.imread(str,cv2.IMREAD_GRAYSCALE)#reading the image as a matrix
 if image is None:
    print("Error:Image not found")
 h,w=image.shape#to know the shape of the image
 start=time.time()
 edge_x=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
 edge_y=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
 image_Final=np.hypot(edge_x,edge_y)
 image_Final=np.uint8(image_Final*255/np.max(image_Final))
 end=time.time()
 print(f"the image is of the shape {h} and {w}")
 print(f"the time to process the image is {end-start} sec")
 cv2.imwrite('edge_'+str,image_Final)

Calculte_time('test1.jpg')
Calculte_time('test2.jpg')
Calculte_time('test3.jpg')




