# Condicionales

## Expresiones condicionales

- Una **expresión condicional** está formada por diferentes operadores que dan por resultado un valor **booleano**

```py
# Operadores de comparación
1000 < 500 # Devuelve False
200 != 300 # Devuelve True
```

```py
# Operadores lógicos
# Para combinar cualquier expresión condicional
1000 < 500 and 200 != 300 # Devuelve False
1000 < 500 or 200 != 300  # Devuelve True
```

```py
# Operadores de pertenencia
lista = [10, 20, 30]
tupla = ["a", "b", "c"]

10 in lista      # Devuelve True
"b" not in tupla # Devuelve False
```

```py
# Operadores de identidad
lista_1 = [10, 20, 30]
lista_2 = [10, 20, 30]

lista_1 is not lista_2 # Devuelve True
```

### Concatenación de operadores

- Operadores de comparación

```py
0 < 50 < 100 < 200

# Equivalente a:
0 < 50 and 50 < 100 and 100 < 200
```

- Operadores de comparación y lógicos

```py
# Se resuelven de izquierda a derecha y por prioridad
0 < 50 and 100 > 200 or 50 != 25 and not False # Devuelve True
not 0 < 50 or True                             # Devuelve True
```

### Prioridad de operadores

1. Operador de comparación
1. Operador `not`
1. Operador `and`
1. Operador `or`

## Estructura IF

- Ejecuta un bloque de código sólo si se cumple una condición, esto es, si la expresión condicional dada es verdadera

```py
if expresion_condicional:
	# código a ejecutar
	# si la expresion
	# es verdadera
```

```py
if expresion_condicional:
	# código a ejecutar
	# si la expresion
	# es verdadera
else:
	# código a ejecutar
	# si la expresion
	# es falsa
```

```py
if expresion_condicional_1:
	# código a ejecutar
	# si la expresion 1
	# es verdadera
elif expresion_condicional_2:
	# código a ejecutar
	# si la expresion 2
	# es verdadera

	# ...

elif expresion_condicional_n:
	# código a ejecutar
	# si la expresion n
	# es verdadera
else:
	# código a ejecutar
	# si ninguna expresion
	# anterior fue verdadera
```
