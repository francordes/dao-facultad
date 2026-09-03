class Ascensor:
    def __init__(self, cantidadPersonas, numeroPiso, cantMaxima):
        self.cantidadPersonas = cantidadPersonas
        self.numeroPiso = numeroPiso
        self.cantMaxima = cantMaxima
        self.pisoMaximo = 20
        self.pisoMinimo = -1
    def subirPersona(self, cantSuben):
        if (self.cantidadPersonas + cantSuben <= self.cantMaxima) and cantSuben >= 1:
            self.cantidadPersonas += cantSuben
            return f"Se subieron {cantSuben} personas correctamente"
        else:
            return f"No se puede subir a esa cantidad de gente, la cantidad maxima es de {self.cantMaxima} y hay subidas {self.cantidadPersonas}"
    def bajarPersona(self, cantBajan):
        if (self.cantidadPersonas >= cantBajan) and cantBajan >= 1:
            self.cantidadPersonas -= cantBajan
            return f"Se bajaron {cantBajan} personas correctamente"
        else:
            return f"No se pueden bajar esa cantidad de personas, en el ascensor solo hay subidas {self.cantidadPersonas} personas"
    def subirPiso(self):
        if self.pisoMaximo >= self.numeroPiso + 1:
            self.numeroPiso += 1
            return f"Se subió de piso correctamente, el piso actual es el {self.numeroPiso}"
        else:
            return f"No se puede subir mas pisos. El piso actual es el {self.numeroPiso}"
    def bajarPiso(self):
        if self.pisoMinimo <= self.numeroPiso - 1:
            self.numeroPiso -= 1
            return f"Se bajó de piso correctamente, el piso actual es el {self.numeroPiso}"
        else:
            return f"No se puede bajar mas pisos. El piso actual es el {self.numeroPiso}"
    def __str__(self):
        return f"Cantidad de personas subidas: {self.cantidadPersonas} | Piso actual: {self.numeroPiso} | Cantidad maxima de personas: {self.cantMaxima}"

ascensor1 = Ascensor(0, 0, 20)
print(ascensor1.subirPersona(2))
print(ascensor1)
print(ascensor1.subirPiso())
print(ascensor1)
print(ascensor1.bajarPiso())