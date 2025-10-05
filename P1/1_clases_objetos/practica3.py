import os 
os.system("cls")

class Alumno():
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula
    def inscribirse(self):
        pass
    def estudiar(self):
        pass

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getEdad(self):
        return self.__edad
    def setEdad(self,edad):
        self.__edad=edad
    
    def getMatricula(self):
        return self.__matricula
    def setMatricula(self,matricula):
        self.__matricula=matricula

class Profesores():
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor
    def impartir(self):
        pass
    def evaluar(self):
        pass

class Cursos():
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos
    def asignar(self):
        pass

#alumnos
alumno1=Alumno("Alessandro",19,"123")
alumno2=Alumno("Uriel",19,"456")

#profesor
profesor1=Profesores("Dagoberto","SI",1)
profesor2=Profesores("Dago","SI",2)

#curso
curso1=Cursos("POO",1,100)
curso2=Cursos("BD",2,80)