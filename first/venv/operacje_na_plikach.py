from draw import Draw

file = open('wyniki-lotto-sortowane.csv', 'r')
file_contentent = file.readlines()
file_without_keys = file_contentent[1:]
data = file_without_keys

for i in range(len(file_without_keys)):
    string = str(file_without_keys[i])
    for j in range(len(string)):
        data[i] = string.split(';')
for i in range(len(data)):
    lenght = len(data[i])
    if len(data[i][lenght-1]) == 3:
        data[i][lenght-1] = data[i][lenght-1][:2]
    else:
        data[i][lenght-1] = data[i][lenght-1][:1]

draws = {}
for i in range(len(data)):
    details_data = data[i]

    month = details_data[2]
    if (len(month) == 1):
        month = '0'+month
    day = details_data[1]
    if (len(day) == 1):
        day = '0'+day

    date = details_data[1]+'-'+month+'-'+details_data[3]
    draws[date] = Draw(details_data[0]).numbers = [
        details_data[4],
        details_data[5],
        details_data[6],
        details_data[7],
        details_data[8],
        details_data[9]
    ]

print(draws['27-01-1957'].numbers)
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

file.close()
