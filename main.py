from PIL import Image

mode = input("Please enter 'T' if you want to hide a text in an image, or 'I' if you want to hide an image in an image: ")

original_img_path = input("Please enter the path to the image, that hides the other image: ")
img_original = Image.open(original_img_path).convert('RGB')

if mode == 'I':
    hidden_img_path = input("Please enter the path to the image, that should be hidden: ")
    blank_img_path = input("Please enter the path to the blank-image, on which the extracted image should be renderd: ")

    img_hidden = Image.open(hidden_img_path).convert('RGB')
    img_blank = Image.open(blank_img_path).convert('RGB')

elif mode == 'T':
    hidden_text = input("Please enter your secret text: ")

width, height = min(img_original.size, img_original.size)


def hide_img(hidden_image, original_image):

    for i in range(width):
        for j in range(height):

            rgb_hidden = list(hidden_image.getpixel((i, j)))
            rgb_original = list(original_image.getpixel((i, j)))

            mask_original = list((rgb_original[0] & 0b1, rgb_original[1] & 0b1, rgb_original[2] & 0b1))   # Check if LSB is 0 or 1
            mask_hidden = list((rgb_hidden[0] & 0b1, rgb_hidden[1] & 0b1, rgb_hidden[2] & 0b1))

            for k in range(3):
                if mask_hidden[k] == 1:    # If LBS of 'hidden' rgb value is 1, 'flip' the LSB of the original rgb value
                    rgb_original[k] = rgb_original[k] ^ 0b1

            original_image.putpixel((i, j), (rgb_original[0], rgb_original[1], rgb_original[2]))


def extract_img(received_image, original_image):
    for i in range(width):
        for j in range(height):

            rgb_received = received_image.getpixel((i, j))
            rgb_original = original_image.getpixel((i, j))

            if rgb_received != rgb_original:    # If there is a difference between the original and received LSBs, change pixel in blank
                img_blank.putpixel((i, j), (0, 0, 0))   # TODO: The different pixels are set to (0,0,0) [Black]. If you want other colors, edit the (0, 0, 0)-Tuple in this line



def hide_text(text, original_image):

    counter = 0
    bin_text = ''.join(format(ord(i), '08b') for i in text) #Convert text into binary string

    for i in range(width):
        for j in range(height):

            rgb_original = list(original_image.getpixel((i, j)))

            for k in range(3):
                if counter < len(bin_text):
                    if int(bin_text[counter]) == 1: #Change LSB of current RGB-Value to the current bit of the bit string
                        rgb_original[k] = rgb_original[k] | 1
                    elif int(bin_text[counter]) == 0:
                        if rgb_original[k] & 1 == 1:
                            rgb_original[k] = rgb_original[k] ^ 1

                    counter += 1

            original_image.putpixel((i, j), (rgb_original[0], rgb_original[1], rgb_original[2]))

def extract_text(received_image):
    
    text_bin = ''

    for i in range(width):
        for j in range(height):

            rgb_original = list(received_image.getpixel((i, j)))
            for k in range(3):
                text_bin = text_bin + str(int(rgb_original[k] & 0b1))   #Extract LSB of the current RGB-Value and add it to binary string

    text_length = 800   #TODO: A length of 800 means, that the first 800 bits of the binarystring are interpreted as ASCII code, so change this value if your text is longer than 100 chars
    text = ""

    for s in range(0, text_length, 8):    #Convert every byte (8 bits) into its decimal and from there to its ASCII character and add it to the plain string
        c = chr(int(text_bin[s:s+8], 2))  
        text = text + c
    print(text)
