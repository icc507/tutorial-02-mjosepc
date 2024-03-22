#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
def arbolBinario(numero):
    return [numero, [], [], []]

def insertaEnArbolBinario(arbol, numero):
    if arbol == []:
        arbol += arbolBinario(numero)
    elif arbol[0] == numero:
        insertaEnArbolBinario(arbol[2], numero)
    elif numero < arbol[0]:
        insertaEnArbolBinario(arbol[1], numero)
    else:
        insertaEnArbolBinario(arbol[3], numero)
    return arbol 

numeros = input().split()
arbol = []
for numero in numeros:
    arbol = insertaEnArbolBinario(arbol, int(numero)) 

print(arbol)
