
import numpy as np
import cv2
def addText(image,Text,width,height):
    cv2.putText(image,Text.text, (width,height), cv2.FONT_HERSHEY_SIMPLEX, Text.fontSize, Text.color, thickness=Text.fontSize)
    return image

