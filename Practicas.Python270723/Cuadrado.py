# 

class Cuadrado:
    
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight 
        
    def valores(self):
        txt = "El cuadrado tiene una altura de: {} y una altura de: {}"
        print (txt.format(self.height,self.weight))  
      
    def perimetro(self):
        print ("El perimetro es {perimetro}".format(perimetro = (2*self.height + 2*self.weight)))
  
    def area(self):
        print ("El area es {area}".format(area = (self.height * self.weight)))
    

cdr = Cuadrado(20,30)
cdr.valores()
cdr.perimetro()
cdr.area()