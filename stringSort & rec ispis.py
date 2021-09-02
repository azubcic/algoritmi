def naiveStringSort(lista):
    for string1 in range(len(lista)):
        for string2 in range(len(lista)):
            if len(lista[string1]) < len(lista[string2]):
                temp = lista[string1]
                lista[string1] = lista[string2]
                lista[string2] = temp
    return lista


def rekurzivniIspis(lista, najduljina, pocetak):
    if len(lista) == pocetak:
        return None
    else:
        leng = len(lista[pocetak])
        print("\nKraci od najduljeg stringa je za: " + str(najduljina - leng))
        print("Duljina: " + str(leng))
        print("Element: " + lista[pocetak])
        return rekurzivniIspis(lista, najduljina, pocetak + 1)

lista = ["ovo874", " je 34 487", "test", "za ovaje", "zadatak"]
print(lista)
naiveStringSort(lista)
print(lista)
rekurzivniIspis(lista, len(lista[-1]), 0)