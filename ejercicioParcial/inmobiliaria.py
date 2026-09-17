from departamento import Departamento
from casa import Casa
from inmueble import Inmueble

class Inmobiliaria():
    def __init__(self):
        self.inmuebles = []

    def agregar(self, inmueble):
        self.inmuebles.append(inmueble)

    def suma_alquileres(self):

        return sum(list(map(lambda i: i.alquiler(),self.inmuebles))) #Una manera

        # Otra manera
        acumulador = 0
        for inmueble in self.inmuebles:
            acumulador += inmueble.alquiler()

        return acumulador

    def cantidad_casas_premium(self):
        c = 0
        for inmueble in self.inmuebles:
            if isinstance(inmueble, Casa) and inmueble.superficie > 150 and inmueble.dormitorios > 2 and inmueble.pileta:
                c += 1
        return c

    def propietario_alquiler_mas_bajo(self):
        menor = None
        for inmueble in self.inmuebles:
            if isinstance(inmueble, Departamento):
                if menor is None or inmueble.alquiler() < menor.alquiler():
                    menor = inmueble
        if menor is None:
            return None
        return menor.propietario