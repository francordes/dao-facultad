from inmueble import Inmueble

class Departamento(Inmueble):
    
    def __init__(self, codigo, propietario, superficie, alquiler_base, expensas, piso):
        super().__init__(codigo, propietario, superficie, alquiler_base)
        self.expensas = expensas
        self.piso = piso

    def alquiler(self):
        importe_piso = 0
        if self.piso < 3:
            importe_piso = 20000

        importe = self.alquiler_base + self.expensas + importe_piso
        return importe
        