def sortRec(lista, element, shifter):
    if element == len(lista):
        return lista
    elif shifter == len(lista):
        return sortRec(lista, element + 1, 0)
    elif len(lista[element]) > len(lista[shifter]):
        temp = lista[element]
        lista[element] = lista[shifter]
        lista[shifter] = temp
        return sortRec(lista, element, shifter + 1)
    else:
        return sortRec(lista, element, shifter + 1)


# test
lista = ["samo", "je", "ovo je dobro", "i", "neki-mali", "primjer", "opet"]
print("Input Array:\n" + str(lista))
# sort(lista, 0 ,0)
print("Recursion result:\n" + str(sortRec(lista, 0 ,0)))


