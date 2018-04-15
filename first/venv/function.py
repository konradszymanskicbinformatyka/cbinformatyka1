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


first=int(input("podaj pierwszą liczbę"))
second=int(input("podaj pierwszą liczbę"))
print(add(2,3))
print(oddejmowanie(2,3))
print(mnozenie(2,3))
print(dzielenie(2,3))