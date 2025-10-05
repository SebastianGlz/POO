import os
os.system("cls")

class Coches:
#Metodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase

     def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas


     def getMarca(self):
          return self.__marca
     def setMarca(self,marca):
          self.__marca=marca
     def getColor(self):
          return self.__color
     def setColor(self,color):
          self.__color=color
     def getModelo(self):
          return self.__modelo
     def setModelo(self,modelo):
          self.__modelo=modelo
     def getVelocidad(self):
          return self.__velocidad
     def setVelocidad(self,velocidad):
          self.__velocidad=velocidad
     def getCaballaje(self):
          return self.__caballaje
     def setCaballaje(self,caballaje):
          self.__caballaje=caballaje
     def getPlazas(self):
          return self.__plazas
     def setPlazas(self,plazas):
          self.__plazas=plazas

     #Metodos o acciones o funciones que hace el objeto 

     def acelerar(self):
          return "ESTASB ACELERANDO"


     def frenar(self):
          return "ESTAS FRENNDANDO"  

#Fin definir clase

#Crear un objetos o instanciar la clase