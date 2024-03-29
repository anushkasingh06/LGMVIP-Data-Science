import cv2
image = cv2.imread("1.png")
grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)

sketch_filter = cv2.divide(grey_filter, invertedblur, scale = 256.0)
cv2.imwrite("output1.png", sketch_filter)