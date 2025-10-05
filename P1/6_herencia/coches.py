import os
os.system("cls")

class Coches:
#Metodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase

     def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas


     def getMarca(self):
          return self._marca
     def setMarca(self,marca):
          self._marca=marca
     def getColor(self):
          return self._color
     def setColor(self,color):
          self._color=color
     def getModelo(self):
          return self._modelo
     def setModelo(self,modelo):
          self._modelo=modelo
     def getVelocidad(self):
          return self._velocidad
     def setVelocidad(self,velocidad):
          self._velocidad=velocidad
     def getCaballaje(self):
          return self._caballaje
     def setCaballaje(self,caballaje):
          self._caballaje=caballaje
     def getPlazas(self):
          return self._plazas
     def setPlazas(self,plazas):
          self._plazas=plazas

     #Metodos o acciones o funciones que hace el objeto 

     def acelerar(self):
          return "ESTASB ACELERANDO el coche"


     def frenar(self):
          return "ESTAS FRENNDANDO el coche"  

#Fin definir clase
class Camiones(Coches):
     def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga):
          super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
          self.__eje=eje
          self.__capacidadCarga=capacidadCarga

     def cargar(self,tipo_carga):
          self.tipo_carga=tipo_carga
          return self.tipo_carga
     
     def acelerar(self):
          return "ESTASB ACELERANDO el camion"


     def frenar(self):
          return "ESTAS FRENNDANDO el camion"  
     
     @property
     def eje(self):
          return self.__eje
     
     @eje.setter
     def eje(self,eje):
          self.__eje=eje

     @property
     def capacidadCarga(self):
          return self.__capacidadCarga
     
     @capacidadCarga.setter
     def capacidadCarga(self,capacidadCarga):
          self.__capacidadCarga=capacidadCarga

class Camionetas(Coches):
     def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
          super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
          self.__traccion=traccion
          self.__cerrada=cerrada
     def transportar(self,num_pasajeros):
          self.num_pasajeros=num_pasajeros
          return self.num_pasajeros
     def acelerar(self):
          return "ESTASB ACELERANDO la camioneta"


     def frenar(self):
          return "ESTAS FRENNDANDO la camioneta"  
     
     @property
     def traccion(self):
          return self.__traccion
     
     @traccion.setter
     def traccion(self,traccion):
          self.__traccion=traccion

     @property
     def cerrada(self):
          return self.__cerrada
     
     @cerrada.setter
     def cerrada(self,cerrada):
          self.__cerrada=cerrada

          
#Crear un objetos o instanciar la clase