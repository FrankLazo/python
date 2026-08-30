# Polimorfismo

```python
class Perro:
    def hablar(self):
        print("Guau")


class Gato:
    def hablar(self):
        print("Miau")
```

```python
animales = [Perro(), Gato()]

for animal in animales:
    animal.hablar()
```

```python
def hablar(animal):
    animal.hablar()

fido = Perro()
salem = Gato()

hablar(fido)
hablar(salem)
```
