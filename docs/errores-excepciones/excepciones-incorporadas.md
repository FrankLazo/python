# Excepciones incorporadas

```python
try:
    numero = int(input("Número: "))
    resultado = 10 / numero

except ValueError:
    print("Debes introducir un número válido")

except ZeroDivisionError:
    print("No puedes dividir entre cero")
```
