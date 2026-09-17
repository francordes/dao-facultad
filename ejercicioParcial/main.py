from casa import Casa
from departamento import Departamento
from inmueble import Inmueble
from inmobiliaria import Inmobiliaria

def main():
    archivo = open("inmuebles.csv")
    inm = Inmobiliaria()
    for linea in archivo:
        datos = linea.split(",")
        tipo = int(datos[0])
        codigo = int(datos[1])
        propietario = datos[2]
        alquiler_base = float(datos[3])
        superficie = int(datos[4])

        if tipo == 1:
            dormitorios = int(datos[5])
            pileta = bool(datos[6])
            casa = Casa(codigo,propietario,superficie,alquiler_base,dormitorios,pileta)
            inm.agregar(casa)
        else:
            expensas = float(datos[5])
            piso = int(datos[6])
            depto = Departamento(codigo,propietario,superficie,alquiler_base, expensas, piso)
            inm.agregar(depto)

    archivo.close()

    print(inm.suma_alquileres())
    print(inm.cantidad_casas_premium())
    print(inm.propietario_alquiler_mas_bajo())


if __name__ == "__main__":
    main()