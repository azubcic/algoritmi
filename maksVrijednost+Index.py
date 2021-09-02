import random


def genList(broj, mini, maxi):
    niz = []
    for i in range(broj):
        niz.append(random.randint(mini, maxi))
    return niz


def searchMaks(lista):
    listaM = []
    maks = lista[0]
    indx = 0
    for integer in range(len(lista)):
        if maks < lista[integer]:
            maks = lista[integer]
            indx = integer;
    listaM.append((maks, indx))
    for integer in range(len(lista)):
        if maks == lista[integer] and indx != integer:
            listaM.append((lista[integer], integer))
    return listaM


lista = genList(6, 0, 15)
print(lista)
rezultat = searchMaks(lista)
# print(rezultat)
print("\nMaksimalna vrijednost:" + str(rezultat[0][0]))
print("Nalazi se na indeksnim pozicijima: ")
for i in range(len(rezultat)):
    print(rezultat[i][1], end=" ")

# import random
#
#
# def pronadiMaks(niz):
#     lista = []
#     maks = niz[0]
#     for integer in range(len(niz)):
#         if maks < niz[integer]:
#             maks = niz[integer]
#     for i in range(len(niz)):
#         if maks == niz[i] and maks not in lista:
#             lista.append((niz[i], i))
#     return lista
#
#
# def genArray(broj, mini, maksi):
#     niz = []
#     for i in range(broj):
#         niz.append(random.randint(mini, maksi))
#     return niz
#
#
# lista = genArray(6, 1, 10)
# print(lista)
# print(pronadiMaks(lista))
