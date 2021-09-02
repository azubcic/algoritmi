import random


def parnnepar(lista):
    neparnalista = []
    parnalista = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            parnalista.append(lista[i])
            neparnalista.append(0)
        else:
            neparnalista.append(lista[i])
            parnalista.append(0)
    return parnalista, neparnalista


def genArray(broj, mini, maksi):
    lista = []
    for i in range(broj):
        lista.append(random.randint(mini, maksi))
    return lista


lista = genArray(7, 1, 10)
print("Original list: " + str(lista))
rezultat = parnnepar(lista)
print("Parna lista iz funkcije: " + str(rezultat[0]))
print("Neparna lista iz funkcije: " + str(rezultat[1]))