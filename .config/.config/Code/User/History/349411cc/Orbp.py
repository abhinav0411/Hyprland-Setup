import cv2
# Step 1 read image
# Step 2 convert it into greyscale and also resize the image
# Step 3 create a list of things like #@,. etc and map them to greyscale values
# Step 4 finally save the new image in a text file

img = cv2.imread("test.jpg")

cv2.COLOR_RGB2GRAY(img)

