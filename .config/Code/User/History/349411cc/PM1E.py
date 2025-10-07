from PIL import Image, ImageOps
# Step 1 read image
# Step 2 convert it into greyscale 
# Step 3 split the image to mxn tiles
# Step 4 m and n depend on the aspect ratio we want
# Step 5 find the avg brightness of the tiles
# Step 6 based on step 5 give the correct ascii



def resize(w, h):
    new_w = 100
    new_h = int(h * (new_w / w) * 0.5)

    return new_w, new_h


def convert_ascii(gray_img, ascii):
    pass

ascii = [ "@", "#", "$", "%", "&", "“", "‘", "!", "?", "*", "+", "=", ":", ";",
    ">", "<", "[", "]", "{", "}", "|", "(", ")", "^", "~", "-", "_", ".", ",", "`", '"', "/"]

img = Image.open("test.jpg")
gray = ImageOps.grayscale(img)
width, height = gray.size
new_width, new_height = resize(width, height)

new_gray = gray.resize((new_width, new_height))
new_gray.show()
