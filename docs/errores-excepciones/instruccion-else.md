# Instrucción `else`

```python
try:
    numero = int(input("Número: "))

except ValueError:
    print("Entrada inválida")

else:
    # Código que se ejecuta solamente si no ocurrió ninguna excepción
    print("Número ingresado:", numero)
```
