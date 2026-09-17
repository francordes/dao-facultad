from abc import ABC, abstractmethod

class Inmueble(ABC):
    def __init__(self, codigo, propietario, superficie, alquiler_base):
        self.codigo = codigo
        self.propietario = propietario
        self.superficie = superficie
        self.alquiler_base = alquiler_base

    @abstractmethod
    def alquiler(self):
        pass