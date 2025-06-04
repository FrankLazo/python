# Cadenas de caracteres

- Secuencia de caracteres entre comillas simples **`' '`**, dobles **`" "`** o triples **`''' '''`**
- Se denominan **strings** y son del tipo `<class 'str'>`

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

- Tratamiento similar a las listas

```py
texto = "Muestra"

print( texto[0] )  # "M"
print( texto[-7] ) # "M"

print( texto[6] )  # "a"
print( texto[-1] ) # "a"
```

```py
print( texto[:5] ) # "Muest"
print( texto[2:] ) # "estra"
```

## f-string

- Del inglés *formatted string literal*.
- Permite insertar variables o expresiones dentro de una cadena

```py
nombre = "Ana"
saldo = 720.35

mensaje = f"Hola { nombre }, su saldo es: ${ saldo }"
# Hola Ana, su saldo es $720.35
```

## Métodos

- Cantidad de caracteres

```py
texto = "Muestra"

len( texto ) # Devuelve 7
```

- Convertir entre minúsculas y mayúsculas

```py
texto_muestra.lower() # Convierte a minúsculas
texto_muestra.upper() # Convierte a mayúsculas
```

- Reemplazar todas las coincidencias de un caracter

```py
texto = "banana"
nuevo_texto = texto.replace("a", "o") # "bonono"
```
