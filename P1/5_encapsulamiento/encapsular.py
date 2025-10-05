import os
os.system("cls")

class Clase():
    atributo_publico="soy un atributo publico"
    _atributo_protegido="soy un atributo protegido"
    __atributo_privado="soy un atributo privado"

    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self,tamanio):
        self.__tamanio=tamanio

    def getAtributoPrivado(self):
        return self.__atributo_privado
    def setAtributoPrivado(self,atributo_privado):
        self.__atributo_privado=atributo_privado

objeto=Clase("rojo","grande")
#usar los atributos y metodos de acuerdo a su encapsulamiento
print(f"mi objeto tiene las siguientes atributos: {objeto.color} y {objeto.tamanio}")


print(f"soy el contenido del atributo: {objeto.atributo_publico}")
print(f"soy el contenido del atributo: {objeto._atributo_protegido}")


objeto.setAtributoPrivado(f"cambie el contenido de {objeto.getAtributoPrivado()}")
print(f"soy el contenido del atributo: {objeto.getAtributoPrivado()}")  
