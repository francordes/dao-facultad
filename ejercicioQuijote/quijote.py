import string

with open("quijote.txt", "r", encoding="utf-8") as archivo:
    texto_quijote = archivo.read()

with open("words_alpha.txt", "r", encoding="utf-8") as archivo:
    texto_diccionario = archivo.read()

palabras_diccionario = set(texto_diccionario.splitlines())

texto_quijote_minuscula = texto_quijote.lower()

for signo in string.punctuation:
    texto_quijote_minuscula = texto_quijote_minuscula.replace(signo, " ")

print(string.punctuation)

palabras_quijote = set(texto_quijote_minuscula.split())

print(f"Cantidad de palabras del libro sin repeticion: {len(palabras_quijote)}")
print(f"Cantidad de palabras del diccionario sin repeticion: {len(palabras_diccionario)}")

cantidad_palabras_no_en_diccionario = len(palabras_quijote - palabras_diccionario)

print(f"Cantidad de palabras del libro que no estan en el diccionario: {cantidad_palabras_no_en_diccionario}")

palabras_no_existen = sorted(palabras_quijote - palabras_diccionario)

print("Palabras del libro que no estan en el diccionario:")

for palabra in palabras_no_existen:
    print(palabra)