# Steganography
This Repo contains my attempts for scripts using Steganography

# About

The main.py is currently only using one method for hiding an image "inside" an other image. It does this by flipping the least significant bit (LSB) of every 
RGB-Value of every pixel of the image you want to use, to hide the other one, whenever the LBS of the current RGB-Value of the image you want to hide is 1.

To hide text in an image, the text is first converted into a binary string. After that the LSB of the current RGB-Value is set to the current bit in the
bitstring. 

# Usage

When you execute the main.py file, you are asked to choose a mode:

  The first mode is hiding a text in the image. For that you are asked to enter the path to the image, and the text you want to hide in the image.
  
  The second mode is hiding an image inside an other image. For that you are asked to enter three paths:
    The first one is the path to the image you want to hide.
    The second one is the path to the image you want to use, to hide the first one
    The third one is the path to the "blank" image, on which the "extracted" image is displayed.
  
  
# Examples
  
I also added two images to show you the results. In this example I tried to hide image of the eagle inside the image of the sleeping cat. 

The result after extracting the eagle-image from the cat-image looks like this: ![Result](https://user-images.githubusercontent.com/95371658/202023089-6175d025-5d6c-4771-90e4-3177f45679ab.jpg)

I know it doesn't look well, but you can see the eagle. Of course the more details there are, the less they will be recognisable in the result.


Used packages: Pillow (https://python-pillow.org/)

The cat- and eagle-image are from Pixabay
