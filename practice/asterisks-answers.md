# Asteriscos: Soluciones

## Línea vertical

```py
longitud = int(input("Longitud: "))

for fila in range(longitud):
    print("*")
```

## Línea horizontal

```py
longitud = int(input("Longitud: "))

for columna in range(longitud):
    print("*", end="  ")
```

## Rectángulo sólido

```py
base   = int(input("Base: "))
altura = int(input("Altura: "))

for fila in range(altura):
    for columna in range(base):
        print("*", end="  ")

    print("") # Salto de línea
```

## Cuadrado sólido

```py
lado = int(input("Lado: "))

for fila in range(lado):
    for columna in range(lado):
        print("*", end="  ")

    print("")
```

## Triángulos sólidos

### Caso I

```py
altura = int(input("Altura: "))

for fila in range(altura):
    for columna in range(altura):
        if fila >= columna:
            print("*", end="  ")
        else:
            break # Termina la ejecución del bloque FOR

    print("")
```

### Caso II

```py
altura = int(input("Altura: "))

for fila in range(altura):
    for columna in range(altura):
        if fila > columna:
            print(" ", end="  ")
        elif fila <= columna:
            print("*", end="  ")

    print("")
```

## Diagonales de un cuadrado

### Caso I

```py
lado = int(input("Lado: "))

for fila in range(lado):
    for columna in range(lado):
        if fila > columna:
            print(" ", end="  ")
        elif fila == columna:
            print("*")
            break
```

### Caso II

```py
lado = int(input("Lado: "))

for fila in range(lado):
    for columna in range(lado):
        if fila + columna < lado - 1:
            print(" ", end="  ")
        elif fila + columna == lado - 1:
            print("*")
            break
```

### Caso III

```py
lado = int(input("Lado: "))

for fila in range(lado):
    for columna in range(lado):
        if fila < columna and fila + columna > lado - 1:
            break
        elif fila == columna or fila + columna == lado - 1:
            print("*", end="  ")
        else:
            print(" ", end="  ")

    print("")
```

## Triángulos sólidos

### Caso III

```py
lado = int(input("Lado: "))

for fila in range(lado):
    for columna in range(lado):
        if fila + columna < lado - 1:
            print("*", end="  ")
        elif fila + columna == lado - 1:
            print("*")
            break
```

### Caso IV

```py
lado = int(input("Lado: "))

for fila in range(lado):
    for columna in range(lado):
        if fila + columna < lado - 1:
            print(" ", end="  ")
        elif fila + columna >= lado - 1:
            print("*", end="  ")

    print("")
```

## Rectángulo hueco

```py
base   = int(input("Base: "))
altura = int(input("Altura: "))

for columna in range(base): # Primera línea
    print("*", end="  ")

print("")

for fila in range(altura - 2):
    for columna in range(base):
        if columna == 0 or columna == base - 1:
            print("*", end="  ")
        else:
            print(" ", end="  ")

    print("")

for columna in range(base): # Última línea
    print("*", end="  ")
```

## Super diagonal

```py
espesor = int(input("Espesor: "))
altura  = int(input("Altura: "))

for fila in range(altura):
    for espacio in range(fila):
        print(" ", end="  ")

    for columna in range(espesor):
        print("*", end="  ")

    print("")
```

## Triángulo isósceles

```py
altura = int(input("Altura: "))
base   = altura * 2 - 1

for fila in range(altura):
    for columna in range(base):
        if fila + columna < altura - 1:
            print(" ", end="  ")
        elif fila + altura <= columna:
            break
        else:
            print("*", end="  ")

    print("")
```

## Cuadrado a 45º

```py
diagonal = int(input("Diagonal: "))

for fila in range(diagonal):
    for columna in range(diagonal):
        if fila + columna < diagonal / 2 - 1 or fila > columna + diagonal / 2:
            print(" ", end="  ")
        elif fila + diagonal / 2 < columna or fila + columna > diagonal + diagonal / 2 - 1:
            break
        else:
            print("*", end="  ")

    print("")
```
