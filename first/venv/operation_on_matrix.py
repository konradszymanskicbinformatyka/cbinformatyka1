def zamianaWierszyNaKolumny(klucze,wynik):
    for j in range(len(klucze)):
        lista = []
        for i in range(len(wynik)):
            lista.append(wynik[i][j])
        wynik.append(lista)
    return wynik