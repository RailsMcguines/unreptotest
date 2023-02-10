def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def bubble_sort2(lista):
    aux=0
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                
    return lista


lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
bubble_sort(lista)
print("Lista ordenada:", lista)

bubble_sort2(lista)
print("Lista ordenada2:", lista)