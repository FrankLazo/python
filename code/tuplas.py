tupla = ( 10, 20, 40, 80, 160, 80, 40, 80 )

# Devolver elementos de la tupla

print( tupla )
print( tupla[:] )

print( tupla[0] )
print( tupla[-8] )

print( tupla[7] )
print( tupla[-1] )

print( tupla[2:6] )
print( tupla[:4] )
print( tupla[4:] )

# Conversión entre listas y tuplas

lista = list( tupla )
print( lista )

otra_tupla = tuple( lista )
print( otra_tupla )

# Tupla unitaria

tupla_1 = ( 100, )
print( type(tupla_1) )
print( tupla_1 )

# Empaquetado de tupla

tupla_2 = 10, 20, "testeo", True
print( tupla_2 )

# Desempaquetado de tupla

var_1, var_2, var_3, var_4 = tupla_2
print( var_1 )
print( var_2 )
print( var_3 )
print( var_4 )

# Obtener índice de un elemento

print( tupla.index( 40 ) )

# Obtener cantidad de elementos

print( tupla.count( 80 ) )
print( len( tupla ) )
