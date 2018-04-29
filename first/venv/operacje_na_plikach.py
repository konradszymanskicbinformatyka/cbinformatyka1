plik = open('wyniki-lotto-sortowane.csv','r')
file_contentent = plik.readlines()
file_without_keys = file_contentent[1:]
wynik = file_without_keys

for i in range(len(file_without_keys)):
    string = str(file_without_keys[i])
    for j in range(len(string)):
        wynik[i] = string.split(';')
for i in range(len(wynik)):
    lenght = len(wynik[i])
    if len(wynik[i][lenght-1]) == 3:
        wynik[i][lenght-1] = wynik[i][lenght-1][:2]
    else:
        wynik[i][lenght-1] = wynik[i][lenght-1][:1]

klucze_str = str(file_contentent[0])
klucze = klucze_str.split(';')
lista = list()
wynik_zamania_kolumn_na_wiersze = []
klucze[len(klucze)-1]=klucze[len(klucze)-1][:2]
słownik={}
lista_słowników=list()

# print(wynik)
for i in range(len(wynik)):
    for j in range(len(klucze)):
        słownik[klucze[j]] = wynik[i][j]
    lista_słowników.append(słownik)
# print(lista_słowników)
for j in range(len(klucze)):
    lista=[]
    for i in range(len(wynik)):
        lista.append(wynik[i][j])
    wynik_zamania_kolumn_na_wiersze.append(lista)

słownik_list ={}
for i in range(len(klucze)):
    słownik_list[klucze[i]] = wynik_zamania_kolumn_na_wiersze[i]
liczba=input('podaj liczbę która cię interesuje')
# for i in range(len(klucze)):
#     if liczba ==
#     print(słownik_list[klucze[i]])
# print(słownik_list)

plik.close()
