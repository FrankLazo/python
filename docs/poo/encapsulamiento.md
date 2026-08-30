# Encapsulamiento

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo  # atributo protegido

    def _verificar(self):    # método protegido
        pass
```

```python
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado (name mangling)

    def __verificar(self):    # método privado (name mangling)
        pass
```
