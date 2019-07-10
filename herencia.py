class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def hola(self):
        print(self.nombre,self.apellido)

class Estudiante(Persona):
    def __init__(self,nombre,apellido,edad):
        Persona.__init__(self,nombre,apellido)
        self.edad = edad
    def hola(self):
        print(self.nombre,self.apellido,self.edad)
        
