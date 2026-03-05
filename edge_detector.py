import numpy as np
import cv2 
import time
image=cv2.imread('test1.jpg',cv2.IMREAD_GRAYSCALE)#reading the image as a matrix,dont know why we need the greay scale
if image is None:
    print("Error:Image not found")
h,w=image.shape#to know the shape of the image
print(f"the image is of the shape {h} and {w}")
start=time.time()
edge_x=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
edge_y=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
image_Final=np.hypot(edge_x,edge_y)
image_Final=np.uint8(image_Final*255/np.max(image_Final))
end=time.time()
toatl_time=end-start
print(f"the total time taken is {toatl_time} seconds")
cv2.imwrite('output.jpg', image_Final) 

