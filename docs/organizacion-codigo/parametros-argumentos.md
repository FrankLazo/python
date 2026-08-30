# Parámetros y argumentos

```python
def saludar(nombre):  # parámetro único
    print(f"Hola {nombre}")
```

```python
def presentar(nombre, edad):  # varios parámetros
    print(f"{nombre} tiene {edad} años")
```

```python
saludar("Ana")  # argumento único
```

```python
saludar("Ana", 20)  # argumentos por posición
```

```python
saludar(edad=20, nombre="Ana")  # argumentos por nombre
```
