import random


def pronadiParne(lista):
    # parnaLista = []
    # cnt = 0
    # for i in lista:
    #     if i % 2 == 0:
    #         parnaLista.append((i, cnt))
    #     cnt += 1
    parnaLista = [(lista[i], i) for i in range(len(lista)) if (i % 2 == 0)]
    # if len(parnaLista) == 0:
    #     print("U ulaznoj listi nije bilo parnih brojeva!")
    return parnaLista


def generirajListu(broj):
    lista = []
    for i in range(broj):
        lista.append(random.randint(1, 100))
    return lista


lista = generirajListu(8)
print(lista)
print(pronadiParne(lista))
