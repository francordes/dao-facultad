from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido, edad, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._documento = documento

    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, nuevo_documento):
        self._documento = nuevo_documento

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Documento: {self.documento}"
    

class Alumno(Persona): 
    def __init__(self, nombre, apellido, edad, documento, carrera, legajo):
        super().__init__(nombre, apellido, edad, documento)
        self.carrera = carrera
        self._legajo = legajo

    @property
    def legajo(self):
        return self._legajo
    
    @legajo.setter
    def legajo(self, nuevo_legajo):
        self._legajo = nuevo_legajo

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")
    
    def __str__(self):
        return f"{super().__str__()}, Carrera: {self.carrera}, Legajo: {self.legajo}"



class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, documento, sueldoBasico):
        super().__init__(nombre, apellido, edad, documento)
        self.sueldoBasico = sueldoBasico

    def __str__(self):
        return f"{super().__str__()}, Sueldo Básico: {self.sueldoBasico}"

    









joseMenso = Alumno("Josefina", 20, "Ingeniería en Sistemas", "409426", 46999661)
lauchaAlomar = Alumno("Lautaro", 20, "Ingeniería en Sistemas", "413917", 47179853)
franquitoCordes = Alumno("Franco", 21, "Ingeniería en Sistemas", "408867", 46222270)

print(joseMenso)
print(lauchaAlomar)
print(franquitoCordes)

joseMenso.documento = 46222270
joseMenso.legajo = 408867

print(joseMenso)