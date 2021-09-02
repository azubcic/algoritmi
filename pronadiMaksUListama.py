def findMaks(*listeInput):
    print("=============")
    brojliste = 0
    for lista in listeInput:
        brojliste += 1
        print(str(lista))
        max = lista[0]
        index = 0
        cnt = 0
        for integer in lista:
            if integer > max:
                max = integer
                index = cnt
                finalListe = brojliste
            cnt += 1
    print("=============")
    return max, index, finalListe


lista1 = [23, 1, -100, 23, 44, 567, 10000, 0]
lista2 = [-2, 3, 50000, 89, 1000]
lista3 = [244, 456, 300, 3000, -100, 0, 6, 77, 88, 235000]
rezultat = findMaks(lista1, lista2, lista3)
print("INDP: " + str(rezultat[1]))
print("MAX: " + str(rezultat[0]))
print("IN ARRAY: " + str(rezultat[2]))