# Módulos como programas ejecutables

```python
def sumar(a, b):
    return a + b


print(sumar(10, 5))  # se ejecutará al importar
```

```python
def sumar(a, b):
    return a + b


if __name__ == "__main__":  # evita la ejecución al importar
    print(sumar(10, 5))
```
