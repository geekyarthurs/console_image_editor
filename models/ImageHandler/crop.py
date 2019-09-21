import cv2
from models.Utils.ColorPrint import ColorPrint


def crop(image, w, h, x=0, y=0):
    try:

        image = image[x:x+w, y:y+h]
        ColorPrint().print_pass("Succesfully Cropped Image")
        return image

    except(IndexError):
        ColorPrint().print_fail(
            "Your new dimensions is more than the image's dimensions. Failed to Crop")
        return image
