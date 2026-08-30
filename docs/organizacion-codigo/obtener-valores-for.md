# Obtener valores con `for`

```python
def numeros():
    yield 1
    yield 2
    yield 3
```

```python
for numero in numeros():
    print(numero)
```
