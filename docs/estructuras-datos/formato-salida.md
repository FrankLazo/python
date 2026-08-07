# Formato de salida

```python
precio = 12.5           # decimales
print(f"{precio:.2f}")  # 12.50
```

```python
valor = 0.85           # porcentaje
print(f"{valor:.0%}")  # 85%
```

```python
numero = 1234567      # separador de miles
print(f"{numero:,}")  # 1,234,567
```

```python
print(f"{25:5}")   #    25 ancho mínimo
print(f"{25:05}")  # 00025 relleno con ceros
```

```python
print(f"|{'Ana':<10}|")  # |Ana       | alineación derecha
print(f"|{'Ana':^10}|")  # |   Ana    | alineación centro
print(f"|{'Ana':>10}|")  # |       Ana| alineación izquierda
```
