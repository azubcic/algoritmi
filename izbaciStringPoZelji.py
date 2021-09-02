def izbaciDupl(lista, element, shifter):
    if element == len(lista):
        return lista
    elif shifter == len(lista):
        return izbaciDupl(lista, element + 1, 0)
    elif element == shifter:
        return izbaciDupl(lista, element, shifter + 1)
    elif lista[element].lower() == lista[shifter].lower():
        lista.remove(lista[shifter])
        return izbaciDupl(lista, element, shifter + 1)
    else:
        return izbaciDupl(lista, element, shifter + 1)


def SimpleStringSort(lista):
    for integer in range(len(lista)):
        for integer2 in range(integer + 1, len(lista)):
            if len(lista[integer]) < len(lista[integer2]):
                temp = lista[integer]
                lista[integer] = lista[integer2]
                lista[integer2] = temp
    return lista


lista = ["string", "koji", "ce", "CE", "se", "ukloniti", "ukloniti", "ajde"]
print(lista)
rez = izbaciDupl(lista, 0, 0)
print(rez)
rez = SimpleStringSort(rez)
print(rez)