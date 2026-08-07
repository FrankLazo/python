# Diccionarios

Estructura de datos en pares `"clave": valor`: `dict`

```python
dicc_vacio = {}
```

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Lima"
}
```

```python
persona["nombre"]           # obtener valor
persona["estatura"] = 1.65  # nuevo elemento
```

## Métodos y funciones

- `len()`      → Contar todas las claves
- `.get()`     → Obtener valor por clave (o valor por defecto)
- `.keys()`    → Obtener claves
- `.values()`  → Obtener valores
- `.items()`   → Obtener pares `(clave, valor)`
- `.update()`  → Actualizar o agregar elementos
- `.pop()`     → Eliminar por clave y devolver valor
- `.popitem()` → Eliminar y devolver el último par `(clave, valor)`
- `.clear()`   → Eliminar todos los elementos
- `.copy()`    → Obtener copia
