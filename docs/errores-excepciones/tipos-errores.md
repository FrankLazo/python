# Tipos de errores

Errores de **sintaxis**:

```python
edad = int(input("Edad: ")   # falta un paréntesis
if edad >= 18                # faltan los dos puntos
print("Eres mayor de edad")  # falta la identación
```

Errores **lógicos**:

```python
edad = int(input("Edad: "))
if edad <= 18  # operador de comparación incorrecto
    print("Eres mayor de edad")
```

Errores en **tiempo de ejecución**:

```python
edad = int(input("Edad: "))  # error si el usuario ingresa un texto
if edad >= 18
    print("Eres mayor de edad")
```
