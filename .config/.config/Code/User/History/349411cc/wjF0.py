from PIL import Image, ImageOps


# Step 1 read image - done
# Step 2 convert it into greyscale - done
# Step 3 split the image to mxn tiles - done
# Step 4 m and n depend on the aspect ratio we want - done
# Step 5 find the avg brightness of the tiles
# Step 6 based on step 5 give the correct ascii

ascii = [ "@", "#", "$", "%", "&", "“", "‘", "!", "?", "*", "+", "=", ":", ";",
    ">", "<", "[", "]", "{", "}", "|", "(", ")", "^", "~", "-", "_", ".", ",", "`", '"', "/"]


# Creating tiles
def tiles(img, factor):
    width, height = img.size
    tile_width, tile_height = width * factor, height * factor

    return tile_width, tile_height


# Finding avg of tiles
def find_avg(tile_width, tile_height, img_width, img_height, img):
    gray_list = []
    for i in range(img_width, img_width + tile_width):
        for j in range(img_height, img_height + tile_height):
            pixel = img.getpixel((i, j))
            gray_list.append(pixel)
    
    avg = int(sum(gray_list) / len(gray_list))

    return avg

img = Image.open("test.jpg")

gray = ImageOps.grayscale(img)

# gray.show()

tile_width, tile_height = tiles(gray, 0.5)

