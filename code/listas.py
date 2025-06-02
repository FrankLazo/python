# Creación de listas
lista_a = [ 10, 20, 30, 40, 50 ]
lista_b = [ 12, 'Muestra', False, 125.37 ]
lista_c = [ -7, 'Otra muestra', True, [ 37, 0 ] ]

# Mostrar listas completas
print( lista_a[:] )
print( lista_b[:] )
print( lista_c[:] )

# Mostrar elementos X de la lista
print( lista_a[0] )
print( lista_a[4] )

print( lista_a[-5] )
print( lista_a[-1] )

# Mostrar porción de la lista
print( lista_a[1:4] )
print( lista_a[:3] )
print( lista_a[2:] )

# Agregar nuevos elementos

lista_a.append( 20 )
lista_a.insert( 2, 50 )
print( lista_a )

# Combinar listas

lista_a.extend( lista_b )
print( lista_a )

nueva_lista = lista_a + lista_b + lista_c
print( nueva_lista )

nueva_lista = lista_a * 3
print( nueva_lista )

# Eliminar elementos

lista_a.remove( 50 )
lista_a.pop( 5 )
lista_a.pop()
print( lista_a )

# Obtener índice de un elemento

index = lista_a.index( 50 )
print( index )
