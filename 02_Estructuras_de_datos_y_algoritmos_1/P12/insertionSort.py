def insertionSort_time(n_lista):
    for index in range(1,len(n_lista)):
        actual = n_lista[index]
        posicion = index
        #print("valor a ordenar = {}".format(actual))
        while posicion>0 and n_lista[posicion-1]>actual:
            n_lista[posicion]=n_lista[posicion-1]
            posicion = posicion-1           
        n_lista[posicion]=actual
        #print(n_lista)
        #print() 
    return n_lista
	
	