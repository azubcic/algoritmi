def searchForString(lista, string, shifter, status):
    if status == False:
        print(f"Element [{string}] pronađen u listi na indeksnoj poziciji {shifter}")
        return lista, string, status
    elif shifter == len(lista):
        status = False
        print(f"Element [{string}] nije pronađen u listi!")
    elif lista[shifter] == string:
        status = False
        return searchForString(lista, string, shifter, status)
    else:
        return searchForString(lista, string, shifter + 1, status)

# def searchUI(lista, string, shifter, status):
#     searchForString(lista, string, shifter, s)
#     if status == False:



test = ["Ovo je ", "neki testni ", "string", "za test", "je ", "je"]
print(test)
print("Test koda: ")
print(searchForString(test, "string", 0, True))