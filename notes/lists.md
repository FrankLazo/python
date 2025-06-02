# Listas

- Son **mutables**
- Son de tamaño dinámico
- Sus elementos son de cualquier tipo
- Sus elementos mantienen su respectivo orden

```py
nombre_lista = [ elem_1, elem_2, elem_3, ..., elem_N ]
```

```py
lista_a = [ 10, 20, 30, 40, 50 ]
lista_b = [ 12, 'Muestra', False, 125.37 ]
lista_c = [ -7, 'Otra muestra', True, [ 37, 0 ] ]
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

## Métodos

- Agregar nuevos elementos

```py
lista.append(new_element)        # Al final de la lista
lista.insert(index, new_element) # En la posición index
```

- Combinar listas

```py
lista.extend(lista_n)           # Se agrega al final
nueva_lista = lista_1 + lista_2 # Concatena las listas
nueva_lista = lista_1 * N       # Concatena la lista N veces
```

- Eliminar elementos

```py
lista.remove('elemento') # La primera coincidencia
lista.pop(index)		 # El elemento en la posición index
lista.pop()				 # El último elemento
```

- Obtener índice de un elemento

```py
lista.index('elemento') # De la primera coincidencia
```
