from PIL import Image, ImageOps
# Step 1 read image
# Step 2 convert it into greyscale and also resize the image
# Step 3 create a list of things like #@,. etc and map them to greyscale values
# Step 4 finally save the new image in a text file



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
# gray.show()


