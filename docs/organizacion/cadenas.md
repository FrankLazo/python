# Cadenas

Objeto **inmutable** de **caracteres**: `str`

```python
s_vacio = ""
nombre = "Python"
```

## Métodos

- `.find()`    → Obtener índice de carácter (o `-1`)
- `.strip()`   → Eliminar espacios a la izquierda y derecha
- `.lstrip()`  → Eliminar espacios a la izquierda
- `.rstrip()`  → Eliminar espacios a la derecha
- `.replace()` → Reemplazar caracteres
- `.split()`   → Obtener cadenas a partir de separador
- `.join()`    → Concatenar cadenas a través de separador

Transformación:

- `.lower()`      → Convertir a minúsculas
- `.upper()`      → Convertir a mayúsculas
- `.title()`      → Convertir primera letra de cada palabra a mayúscula
- `.capitalize()` → Convertir primera letra a mayúscula
- `.swapcase()`   → Convertir cada carácter a case contrario

Validación:

- `.isdigit()`    → Validar 0-9 y no vacío
- `.isalpha()`    → Validar a-z, A-Z y no vacío
- `.isalnum()`    → Validar a-z, A-Z, 0-9 y no vacío
- `.isspace()`    → Validar espacios, tabulaciones o nuevas líneas
- `.isupper()`    → Validar mayúsculas y no vacío
- `.islower()`    → Validar minúsculas y no vacío
- `.startswith()` → Validar caracteres de inicio
- `.endswith()`   → Validar caracteres de final
