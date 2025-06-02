# Salida estándar

- Es la salida de datos normalmente conectada a la pantalla

```py
print() # Imprime una línea vacía
```

```py
# Cada llamada a print() se realiza en una línea nueva

print( "Texto de muestra" )
print( nombre_variable )
print( 12500 )
print( 0.578 )
print( False )
```

```py
print( "Texto de muestra", end="" )  # Evita un salto de línea
print( "Texto de muestra", end=" " ) # Y agrega un espacio al final
```

- Concatenación de valores

```py
# Saldo: 500 soles
print( "Saldo: ", 500, "soles" )
print( "Saldo: " + str( 500 ) + "soles" )
```
