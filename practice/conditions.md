# Condicionales

## ¿El número es menor o igual a cero?

Crea una función que tome un número como único argumento y devuelva `True` si es menor o igual a cero, de lo contrario, devuelve `False`.

### Ejemplos

```py
less_than_or_equal_to_zero(5)  ➞ False
less_than_or_equal_to_zero(0)  ➞ True
less_than_or_equal_to_zero(-2) ➞ True
```

## ¿Los números son iguales?

Crea una función que devuelva `True` cuando `num1` sea igual a `num2`, de lo contrario, devuelve `False`.

### Ejemplos

```py
is_same_num(4, 8)   ➞ False
is_same_num(2, 2)   ➞ True
is_same_num(2, -2)  ➞ False
```

## ¿Menor que 100?

Dados dos números, devuelve `True` si la suma de ambos es menor que 100. De lo contrario, devuelve `False`.

### Ejemplos

```py
less_than_100(22, 15) ➞ True  # 22 + 15 = 37
less_than_100(83, 34) ➞ False # 83 + 34 = 117
less_than_100(3, 77)  ➞ True
```

## División exacta

Dados dos números enteros, `a` y `b`, devuelve `True` si `a` puede dividirse exactamente entre `b`. Devuelve `False` en caso contrario.

### Ejemplos

```py
divides_evenly(98, 7) ➞ True  # 98/7 = 14
divides_evenly(85, 4) ➞ False # 85/4 = 21.25
```

## Comprobar si un número entero es divisible por cinco

Crea una función que devuelva `True` si un número entero se puede dividir exactamente entre 5, y `False` en caso contrario.

### Ejemplos

```py
divisible_by_five(5)   ➞ True
divisible_by_five(-55) ➞ True
divisible_by_five(37)  ➞ False
```

## Apuesta rentable

Crea una función que tome tres argumentos: `prob` (probabilidad), `prize` (premio) y `pay` (costo de la apuesta), y devuelva `True` si `prob * prize > pay`, de lo contrario, devuelve `False`.

- Una apuesta rentable es un juego que genera una ganancia neta positiva
- Donde la ganancia neta se calcula de la siguiente manera: `ganancia_neta = probabilidad_de_ganar * premio − costo_de_jugar`.

Para ilustrar:

```py
profitable_gamble(0.2, 50, 9)
```
... debería devolver `True`, ya que la ganancia neta es 1 (0.2 * 50 - 9), y 1 > 0.

### Ejemplos

```py
profitable_gamble(0.2, 50, 9) ➞ True
profitable_gamble(0.9, 1, 2)  ➞ False
profitable_gamble(0.9, 3, 2)  ➞ True
```

## Dos hacen diez

Crea una función que tome dos argumentos. Ambos argumentos son enteros, `a` y `b`. Devuelve `True` si uno de ellos es 10 o si su suma es igual a 10.

### Ejemplos

```py
makes10(9, 10) ➞ True
makes10(9, 9)  ➞ False
makes10(1, 9)  ➞ True
```

