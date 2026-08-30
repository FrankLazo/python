# Lazy evaluation

```python
def numeros():
    for i in range(1000000):
        yield i
```

Cada número se produce conforme se necesita:

```python
for numero in numeros():
    print(numero)
```

Todos los números se almacenan en memoria:

```python
numeros = [i for i in range(1000000)]
```
