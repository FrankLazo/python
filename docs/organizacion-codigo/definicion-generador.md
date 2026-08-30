# Definición de un generador

```python
def numeros():
    yield 1
    yield 2
    yield 3
```

```python
g = numeros()  # objeto generador
```

```python
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
```
