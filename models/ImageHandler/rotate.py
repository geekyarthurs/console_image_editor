import cv2
import imutils
from models.Utils.ColorPrint import ColorPrint


def rotate(image, rotationType):
    if(len(rotationType) == 1):
        degreeToRotate = abs(int(rotationType[0]))
        rotatedImage = imutils.rotate_bound(image, degreeToRotate)
        ColorPrint().print_pass("Succesfully rotated the image by {}".format(degreeToRotate))
        return rotatedImage
    if(len(rotationType) == 2):
        degreeToRotate = abs(int(rotationType[0]))
        if rotationType[1] == "c" or rotationType[1] == "clockwise":
            rotatedImage = imutils.rotate_bound(image, degreeToRotate)
            ColorPrint().print_pass("Succesfully rotated the image clockwise by {}".format(degreeToRotate))
            return rotatedImage
        elif rotationType[1] == "ac" or rotationType[1] == "anti-clockwise":
            rotatedImage = imutils.rotate_bound(image, 0 - degreeToRotate)
            ColorPrint().print_pass("Succesfully rotated the image anti-clockwise by {}".format(degreeToRotate))
            return rotatedImage

    else:
        ColorPrint().print_fail("Invalid Options provided to rotate the image.")
