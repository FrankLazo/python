# Instrucción `else`

- En los bucles funciona similar que en la estructura `if... else...`
- Se ejecuta al finalizar el bucle de manera normal
- No se ejecuta si el bucle termina con `break`

```py
for i in range():
	# ...
else:
	# Bloque de código
	# que se ejecuta al
	# terminar el bucle for
```

```py
while expresion:
	# ...
else:
	# Bloque de código
	# que se ejecuta al
	# terminar el bucle while
```

- Útil en búsqueda de elementos, para saber si se encontró o no:

```py
for i in range(5):
    if i == 3:
        print("Encontrado:", i)
        break
else:
    print("No se encontró ningún 3")
```
