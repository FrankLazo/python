# Bucle determinado

- Un **bucle** permite ejecutar un bloque de código repetidamente.
- Una **iteración** es cada ejecución o repetición de código que realiza el bucle.
- En un **bucle determinado** se puede conocer o determinar de antemano el número de iteraciones.
- En Python se usa la estructura `for ... in`

```py
for elemento in coleccion_de_elementos:
	# Bloque de código
	# a ejecutar por
	# cada elemento
	# de la colección
```

- Se puede leer como: *para cada o por cada elemento en esta colección o grupo de elementos, ejecutar el siguiente código*.
- La colección o grupo de elementos pueden ser: un objeto `range`, un **string**, una **lista**, una **tupla**, etc.
- La variable `elemento` puede tener cualquier nombre.
- Esta variable en cada iteración tomará el valor de cada uno de los elementos de la colección en su orden respectivo.

## Función range()

- La función `range()` devuelve un objeto tipo `range` que consiste en una secuencia de números.
- No es una lista y tampoco una tupla.

```py
# Ejemplos de secuencias:

range(10)       # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(6, 14)    # 6, 7, 8, 9, 10, 11, 12, 13
range(3, 16, 2) # 3, 5, 7, 9, 11, 13, 15
```

```py
for iterador in range(n):
	# Código que se
	# ejecutará n veces
```
