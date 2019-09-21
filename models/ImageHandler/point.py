from PIL import Image, ImageDraw
import cv2
import numpy as np

def point(image, x, y):
    img = Image.fromarray(image)
    dr = ImageDraw.Draw(img)
    r = 10
    dr.ellipse((x-r, y-r, x+r, y+r),'black') # x1 y1 x2 y2
    numpyImage = np.array(img)
    
    cv2.imshow("Point",numpyImage)
    cv2.waitKey()
    cv2.destroyAllWindows()