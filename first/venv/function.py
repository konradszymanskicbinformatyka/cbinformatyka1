first = int(input("podaj pierwszą liczbę"))
second = int(input("podaj pierwszą liczbę"))
print('wybierz jaką operacje matematyczna chcesz wykonywać na podanych dwóch liczbach ')
answer = int(input("1.dodawanie 2.odejmowanie 3. dzielenie 4. mnożenie\n"))
if answer == 1:
    print(function.add(first, second))
elif answer == 2:
    print(function.oddejmowanie(first, second))
elif answer == 3:
    print(function.dzielenie(first, second))
elif answer == 4:
    print(function.mnozenie(first, second))
else:
    print("nie ma takiej opcji")

def add(a,b):
    wynik=a+b
    return wynik


def oddejmowanie(a,b):
    wynik=a-b
    return wynik


def mnozenie(a,b):
    wynik=a*b
    return wynik


def dzielenie(a,b):
    if b==0:
        wynik="nie można dzielić przez zero"
        return wynik
    wynik=a/b
    return wynik


