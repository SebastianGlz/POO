import os
os.system("cls")

class Coches:
#Metodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase

     def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.marca=marca
        self.color=color
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas


     def getMarca(self):
          return self.marca
     def setMarca(self,marca):
          self.marca=marca
     def getColor(self):
          return self.color
     def setColor(self,color):
          self.color=color
     def getModelo(self):
          return self.modelo
     def setModelo(self,modelo):
          self.modelo=modelo
     def getVelocidad(self):
          return self.velocidad
     def setVelocidad(self,velocidad):
          self.velocidad=velocidad
     def getCaballaje(self):
          return self.caballaje
     def setCaballaje(self,caballaje):
          self.caballaje=caballaje
     def getPlazas(self):
          return self.plazas
     def setPlazas(self,plazas):
          self.plazas=plazas

     #Metodos o acciones o funciones que hace el objeto 

     def acelerar(self):
          pass


     def frenar(self):
          pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches("VW","BLANCO","2022",220,150,5)
coche2=Coches("NISSAN","AZUL","2020",180,150,6)
coche3=Coches("HONDA","","",0,0,0)






print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")
print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")
print(coche3.getMarca())