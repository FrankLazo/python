# Herencia

```python
class Animal:  # clase padre
    def comer(self):
        print("Comiendo")


class Perro(Animal):  # clase hija
    def ladrar(self):
        print("Guau")
```

```python
perro = Perro()

perro.comer()
perro.ladrar()
```
