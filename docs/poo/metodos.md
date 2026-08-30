# Métodos

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

persona = Persona("Ana")
persona.saludar()
```

```python
class Calculadora:
    def sumar(self, a, b):
        return a + b

calc = Calculadora()

resultado = calc.sumar(5, 3)
print(resultado)
```
