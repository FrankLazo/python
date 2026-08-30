# Funciones como objetos

```python
def saludar():
    print("Hola")

f = saludar

f()
```

```python
def ejecutar(funcion):
    funcion()

ejecutar(saludar)
```
