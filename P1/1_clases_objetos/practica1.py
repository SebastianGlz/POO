#PROGRAMACION ESTRUCTURADA
def rectangulo(base,altura):
    return base*altura

print(rectangulo(5,3))

#PROGRAMACION ORIENTADA A OBJETOS
class Rectangulos():
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base*self.altura
    
rect=Rectangulos(5,3)
print(rect.area())