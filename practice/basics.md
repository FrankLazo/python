# Fundamentos

## ¡Saludo con nombre!

Crea una función que tome un nombre y devuelva un saludo en forma de cadena de texto.

### Ejemplos

```py
hello_name("Gerald")  ➞ "Hello Gerald!"
hello_name("Tiffany") ➞ "Hello Tiffany!"
hello_name("Ed")      ➞ "Hello Ed!"
```

## Devolver el siguiente número del entero dado

Crea una función que tome un número como argumento, lo incremente en **+1** y devuelva el resultado.

### Ejemplos

```py
addition(0)  ➞ 1
addition(9)  ➞ 10
addition(-3) ➞ -2
```

## Devolver la suma de dos números
Crea una función que tome dos números como argumentos y devuelva su **suma**.

### Ejemplos

```py
addition(3, 2)   ➞ 5
addition(-3, -6) ➞ -9
addition(7, 3)   ➞ 10
```

## Devolver el residuo de dos números

Hay un único operador en Python capaz de proporcionar el **residuo** (resto) de una operación de división. Se pasan dos números como parámetros. El primer parámetro dividido por el segundo tendrá un residuo, posiblemente cero. Devuelve ese valor.

### Ejemplos

```py
remainder(1, 3) ➞ 1
remainder(3, 4) ➞ 3
remainder(5, 5) ➞ 0
remainder(7, 2) ➞ 1
```

## Encontrar el perímetro de un rectángulo

Crea una función que tome el **largo** y el **ancho** y calcule el **perímetro** de un rectángulo.

### Ejemplos

```py
find_perimeter(6, 7)   ➞ 26
find_perimeter(20, 10) ➞ 60
find_perimeter(2, 9)   ➞ 22
```

## Área de un triángulo

Escribe una función que tome la **base** y la **altura** de un triángulo y devuelva su **área**.

### Ejemplos

```py
tri_area(3, 2)   ➞ 3
tri_area(7, 4)   ➞ 14
tri_area(10, 10) ➞ 50
```

## Convertir minutos en segundos

Escribe una función que tome un número entero (**minutos**) y lo convierta en **segundos**.


### Ejemplos

```py
convert(5) ➞ 300
convert(3) ➞ 180
convert(2) ➞ 120
```

## Convertir horas en segundos

Escribe una función que convierta **horas** en **segundos**.

### Ejemplos

```py
how_many_seconds(2)  ➞ 7200
how_many_seconds(10) ➞ 36000
how_many_seconds(24) ➞ 86400
```

## Convertir horas y minutos en segundos

Escribe una función que tome dos enteros (**horas**, **minutos**), los convierta a **segundos** y los sume.

### Ejemplos

```py
convert(1, 3) ➞ 3780
convert(2, 0) ➞ 7200
convert(0, 0) ➞ 0
```

## Convertir edad a días

Crea una función que tome la edad en **años** y devuelva la edad en **días**.

- Usa 365 días como la duración de un año para este desafío.
- Ignora los años bisiestos y los días entre el último cumpleaños y el momento actual.

### Ejemplos

```py
calc_age(65) ➞ 23725
calc_age(0)  ➞ 0
calc_age(20) ➞ 7300
```

## El problema de la granja
En este desafío, un granjero te pide que le digas cuántas patas se pueden contar entre todos sus animales. El granjero cría tres especies:

- **Gallinas** = 2 patas
- **Vacas** = 4 patas
- **Cerdos** = 4 patas

El granjero ha contado sus animales y te da un subtotal para cada especie. Debes implementar una función que devuelva el **número total de patas** de todos los animales.

### Ejemplos

```py
animals(2, 3, 5) ➞ 36
animals(1, 2, 3) ➞ 22
animals(5, 2, 8) ➞ 50
```

## Puntos de fútbol

Crea una función que tome el número de **victorias**, **empates** y **derrotas**, y calcule el número de puntos que ha obtenido un equipo de fútbol hasta el momento.

- Las **victorias** dan 3 puntos
- Los **empates** dan 1 punto
- Las **derrotas** dan 0 puntos

### Ejemplos

```py
football_points(3, 4, 2) ➞ 13
football_points(5, 0, 2) ➞ 15
football_points(0, 0, 1) ➞ 0
```


