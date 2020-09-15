import cv2

image = cv2.imread('C:/Users/Nurmakhan Pazylkhan/source/repos/i.png')
cv2.imshow('Original', image)
cv2.waitKey()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()


# # Faster method 
# import cv2 
  
# # The second argument zero specifies that 
# # image is to be read in grayscale mode. 
# img = cv2.imread('C:/Users/Nurmakhan Pazylkhan/source/repos/i.png', 0)   
  
# cv2.imshow('Grayscale', img) 
# cv2.waitKey() 
  
# cv2.destroyAllWindows() 
