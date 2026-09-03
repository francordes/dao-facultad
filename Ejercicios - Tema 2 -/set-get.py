class Persona:
    def __init__(self, documento, nombre, apellido, edad):
        self._documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, nuevo_documento):
        self._documento = nuevo_documento

persona1 = Persona(46222270, "Franco", "Cordes", 21)
print(persona1.documento)  # Acceder al documento usando el getter
persona1.documento = 46222271
print(persona1.documento)  # Acceder al documento usando el getter después de modificarlo



