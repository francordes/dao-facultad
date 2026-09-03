from POO import *

per1 = Persona(1234, "Juan", "Perez", 12)
per2 = Persona(46222270, "Franco", "Cordes", 21) # Establece un puntero hacia el objeto, no guarda los atributos del objeto
per3 = Persona(24615456, "Guillermo", "Cordes", 51)

print(per2.nombre_completo())
print(per2.mayor_edad())
print(per2.nombre)
print(per1)
print(per3)