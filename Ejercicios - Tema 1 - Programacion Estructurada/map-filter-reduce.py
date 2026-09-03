# 1) Map/filter con una lista de números
#     Generar una lista con todos los números naturales entre -5 y 10 ambos inclusive. Utilizando únicamente programación funcional informar:
#     Cuadrados de todos los números de la lista
#     Todos los números negativos de la lista
#     Sumatoria de todos los números de la lista

from functools import reduce

numeros = list(range(-5,11)) # 11 porque python no incluye el limite superior
print(numeros)

numeros2 = map(lambda x: x**2,numeros)
print(list(numeros2)) # list() para verlos como lista

numeros3 = filter(lambda x: x<0,numeros)
print(list(numeros3))

sumatoria = reduce(lambda acu, x: acu + x, numeros, 0)
print(sumatoria)

# 2) Map/filter/reduce con una lista de palabras
#   Dada la siguiente lista de palabras: "Aruba","Jamaica","Bermuda","Bahama","Key Largo","Montigo"
#   Utilizando únicamente programación funcional informar:
#   Letra inicial de cada palabra
#   Longitud de cada palabra
#   Cantidad total de letras (sumando totas las palabras)

palabras = ["Aruba","Jamaica","Bermuda", "Bahama", "Key Largo", "Montigo"]

letrasInicial = map(lambda x: x[0], palabras)
print(list(letrasInicial))

longitudPalabra = map(lambda x: len(x), palabras)
print(list(longitudPalabra))

totalLetras = reduce(lambda acu, x: acu+len(x), palabras, 0)
print(totalLetras)
