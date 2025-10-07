from PIL import Image, ImageOps


# Step 1 read image
# Step 2 convert it into greyscale 
# Step 3 split the image to mxn tiles
# Step 4 m and n depend on the aspect ratio we want
# Step 5 find the avg brightness of the tiles
# Step 6 based on step 5 give the correct ascii

ascii = [ "@", "#", "$", "%", "&", "“", "‘", "!", "?", "*", "+", "=", ":", ";",
    ">", "<", "[", "]", "{", "}", "|", "(", ")", "^", "~", "-", "_", ".", ",", "`", '"', "/"]


img = Image.open("test.jpg")

gray = ImageOps.grayscale(img)

gray.show