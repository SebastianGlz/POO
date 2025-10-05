"""
Ejercicio práctico #2: "Modelar y Diagramar en POO"

"""
import os
os.system("cls")

#Crear una clase
class Coches:
    #Método constructor que inicaliza los valores de los atributos cuando 
    # se instancie un objeto de la clase

    def __init__ (self,color,marca,velocidad):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        color=self.__color
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,marca):
        marca=self.__marca
    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self,velocidad):
        velocidad=self.__velocidad
        

    def acelerar(self,incremento):
        return self.__velocidad+incremento

    def frenar(self,decremento):
        return self.__velocidad-decremento
    
    def tocar_claxon(self):
        return "PIIII"
    
#Instanciar objetos de la clase Coches

coche1=Coches("rojo","toyota",120)
coche2=Coches("amarillo","nissan",180)

print(f"los valores del objeto 1 son: {coche1.color}, {coche1.marca}, {coche1.velocidad}")
print(f"la velocidad original del coche 1 es: {coche1.velocidad} y cambio a: {coche1.acelerar(50)}")
print(f"los valores del objeto 2 son: {coche2.color}, {coche2.marca}, {coche2.velocidad}")
print(f"la velocidad original del coche 1 es: {coche1.velocidad} y cambio a: {coche1.frenar(100)}")
