# Módulos con clases

```python
# usuario.py

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")
```

```python
from usuario import Usuario

usuario = Usuario("Ana")
usuario.saludar()
```
