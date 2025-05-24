# Operadores

## Aritméticos

- El operador `%` se denomina **módulo**
- El operador `**` se denomina **exponente**

```py
suma           = 10 +  3 # Devuelve 13
resta          = 10 -  3 # Devuelve 7
multiplicacion = 10 *  3 # Devuelve 30
division       = 10 /  3 # Devuelve 3.3333333333333335
resto          = 10 %  3 # Devuelve 1
cociente       = 10 // 3 # Devuelve 3
potencia       = 10 ** 3 # Devuelve 1000
```

## Comparación

```py
mayor_que         = 50 >  20 # Devuelve True
menor_que         = 50 <  20 # Devuelve False
mayor_o_igual_que = 50 >= 20 # Devuelve True
menor_o_igual_que = 50 <= 20 # Devuelve False
igual_que         = 50 == 20 # Devuelve False
diferente_que     = 50 != 20 # Devuelve True
```

## Asignación

- Incremento `+=`
- Decremento `-=`

```py
asignacion =   240 # Valor resultante 240
asignacion +=   10 # Valor resultante 250
asignacion -=   54 # Valor resultante 196
asignacion *=    2 # Valor resultante 392
asignacion /=    7 # Valor resultante 56.0
asignacion %=   19 # Valor resultante 18.0
asignacion //=   5 # Valor resultante 3.0
asignacion **=   3 # Valor resultante 27.0
```

## Lógicos

- `and` es verdad si ambos operandos son verdaderos

```py
operador_and =  True and True  # Devuelve True
operador_and =  True and False # Devuelve False
operador_and = False and True  # Devuelve False
operador_and = False and False # Devuelve False
```
- `or` es falso si ambos operandos son falsos

```py
operador_or =  True or True  # Devuelve True
operador_or =  True or False # Devuelve True
operador_or = False or True  # Devuelve True
operador_or = False or False # Devuelve False
```

- `not` devuelve el valor opuesto

```py
operador_not =  not True  # Devuelve False
operador_not =  not False # Devuelve True
```

## De pertenencia

- Si un valor se encuentra en una secuencia de valores

```py
operador_in     =  "str"   in   "string" # Devuelve True
operador_not_in =  "str" not in "string" # Devuelve False
```

## De identidad

- Si dos variables son iguales dependiendo del tipo

```py
operador_is     =  "str"   is   "string" # Devuelve False
operador_is_not =  "str" is not "string" # Devuelve True
```

- Las listas son objetos mutables

```py
a = [ 10, 20, 30 ]
b = [ 10, 20, 30 ]

print( a is b ) # Devuelve False
```
