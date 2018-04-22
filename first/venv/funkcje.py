import random
import time
def testPoprawnościDanych(liczby):
    iloscliczb = len(liczby)
    if iloscliczb != 6:
        return 1
    for i in range(iloscliczb):
        j = i + 1
        for z in range(j, iloscliczb):
            if (liczby[i] == liczby[z]):
                return 2
        if (liczby[i] < 1 or liczby[i] > 49):
            return 3
def wylosowanieLiczb():
    random.seed(time.time())
    wylosowaneLiczby = []
    while(len(wylosowaneLiczby)<6):
        liczba = random.randint(1,49)
        if liczba not in wylosowaneLiczby:
            wylosowaneLiczby.append(liczba)
    return wylosowaneLiczby
def ileLiczbTrafionych(podaneLiczby,wylosowaneLiczby):
    iloscLiczb = len(podaneLiczby)
    wynik = 0
    for i in range(iloscLiczb):
        for j in range(iloscLiczb):
            if podaneLiczby[i] == wylosowaneLiczby[j]:
                wynik+=1
    return wynik
