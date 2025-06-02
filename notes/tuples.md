# Tuplas

- Son **inmutables**
- Son de tamaño dinámico
- Sus elementos son de cualquier tipo
- Sus elementos mantienen su respectivo orden
- Sí permiten:
	- Extraer porciones (creará nuevas tuplas)
	- Comprobar si un elemento está en la tupla
- No permiten:
	- Añadir, eliminar o mover elementos
	- Búsqueda de elementos
- Comparado con las listas:
	- Son más rápidas y ocupan menos espacio
	- Se pueden usar para formatear **strings**
	- Se pueden usar como claves en un **diccionario**

```py
nombre_tupla = ( elem_1, elem_2, elem_3, ..., elem_N )
```

- Devolver elementos de la tupla

```py
nombre_tupla      # Todos los elementos
nombre_tupla[:]   # Todos los elementos

nombre_tupla[0]   # Primer elemento
nombre_tupla[-N]  # Primer elemento

nombre_tupla[N-1] # Último elemento
nombre_tupla[-1]  # Último elemento

nombre_tupla[A:B] # Desde el índice A hasta el índice B-1

nombre_tupla[:X]  # Hasta el índice X-1
nombre_tupla[0:X] # Hasta el índice X-1

nombre_tupla[X:]  # Desde el índice X hasta el final
nombre_tupla[X:N] # Desde el índice X hasta el final
```

- Conversión entre listas y tuplas

```py
lista_1 = list( tupla_1 )  # De tupla a lista
tupla_2 = tuple( lista_2 ) # De lista a tupla
```

- Tupla unitaria

```py
tupla_unitaria = ( elem_1, ) # La coma al final es obligatoria
```

- Empaquetado de tupla

```py
# Útil en ciertos contextos para tener un código más limpio y legible
tupla_n = elem_1, elem_2, ..., elem_n # Sin paréntesis
```

- Desempaquetado de tupla

```py
 # Asigna los valores de la tupla a las variables respectivas
 # Cantidad de variables igual al número de elementos de la tupla
var_1, var_2, ..., var_n = tupla_n
```

## Métodos

- Obtener índice de un elemento

```py
tupla.index('elemento') # De la primera coincidencia
```

- Obtener cantidad de elementos

```py
tupla.count('elemento') # De todas las coincidencias
len( tupla )			# Total de elementos
```
