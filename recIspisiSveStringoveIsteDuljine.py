def rekString(lista, duljina, shifter):
    if shifter == len(lista):
        return lista
    else:
        if len(lista[shifter]) != duljina:
            lista.remove(lista[shifter])
            return rekString(lista, duljina, shifter)
        else:
            return rekString(lista, duljina, shifter + 1)


def izbaci(lista, duljina):
    lista2 = []
    for rijec in lista:
        if len(rijec) == duljina:
            lista2.append(rijec)
    return lista2


lista = ['ovo', 'je', 'neki', 'string', 'ima', 'elemenata', 'više', 'od', 'tri']
print("Pocetna lista: " + str(lista))
# print("Zavrsna lista2: " + str(izbaci(lista, 3)))
rekString(lista, 3, 0)
print("Zavrsna lista: " + str(lista))