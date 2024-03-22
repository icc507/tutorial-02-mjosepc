#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = input().split()
m = input().split()

tupla1  = tuple(int(x) if x.isdigit() else x for x in t)
tupla2 = tuple(int(x) if x.isdigit() else x for x in m)

salida = tupla2 + tupla1 + tupla2
print(salida)
