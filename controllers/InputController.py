from init import *
from models.Images.Image import Image
from models.Images.Text import Text
from models.ImageHandler.point import point
class InputController:

    def __init__(self, image):

        self.modelImage = Image(image)

        self.filename = image
        self.text = None

    def processInput(self, msg):
        if(msg.strip()[:4] == "save"):
            self.modelImage.save(msg.strip()[4:])
        if(msg.strip()[:5] == "exit " or msg.strip()[:6] == "close " or msg.strip()[:5] == "quit "):
            ColorPrint().print_warn(messages["exit-message"])
            exit()
        if(msg.strip()[:1] == "!"):
            os.system(msg.strip()[1:])

        if(msg.strip() == "show"):

            self.modelImage.show()

        if(msg.strip() == "size"):
            print("Width : {}px\nHeight : {}px".format(
                self.modelImage.size()[0], self.modelImage.size()[1]))
        if(msg.strip() == "filter bw"):
            try:
                self.modelImage.filter(123)
                ColorPrint().print_pass("Converted into Black and White Image")
            except:
                ColorPrint().print_fail("Image is already Black And White!")

        if(msg.strip()[:4] == "crop"):  # crop 300 300 400 400

            self.modelImage.crop(msg.strip()[5:])

        if(len(msg.strip().split()) == 2 and msg.strip().split()[0] == "change"):
            self.changeImage(msg.strip().split()[1])

        if(msg.strip()[:6] == "rotate"):
             self.modelImage.rotate(msg.strip()[7:].split())
        if(msg.strip() == "reset"):
            self.modelImage.reset()

        if(msg.strip()[:4] == "text"): #text 10-abcd
            rawText = msg.strip()[5:].split("-")
            self.text = Text(fontSize=int(rawText[0]),color=rawText[2],text=rawText[1])
        if(msg.strip()[:5] == "point"):
              dimensions = msg.strip()[6:].split() # point 12 12
              if(len(dimensions) == 2):
                    x = int(dimensions[0])
                    print(x)
                    y = int(dimensions[1])
                    print(y)
                    point(self.modelImage.image,x,y)

        
        if(self.text is not None):
            if(msg.strip()[:5] == "write"): #write 100 100 
                dimensions = msg.strip()[6:].split()
                if(len(dimensions) == 2):
                    width = int(dimensions[0])
                    height = int(dimensions[1])
                    self.modelImage.addText(self.text,width,height)
                    ColorPrint().print_pass("Succesfully Written !")
            if(msg.strip()[:6] == "textc"):
                 pass



    def getInput(self):  # getting input

        command = input("({})$".format(self.filename))
        self.processInput(command)

    def changeImage(self, filename):  # change image
        self.modelImage = Image(filename)
        self.filename = filename
