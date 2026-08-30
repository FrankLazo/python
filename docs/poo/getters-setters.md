# Getters y setters

```python
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
```

```python
persona = Persona("Ana")

print(persona.nombre)    # ejecuta el getter

persona.nombre = "Luis"  # ejecuta el setter
```
