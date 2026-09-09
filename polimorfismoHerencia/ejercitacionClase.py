class Empleado:
    def __init__(self, nombre, apellido, edad, documento, sueldoBasico):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._documento = documento
        self.sueldoBasico = sueldoBasico
    
    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, nuevo_documento):
        self._documento = nuevo_documento
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Documento: {self.documento}, Sueldo Básico: {self.sueldoBasico}"
    

class Obrero(Empleado):
    def __init__(self, nombre, apellido, edad, documento, sueldoBasico, diasTrabajados):
        super().__init__(nombre, apellido, edad, documento, sueldoBasico)
        self.diasTrabajados = diasTrabajados

    def __str__(self):
        return f"{super().__str__()}, Días Trabajados: {self.diasTrabajados}"
    
    @property
    def calcularSueldo(self):
        return (self.sueldoBasico / 20) * self.diasTrabajados

class Administrativo(Empleado):
    def __init__(self, nombre, apellido, edad, documento, sueldoBasico, tienePresentismo):
        super().__init__(nombre, apellido, edad, documento, sueldoBasico)
        self.tienePresentismo = tienePresentismo

    def __str__(self):
        return f"{super().__str__()}, Tiene Presentismo: {self.tienePresentismo}"
    
    @property
    def calcularSueldo(self):
        if self.tienePresentismo:
            return self.sueldoBasico * 1.13
        return self.sueldoBasico

class Vendedor(Empleado):
    def __init__(self, nombre, apellido, edad, documento, sueldoBasico, totalVentas):
        super().__init__(nombre, apellido, edad, documento, sueldoBasico)
        self.totalVentas = totalVentas

    def __str__(self):
        return f"{super().__str__()}, Ventas: {self.totalVentas}"

    @property
    def calcularSueldo(self):
        return self.sueldoBasico + (self.totalVentas * 0.01)


class Empresa:
    def __init__(self, nombre, cuit):
        self.empleados = []
        self.nombre = nombre
        self.cuit = cuit

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def mostrarEmpleados(self):
        for empleado in self.empleados:
            print(empleado)
            print(f"Sueldo: {empleado.calcularSueldo}")
            print("------------------------")


vendedor1 = Vendedor("Juan", "Pérez", 30, "12345678", 2000, 50000)
print(vendedor1)
print(f"Sueldo del vendedor: {vendedor1.calcularSueldo}")

obrero1 = Obrero("María", "Gómez", 28, "87654321", 1500, 10)
print(obrero1)
print(f"Sueldo del obrero: {obrero1.calcularSueldo}")

administrativo1 = Administrativo("Carlos", "López", 35, "11223344", 1800, True)
print(administrativo1)
print(f"Sueldo del administrativo: {administrativo1.calcularSueldo}")

administrativo2 = Administrativo("Ana", "Martínez", 32, "55667788", 1800, False)
print(administrativo2)
print(f"Sueldo del administrativo: {administrativo2.calcularSueldo}")