# Función `super`

```py
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    # super() → acceder a métodos de la clase padre

estudiante = Estudiante("Ana", "Ingeniería")

print(estudiante.nombre)
print(estudiante.carrera)
```
