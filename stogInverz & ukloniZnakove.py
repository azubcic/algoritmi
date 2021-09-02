import string


def stogInverz(lista, pocetak, kraj):
    if pocetak == kraj or pocetak > kraj:
        return None
    else:
        lista[pocetak], lista[kraj] = lista[kraj], lista[pocetak]
        return stogInverz(lista, pocetak + 1, kraj - 1)


def stog2Inverz(lista):
    cnt = len(lista)
    sort = []
    while cnt > 0:
        sort.append(lista.pop())
        cnt -= 1
    return sort


def removeInterPunctions(lista):
    punc = list(string.punctuation)
    for rijec in range(len(lista)):
        for slovo in lista[rijec]:
            if slovo in punc:
                lista[rijec] = lista[rijec].replace(slovo, "")
    return lista


# ovo je primjer koji ima svoj cilj, a onda dolazi interesantni dio!!!
lista = input().split()
print(lista)
# stogInverz(lista, 0, len(lista)-1)
nova = stog2Inverz(lista)
print(nova)
print(removeInterPunctions(nova))
