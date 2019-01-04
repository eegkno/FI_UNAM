def quicksort_time(lista):
    quicksort_aux(lista,0,len(lista)-1)

def quicksort_aux(lista,inicio, fin):
    if inicio < fin:

        pivote = particion_time(lista,inicio,fin)

        quicksort_aux(lista, inicio, pivote-1)
        quicksort_aux(lista, pivote+1, fin)
	
def particion_time(lista, inicio, fin):
    pivote = lista[inicio]
    izquierda = inicio+1
    derecha = fin
    bandera = False
    while not bandera:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda + 1
        while lista[derecha] >= pivote and derecha >=izquierda:
            derecha = derecha -1
        if derecha < izquierda:
            bandera= True
        else:
            # swap places
            temp=lista[izquierda]
            lista[izquierda]=lista[derecha]
            lista[derecha]=temp
    # swap inicio with lista[derecha]
    temp=lista[inicio]
    lista[inicio]=lista[derecha]
    lista[derecha]=temp
    return derecha