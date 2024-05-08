class Persona:
    def __init__(self, nombre, apellido, dni) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def saludar(self):
        print(f"Hola mi nombre es: {self.nombre} {self.apellido}")

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, turno) -> None:
        super().__init__(nombre, apellido, dni)
        self.turno = turno

    def inscribirse(self):
        print("Me inscribi a un curso")

class Docente(Persona):
    def __init__(self, nombre, apellido, dni, CUIT) -> None:
        super().__init__(nombre, apellido, dni)
        self.CUIT = CUIT

    def tomar_curso(self):
        print("Tomé un curso como docente")



alumno1 = Alumno("Carlos", "Lopez", 124124, "tarde")
alumno1.saludar()
alumno1.inscribirse()

docente1 = Docente("Ana", "Paz", 12312, 123)
docente1.saludar()
docente1.tomar_curso()