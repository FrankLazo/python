# Sintaxis de clase general

```python
class NombreClase:

    atributo_clase = valor

    def __init__(self, parametro):
        self.atributo = parametro

    def metodo(self):
        ...

    @classmethod
    def metodo_clase(cls):
        ...

    @staticmethod
    def metodo_estatico():
        ...


objeto = NombreClase(valor)

objeto.atributo
objeto.metodo()
```
