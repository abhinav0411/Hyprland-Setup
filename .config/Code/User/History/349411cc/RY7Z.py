from PIL import Image, ImageOps


# Step 1 read image - done
# Step 2 convert it into greyscale - done
# Step 3 split the image to mxn tiles
# Step 4 m and n depend on the aspect ratio we want
# Step 5 find the avg brightness of the tiles
# Step 6 based on step 5 give the correct ascii

ascii = [ "@", "#", "$", "%", "&", "“", "‘", "!", "?", "*", "+", "=", ":", ";",
    ">", "<", "[", "]", "{", "}", "|", "(", ")", "^", "~", "-", "_", ".", ",", "`", '"', "/"]


def tiles(img, factor):
    width, height = img.size
    tile_width, tile_height = width * factor, new_height * factor

    return tile_width, tile_height

img = Image.open("test.jpg")

gray = ImageOps.grayscale(img)

# gray.show()

tile_width, tile_height = tiles(gray, 0.5)