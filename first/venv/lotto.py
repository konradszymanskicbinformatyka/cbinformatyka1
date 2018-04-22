import funkcje
error = 0
while(error<4):
    otrzymaneLiczby = input('Podaj 6 wybranych prez ciebie liczb z zakresu od 1 do 49 oddzielonych spacja\n')
    listaLiczbZnaki = otrzymaneLiczby.split(' ')
    podaneLiczby = []
    for i in listaLiczbZnaki:
        podaneLiczby.append(int(i))
    error = funkcje.testPoprawnościDanych(podaneLiczby)
    if error == 2:
        print('liczby nie mogą się powtaezać')
    elif error == 1:
        print('podałeś niepoprawną ilość liczb')
    elif error == 3:
        print("liczby które podałeś wychodzą poza zakres")
    else :
        error = 5
wylosowaneLiczby=funkcje.wylosowanieLiczb()
wynik=funkcje.ileLiczbTrafionych(podaneLiczby,wylosowaneLiczby)
print('Dziękujemy za wzięcie udziału w losowaniu tym razem udało ci się trafić %s liczb' % (wynik))



