# Expresiones condicionales

print( 1000 < 500 )
print( 200 != 300 )

print( 1000 < 500 and 200 != 300 )
print( 1000 < 500 or 200 != 300 )

lista = [10, 20, 30]
tupla = ["a", "b", "c"]

print( 10 in lista )
print( "b" not in tupla )

lista_1 = [10, 20, 30]
lista_2 = [10, 20, 30]

print( lista_1 is not lista_2 )

print( 0 < 50 < 100 < 200 )
print( "Expresión: " + str( 0 < 50 and 100 > 200 or 50 != 25 and not False ))
print( "Expresión: " + str( not 0 < 50 or True ))

# Estructura IF

if 0 < 100:
    print( "Estructura IF" )

if 0 > 100:
    print( "Estructura IF" )
else:
    print( "Estructura IF + ELSE" )

if 0 > 100:
    print( "Estructura IF" )
elif 100 < 200:
    print( "Estructura IF + ELIF + ELSE" )
else:
    print( "Estructura IF + ELSE" )
