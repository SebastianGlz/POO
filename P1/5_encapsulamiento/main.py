import os
os.system("cls")

from coches import *

#solicitar los datos que posteriormente seran los atributos del objeto
num_coches=int(input("¿cuantos coches tienes?: "))

for i in range(0,num_coches):
    print(f"\n\t...Datos del automovil #{i+1}...")
    marca=input("ingresa la marca del auto: ").upper()
    color=input("ingresa el color: ").upper()
    modelo=input("ingresa el modelo del auto: ").upper()
    velocidad=int(input("ingresa la velocidad: "))
    potencia=int(input("ingresa la potencia del auto: "))
    plazas=int(input("ingresa las plazas: "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"\n\t\t..::Datos del Vehiculo::.. \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")