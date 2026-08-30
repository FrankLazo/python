# Instrucción `finally`

```python
try:
    archivo = open("datos.txt")

except FileNotFoundError:
    print("El archivo no existe")

finally:
    # Código que se ejecuta siempre, haya ocurrido o no una excepción
    print("Fin de la operación")
```
