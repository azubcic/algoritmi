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


lista = ["string", "koji", "ce", "CE", "se", "ukloniti", "ukloniti", "ajde"]
print(lista)
rezultat = izbaciDupl(lista, 0, 0)
print(rezultat)
