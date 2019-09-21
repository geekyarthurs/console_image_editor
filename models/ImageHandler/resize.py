 
import cv2
 
def resize(image,resizeOptions):
    pass



def scaledResize(image,resizePercent):
    scale_percent = resizePercent
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized


def sized_resize(image,width,height):
    
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
    return resized

