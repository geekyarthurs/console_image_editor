class Text:
    def __init__(self,fontSize,color,text="Hello, World!"):
        self.text = text
        self.fontSize = fontSize

        if(color == "white"):
            self.color = (255,255,255)
        elif(color == "black"):
            self.color = (0,0,0)
        elif(color=="red"):
            self.color = (255,0,0)
        else:
            self.color = (0,0,0)
        
        print("Text : {0}\nColor : {1}\nScale : {2}".format(self.text, str(self.color), self.fontSize))
            
            
        