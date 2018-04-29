# lista_imion = ['kamil', 'konrad', 'agata', 'beata']
# lista_nazwisk = ['kończak', 'roński', 'kot', 'xsijński']
słownik_kamil = {'imię': 'kamil', 'nazwisko': 'kończak', 'ocena': 2}
słownik_beata = {'imię': 'beata', 'nazwisko': 'kot', 'ocena': 3}
słownik_konrad = {'imię': 'konrad', 'nazwisko': 'arwara', 'ocena': 4}
słownik_agata = {'imię': 'agata', 'nazwisko': 'pies', 'ocena': 5}
lista = [słownik_kamil, słownik_beata, słownik_konrad , słownik_agata]
stringw=''
klucze = list(słownik_agata.keys())
for i in range(len(lista)):
    for z in klucze:
        stringw = stringw + ' ' + str(lista[i][z])
    stringw = stringw + '\n'
print(stringw)
