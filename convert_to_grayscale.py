import cv2
image = cv2.imread('california_3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original image',image)
cv2.imwrite('Gray_image_2.png', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
