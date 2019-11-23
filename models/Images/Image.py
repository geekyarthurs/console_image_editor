import cv2
from init import *
from models.ImageHandler.crop import crop
from models.ImageHandler.rotate import rotate
from models.ImageHandler.addText import addText

class Image:
    def __init__(self, filename):
        self.image = cv2.imread(filename)
        self.filename = filename
        if self.image is None:
            ColorPrint().print_fail(error_messages["invalid-image"])
            exit()

    def crop(self, dimensions):
        dimensions = dimensions.split()
        
        if len(dimensions) == 2:
            self.image = crop(image=self.image, w=int(
                dimensions[0]), h=int(dimensions[1]))
        elif len(dimensions) == 4:
            self.image = crop(image=self.image, x=int(dimensions[0]), y=int(
                dimensions[1]), w=int(dimensions[2]), h=int(dimensions[3]))
        else:
            ColorPrint().print_fail("Please provide 2 or 4 dimensions to crop image.")

    def rotate(self, rotationType):
        self.image = rotate(self.image, rotationType)

    def size(self):
        return (self.image.shape[0], self.image.shape[1])

    def show(self):
        cv2.imshow(self.filename, self.image)
        key=cv2.waitKey(0) & 0xFF
        if key==27:
            cv2.destroyAllWindows()
      
        
    def filter(self, type):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def addText(self,Text,width,height):
       self.image =  addText(self.image,Text,width,height)

    def save(self, filename):
        try:
            extension = self.filename.split(".")[1]
            cv2.imwrite(filename + "." + extension, self.image)
            ColorPrint().print_pass("Succesfully saved the image.")
        except:
            ColorPrint().print_fail("Failed to save your image.")

    def reset(self):

        self.image = cv2.imread(self.filename)
        ColorPrint().print_pass("Succesfully reset the image.")
