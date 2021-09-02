import random

def SimpleIntegerSort(lista):
    for integer in range(len(lista)):
      for integer2 in range(integer + 1, len(lista)):
          if lista[integer] < lista[integer2]:
            temp = lista[integer]
            lista[integer] = lista[integer2]
            lista[integer2] = temp
    return lista


def genArray(broj, mini, maksi):
    niz = []
    for i in range(broj):
        niz.append(random.randint(mini, maksi))
    return niz


def recIspis(lista, shifter, maksi):
    maksi = lista[0]
    if shifter == len(lista):
        return None
    else:
        print(lista[shifter])
        print("Od najveceg je kraci za: " + str(maksi - lista[shifter]))
        return recIspis(lista, shifter+1, maksi)


lista = genArray(5, 1, 10)
print(lista)
rezultat = SimpleIntegerSort(lista)
print(rezultat)
recIspis(lista, 0, 0)