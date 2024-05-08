#CLASE
"""
Objeto = Instancia

"""
# ATRIBUTOS
"""
Alumno: 

    -Nombre
    -Apellido
    -DNI
    -Mail
""" 
# metodos (funciones)

"""
-Alta()
-Inscribir_curso()
-modificar_datos_personales()
"""

class Alumno:
    def __init__(self, nombre, apellido, dni) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def alta(self):
        print(f"El alumno {self.nombre} {self.apellido} se dió de alta en un curso")

    def __eq__(self, other: object) -> bool:
        return self.dni == other.dni

alumno1 = Alumno("Carlos", "Lopez", 1234)
alumno2 = Alumno("Ana", "Gomez", 4434)
alumno3 = Alumno("Carl", "pez", 1234)

print(alumno1.nombre, alumno1.apellido)

alumno1.alta()

print(alumno1 == alumno3)