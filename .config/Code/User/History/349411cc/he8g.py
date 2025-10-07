from PIL import Image, ImageOps
# Step 1 read image
# Step 2 convert it into greyscale and also resize the image
# Step 3 create a list of things like #@,. etc and map them to greyscale values
# Step 4 finally save the new image in a text file

ascii = ["!", '"', "“", "#", "$", "%", "&", "‘", "(", ")", "*", "+", ",", "-", ".", "/",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?",
    "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_",
    "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

print(len(ascii))


img = Image.open("test.jpg")
gray = ImageOps.grayscale(img)
# gray.show()