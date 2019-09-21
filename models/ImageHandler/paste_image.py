from PIL import Image
import numpy as np


def pasteImage(image, image_to_paste, area):
    im1 = Image.fromarray(image)
    im2 = Image.fromarray(image_to_paste)
    im1.paste(im2, area)

    return np.array(im1)
