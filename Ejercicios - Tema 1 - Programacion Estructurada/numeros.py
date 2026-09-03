# Lista de números
# Generar 1000 números enteros al azar entre -1000000 y 1000000. Investigar cómo generar los números con un flujo en lugar de un ciclo for Informar:
#   El menor de todos.
#   La cantidad de pares.
#   El promedio de los impares.
#   El cuadrado de todos los que se encuentren entre 10 y 100 sin incluirlos
#   Los múltiplos de 3 del punto anterior (los multiplos de 3 de los cuadrados calculados)
#   Todos los múltiplos de 7 ordenados en forma descendente.
#   El promedio de los impares negativos.
#   La desviación estandar de todos.
#   Si existe o no algún múltiplo de 127.
#   Generar una lista que contenga únicamente los que terminan en 2 o 3.

from random import randint
from functools import reduce

numeros = list(randint(-1000000, 1000000) for i in range(1000))

minimo = min(numeros)
print(f"El menor de todos los numeros es {minimo}")

cantPares = reduce(lambda acu, num: acu + 1 if num % 2 == 0 else acu, numeros, 0)
print(f"Cantidad de numeros pares: {cantPares}")

impares = list(filter(lambda x: x%2 != 0, numeros))
sumatoriaImpares = reduce(lambda acu, x: acu + x, impares, 0) # Tambien se puede usar sum()
promedioImpares = sumatoriaImpares / len(list(impares))
print(f"El promedio de los impares es {promedioImpares}")

entreDiezYCien = filter(lambda x: 10 < x < 100, numeros)
cuadrado = list(map(lambda x: x*x, entreDiezYCien))
print(f"Los cuadrados de los numeros entre 10 y 100 son {cuadrado}")

multiplosDe3 = filter(lambda x: x%3==0, cuadrado)
print(list(multiplosDe3))

multiplosDe7 = sorted(filter(lambda x: x%7==0, numeros),reverse=True)
print(multiplosDe7)

imparesNeg = list(filter(lambda x: x%2!=0 and x < 0, numeros))
promedio = sum(imparesNeg) / len(imparesNeg)
print(f"El promedio de los impares negativos es: {promedio}")