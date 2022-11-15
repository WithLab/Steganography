from PIL import Image

hidden_img_path = input("Please enter the path to the image, that should be hidden: ")
original_img_path = input("Please enter the path to the image, that hides the other image: ")
blank_img_path = input("Please enter the path to the blank-image, on which the extracted image should be renderd: ")

img_hidden = Image.open(hidden_img_path).convert('RGB')
img_original = Image.open(original_img_path).convert('RGB')
img_blank = Image.open(blank_img_path).convert('RGB')

width, height = min(img_original.size, img_hidden.size)


def hide(hidden_image, original_image):

    for i in range(width):
        for j in range(height):

            rgb_hidden = list(hidden_image.getpixel((i, j)))
            rgb_original = list(original_image.getpixel((i, j)))

            mask_original = list((rgb_original[0] & 0b1, rgb_original[1] & 0b1, rgb_original[2] & 0b1))   # Check if LBS is 0 or 1
            mask_hidden = list((rgb_hidden[0] & 0b1, rgb_hidden[1] & 0b1, rgb_hidden[2] & 0b1))

            for k in range(3):
                if mask_hidden[k] == 1:    # If LBS of 'hidden' rgb value is 1, 'flip' the LBS of the original rgb value
                    rgb_original[k] = rgb_original[k] ^ 0b1

            original_image.putpixel((i, j), (rgb_original[0], rgb_original[1], rgb_original[2]))


def extract(received_image, original_image):
    for i in range(width):
        for j in range(height):

            rgb_received = received_image.getpixel((i, j))
            rgb_original = original_image.getpixel((i, j))

            if rgb_received != rgb_original:    # If there is a difference between the original and received LBSs, change pixel in blank
                img_blank.putpixel((i, j), (0, 0, 0))   # TODO: The different pixels are set to (0,0,0) [Black]. If you want other colors, edit the (0, 0, 0)-Tuple in this line


hide(img_hidden, img_original)
img_original.show()
img_original.save("Stealth_image.jpg")
extract(img_original, Image.open(original_img_path))
img_blank.show()
img_blank.save("Result.jpg")
