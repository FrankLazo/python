# Tipos de datos

- La función `type()` devuelve el tipo de dato del valor o variable asignada

```py
print( type( 120.50 ) )
```

```py
print( type( variable ) )
```

- Realmente devuelve un objeto de tipo `type` que representa una **clase**, pero la función `print()` la convierte en una cadena de caracteres

## Numéricos

- Enteros `<class 'int'>`

```py
numero_entero = 0
numero_entero = 37
numero_entero = -37
```

- Coma flotante `<class 'float'>`

```py
numero_real = 12.0
numero_real = 120.50
numero_real = -120.50
```

- Complejos `<class 'complex'>`

```py
numero_complejo = 12 + 5j
numero_complejo = 12 - 5j
numero_complejo = 12 + 0j
numero_complejo = 0 + 5j
numero_complejo = 5j
```

## Textos

- Siempre van entre comillas simples **`' '`** o dobles **`" "`** o triples **`''' '''`**
- Se denominan **strings** o cadenas de caracteres
- Son del tipo `<class 'str'>`

```py
texto_comilla_simple =   'Testeo #1'
texto_comilla_doble  =   "Testeo #2"
texto_comilla_triple = '''Testeo #3'''
```

- La triple comilla `'''` o `"""` permite introducir saltos de línea

```py
texto_con_saltos = '''Texto que
se muestra con
tres saltos de línea'''
```

## Booleanos

- Sólo tienen un valor `True` ó `False`
- Son del tipo `<class 'bool'>`

```py
booleano_verdadero = True
booleano_falso     = False
```
