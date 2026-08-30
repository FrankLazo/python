# Función `isinstance`

```python
isinstance(objeto, Clase)  # True si el objeto es instancia de la Clase
```

```python
class Animal:
    pass

class Perro(Animal):
    pass

perro = Perro()

print(isinstance(perro, Perro))   # True
print(isinstance(perro, Animal))  # True
```
