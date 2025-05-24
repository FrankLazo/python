# import math

text = "Texto de pruebas"

# for car in text:
#     print( car )
#     if car == 'x':
#         break
# else:
#     print( "for terminado" )

lista_a = [ 10, 20, 30 ]
lista_b = [ 12, 'Muestra', False ]
lista_c = [ 12, 'Muestra', False, [ 37, 0 ] ]

# Mostrar listas completas
print( lista_a[:] )
print( lista_b[:] )
print( lista_c[:] )

# Mostrar elementos X de la lista
print( lista_a[0] )
print( lista_a[2] )

print( lista_a[-3] )
print( lista_a[-1] )

# Mostrar porción de la lista
print( lista_c[1:3] )
print( lista_c[:3] )
print( lista_c[1:] )
