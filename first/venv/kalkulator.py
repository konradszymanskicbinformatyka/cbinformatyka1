import function
first = int(input("podaj pierwszą liczbę"))
second = int(input("podaj pierwszą liczbę"))
answer = int(input("wybierz jaką operacje matematyczna chcesz wykonywać na podanych dwóch liczbach \n1.dodawanie\n2.odejmowanie\n3.dzielenie\n4.mnożenie\n"))
if answer == 1:
    print("wynik wybranej przez cciebie operacji wynosi %s " % (function.add(first, second)))
elif answer == 2:
    print("wynik wybranej przez cciebie operacji wynosi %s " % (function.oddejmowanie(first, second)))
elif answer == 3:
    print("wynik wybranej przez cciebie operacji wynosi %s " % (function.dzielenie(first, second)))
elif answer == 4:
    print("wynik wybranej przez cciebie operacji wynosi %s " % (function.mnozenie(first, second)))
else:
    print("nie ma takiej opcji")