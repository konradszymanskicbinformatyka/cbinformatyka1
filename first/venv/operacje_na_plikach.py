from draw import Draw

plik = open('wyniki-lotto-sortowane.csv', 'r')
file_contentent = plik.readlines()
file_without_keys = file_contentent[1:]
wyniki = file_without_keys

for i in range(len(file_without_keys)):
    string = str(file_without_keys[i])
    for j in range(len(string)):
        wyniki[i] = string.split(';')
for i in range(len(wyniki)):
    lenght = len(wyniki[i])
    if len(wyniki[i][lenght-1]) == 3:
        wyniki[i][lenght-1] = wyniki[i][lenght-1][:2]
    else:
        wyniki[i][lenght-1] = wyniki[i][lenght-1][:1]

draws = {}
for i in range(len(wyniki)):
    wynik = wyniki[i]

    month = wynik[2]
    if (len(month) == 1):
        month = '0'+month
    day = wynik[1]
    if (len(day) == 1):
        day = '0'+day

    date = wynik[1]+'-'+month+'-'+wynik[3]

    draws[date] = Draw(wynik[0]).numbers = [
        wynik[4],
        wynik[5],
        wynik[6],
        wynik[7],
        wynik[8],
        wynik[9]
    ]

# print(draws['21-7-1957'].numbers)
# słownik = {}
# lista_słowników = list()

# # print(wynik)
# for i in range(len(wynik)):
#     for j in range(len(klucze)):
#         słownik[klucze[j]] = wynik[i][j]
#     lista_słowników.append(słownik)
# # print(lista_słowników)
# for j in range(len(klucze)):
#     lista = []
#     for i in range(len(wynik)):
#         lista.append(wynik[i][j])
#     wynik_zamania_kolumn_na_wiersze.append(lista)

# słownik_list = {}
# for i in range(len(klucze)):
#     słownik_list[klucze[i]] = wynik_zamania_kolumn_na_wiersze[i]

# print(lista_słowników[0])
# liczba=input('podaj liczbę która cię interesuje')
# for i in range(len(klucze)):
#     if liczba ==
#     print(słownik_list[klucze[i]])
# print(słownik_list)

plik.close()
