# Número variable de argumentos

```python
def mostrar_suma(*numeros):
    print(sum(numeros))
```

```python
def mostrar_datos(**datos):
    print(datos)
```

```python
mostrar_suma(1, 2, 3, 4)              # tupla
mostrar_datos(nombre="Ana", edad=25)  # diccionario
```
