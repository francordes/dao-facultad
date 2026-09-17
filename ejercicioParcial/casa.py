from inmueble import Inmueble

class Casa(Inmueble):
    
    def __init__(self, codigo, propietario, superficie, alquiler_base, dormitorios, pileta):
        super().__init__(codigo, propietario, superficie, alquiler_base)
        self.dormitorios = dormitorios
        self.pileta = pileta

    def alquiler(self):
        importe_dormitorios = self.dormitorios * 30000
        importe_pileta = 0
        if self.pileta: importe_pileta = 100000

        importe = self.alquiler_base + importe_dormitorios + importe_pileta
        return importe
        

