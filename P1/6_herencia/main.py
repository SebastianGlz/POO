from coches import *

#Solicitar los datos que posteriormente seran los atributos del objeto

#numm_coches=int(input("Cuantos vehiculos desea ingresar: "))

"""for i in range(0, numm_coches):
    print(f"\n\t . . . Datos del Vehiculo #{i+1} . . . ")
    marca=input("Ingresar la marca: ").upper()
    color=input("Ingresar el color: ").upper()
    modelo=input("Ingresar el modelo: ").upper()
    velocidad=int(input("Ingresar la velocidad: "))
    caballaje=int(input("Ingresar el caballaje: "))
    plazas=int(input("Ingresar el numero de plazas: "))

    coche1=Coches(marca, color, modelo, velocidad, caballaje, plazas)


    print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")
"""
coche=Coches("VW","BLANCO","2020",220,180,4)
print(coche.getColor(),coche.acelerar())

camion=Camiones("VW","BLANCO APERLADO","2020",220,180,4,2,2500)
print(camion.getColor(),camion.acelerar())

camioneta=Camionetas("VW","AZUL","2020",220,180,4,"DELANTERA",True)
print(camioneta.getColor(),camioneta.acelerar())
