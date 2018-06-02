from draw import Draw
from collections import Counter

file = open('wyniki-lotto-sortowane.csv', 'r')
file_contentent = file.readlines()
file_without_keys = file_contentent[1:]
data = file_without_keys

for i in range(len(file_without_keys)): #usuwanie średników
    string = str(file_without_keys[i])
    for j in range(len(string)):
        data[i] = string.split(';')

for i in range(len(data)):  #uduwanie /n
    lenght = len(data[i])
    if len(data[i][lenght-1]) == 3:
        data[i][lenght-1] = data[i][lenght-1][:2]
    else:
        data[i][lenght-1] = data[i][lenght-1][:1]

draws = {}
dict_keys = []

for i in range(len(data)): #tworzenie słownika z objektem
    details_data = data[i]

    month = details_data[2]
    if (len(month) == 1):
        month = '0'+month
    day = details_data[1]
    if (len(day) == 1):
        day = '0'+day

    draw = Draw(details_data[0]) #tworznie objektu
    draw.numbers = [
        details_data[4],
        details_data[5],
        details_data[6],
        details_data[7],
        details_data[8],
        details_data[9]
    ]

    date = day+'-'+month+'-'+details_data[3] #tworznie klucza do słownika
    dict_keys.append(date) #Zapisanie sobie kluczy do statystyk
    draws[date] = draw

no_appearances = Counter()

for key in dict_keys:
    no_appearances = no_appearances + Counter(draws[key].numbers)

file.close()

print("Witaj posiadam wyniki losowania lotto od %s do %s" % (dict_keys[0],dict_keys[len(dict_keys)-1]))
print('Czego chciałbyś się dowiedzieć')

wyjsc = ''

while (wyjsc != 't'):
    print('1.Ile razy podana przeze mnie liczba była wylosowana')
    print('2.x najczęściej wylosowywanych liczb')
    print('3.x najrzadziej wylosowywanych liczb')
    print('4.x liczba pod względem najczęściej wylosowywanych')
    print('5.Wylosowane liczby z określonej daty dd-mm-rrrr')
    choice = input('Podaj swój wybór od 1 do 5: ')
    if int(choice) < 1 or int(choice) > 5:
        print('Nie ma takiego wyboru')

    elif choice == '1':
        liczba = input('Podaj liczbę: ')
        if int(liczba) > 49: #sprawdzenie tylko podstawowwych przypadków
            print('Nie ma tylu liczb')
        elif int(liczba) == 0:
            print('0 naprawdę?')
        elif int(liczba) < 0:
            print('ujemne naprawdę?')
        else:
            print('Liczba %s była wolosowywana %s razy' % (liczba,no_appearances[liczba]))

    elif choice == '2':
        quantity=input('Ile najczęściej wylosowanych liczb chcesz znać? ')
        quantity = int(quantity)
        if quantity > 49: #sprawdzenie tylko podstawowwych przypadków
            print('Nie ma tylu liczb')
        elif quantity == 0:
            print('0 naprawdę?')
        elif quantity < 0:
            print('ujemne naprawdę?')
        else:
            answers = no_appearances.most_common(quantity)
            for answer in answers:
                print('Liczba %s była wylosowana %s razy ' % (answer[0],answer[1]))

    elif choice == '3':
        quantity=input('Ile najrzadziej wylosowanych liczb chcesz znać? ')
        quantity = int(quantity)
        if quantity > 49: #sprawdzenie tylko podstawowwych przypadków
            print('Nie ma tylu liczb')
        elif quantity == 0:
            print('0 naprawdę?')
        elif quantity < 0:
            print('ujemne naprawdę?')
        else:
            answers = no_appearances.most_common()[:-quantity-1:-1]
            for answer in answers:
                print('Liczba %s była wylosowana %s razy ' % (answer[0],answer[1]))

    elif choice == '4':
        number=input('Ktora liczba pod wględem najczęściej wylosowanych? ')
        number = int(number)
        if number > 49: #sprawdzenie tylko podstawowwych przypadków
            print('Nie ma tylu liczb')
        elif number == 0:
            print('0 naprawdę?')
        elif number < 0:
            print('ujemne naprawdę?')
        else:
            answer = no_appearances.most_common()[number - 1]
            print('Liczba %s była wylosowana %s razy ' % (answer[0],answer[1]))

    elif choice == '5':
        date = input("podaj datę dd-mm-rrrr : ")
        if (len(date)!=10): #sprawdzenie tylko podstawowwych przypadków
            print('Niepoprawna data')
        elif (date not in dict_keys):
            print('Tego dnia nie było losowania')
        else:
            print('wylosowane liczby tego dnia to %s ' % (draws[date].numbers))

    wyjsc = input('Czy to wszystko t tak n nie: ')
    print()

print('Dziękuje zapraszam ponownie')

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


