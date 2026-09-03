class Persona:
    def __init__(self, documento, nombre, apellido, edad):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    def mayor_edad(self):
        return self.edad >= 18
    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Documento: {self.documento} | Edad: {self.edad}"