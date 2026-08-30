# Atributos

```python
class Persona:
    especie = "Humano"  # atributo de clase

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre  # atributo de instancia

    # self → objeto actual
```

```python
persona1 = Persona("Ana")
persona2 = Persona("Luis")

print(Persona.especie)  # atributo de clase

print(persona1.nombre)  # atributo de instancia
print(persona2.nombre)  # atributo de instancia
```
