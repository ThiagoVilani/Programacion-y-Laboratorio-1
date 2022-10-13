import random
lista_de_numeros = []
for i in range(10):
    lista_de_numeros.append(random.randint(1, 1000))

#---------------------------------------------
def Buscar_minimo(lista:list):
    minimo = 0
    for i in range(len(lista)):
        if lista[i] < lista[minimo]:
            minimo = i
    return minimo
#---------------------------------------------

#---------------------------------------------
"""
def Ordenar_lista_by_Nahuel(lista:list):
    lista_ordenada = []
    for i in range(len(lista)):
        minimo = Buscar_minimo(lista)
        lista_ordenada.append(lista[minimo])
        lista.pop(minimo)
    return lista_ordenada
"""
#---------------------------------------------


#---------------------------------------------
def Ordenar_lista_by_Ivan(lista:list):
    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)-1):
        if  lista_ordenada[i] > lista_ordenada[i+1]: 
            numero_atras = lista_ordenada[i]
            lista_ordenada[i] = lista_ordenada[i+1]
            lista_ordenada[i+1] = numero_atras
#---------------------------------------------
print(lista_de_numeros)
print(Buscar_minimo(lista_de_numeros))
#print(Ordenar_lista_by_Nahuel(lista_de_numeros, "Esta es la lista ordenada por Nahuel"))
print(Ordenar_lista_by_Ivan(lista_de_numeros), "Esta es la lista ordenada por Ivan")