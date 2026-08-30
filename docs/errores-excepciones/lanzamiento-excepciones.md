# Lanzamiento de excepciones

```python
edad = -5

if edad < 0:
    raise ValueError("La edad no puede ser negativa")
```

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("El divisor no puede ser cero")

    return a / b
```
