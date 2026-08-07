# Secuencias

Objeto **ordenado** con **índice**: `list`, `tuple`, `str`, `range`

## Acceso

```python
secuencia[2]   # desde la izquierda
secuencia[-3]  # desde la derecha
```

```python
secuencia[1:4]  # slicing
secuencia[:3]   # desde primer elemento
secuencia[2:]   # hasta último elemento
secuencia[:]    # todo
```

```python
secuencia[::2]   # con paso
secuencia[::-1]  # orden inverso
```

## Operadores

- Concatenación (no `range`) → `+`
- Repetición (no `range`) → `*`

## Funciones y métodos

- `sorted()` → Obtener secuencia ordenada
- `.index()` → Obtener índice de elemento
- `.count()` → Contar por elemento
- `len()`    → Contar todos los elementos
- `sum()`    → Sumar todos los elementos (sólo números)
- `max()`    → Hallar valor máximo
- `min()`    → Hallar valor mínimo
- `list()`   → Convertir a lista
- `tuple()`  → Convertir a tupla
