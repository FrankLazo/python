# Listas

- Son **mutables**
- Son de tamaño dinámico
- Sus elementos son de cualquier tipo
- Sus elementos mantienen su respectivo orden

```py
nombre_lista = [ elem_1, elem_2, elem_3, ..., elem_N ]
```

```py
lista_a = [ 10, 20, 30 ]
lista_b = [ 12, 'Muestra', False ]
lista_c = [ 12, 'Muestra', False, [ 37, 0 ] ]
```

- Devolver todos los elementos de la lista

```py
nombre_lista[:]
```

- Devolver un elemento de la lista

```py
nombre_lista[0]   # Primer elemento
nombre_lista[N-1] # Último elemento

nombre_lista[-N]  # Primer elemento
nombre_lista[-1]  # Último elemento
```

- Devolver una porción de la lista

```py
nombre_lista[A:B] # Desde el índice A hasta el índice B-1

nombre_lista[:X]  # Hasta el índice X-1
nombre_lista[0:X] # Hasta el índice X-1

nombre_lista[X:]  # Desde el índice X hasta el final
nombre_lista[X:N] # Desde el índice X hasta el final
```

