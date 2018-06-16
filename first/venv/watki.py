import threading
import time
from datetime import date
today = str(date.today())


def add(name,delay):
    count = 0
    wynik = 0
    try:
        file = open(name, 'w')
    except PermissionError:
        print('nie masz uprawnień do utorzenie/otworzenia tego pliku')
    while count < 5:
        time.sleep(delay)
        count += 1
        wynik += 6
        try:
            file.write(today + ' ' + str(wynik) + '\n')
        except FileNotFoundError:
            print('Nie znalezionu takiego pluku')
    file.close()


def substruck(name,delay):
    count = 0
    wynik = 123
    try:
        file = open(name, 'w')
    except PermissionError:
        print('nie masz uprawnień do utorzenie/otworzenia tego pliku')
    while count < 5:
        time.sleep(delay)
        count += 1
        wynik -= 6
        try:
            file.write(today + ' ' + str(wynik) + '\n')
        except FileNotFoundError:
            print('Nie znalezionu takiego pluku')
    file.close()


def divide(name,delay):
    count = 0
    wynik = 256
    try:
        file = open(name, 'w')
    except PermissionError:
        print('nie masz uprawnień do utorzenie/otworzenia tego pliku')
    while count < 5:
        time.sleep(delay)
        count += 1
        wynik /= 2
        try:
            file.write(today + ' ' + str(wynik) + '\n')
        except FileNotFoundError:
            print('Nie znalezionu takiego pluku')
    file.close()


def multiply(name, delay):
    count = 0
    wynik = 1
    try:
        file = open(name, 'w')
    except PermissionError:
        print('nie masz uprawnień do utorzenie/otworzenia tego pliku')
    while count < 5:
        time.sleep(delay)
        count += 1
        wynik *= 6
        try:
            file.write(today + ' ' + str(wynik) + '\n')
        except FileNotFoundError:
            print('Nie znalezionu takiego pluku')
    file.close()


def power(name, delay, power_up):
    count = 0
    wynik = 0
    try:
        file = open(name, 'w')
    except PermissionError:
        print('nie masz uprawnień do utorzenie/otworzenia tego pliku')

    while count < 5:
        time.sleep(delay)
        count += 1
        result = 1
        for i in range(power_up):
            result = result * 3
        wynik = wynik + result
        try:
            file.write(today + ' ' + str(wynik) + '\n')
        except FileNotFoundError:
            print('Nie znalezionu takiego pluku')
    file.close()


t1 = threading.Thread(target=add,args=('add',1))
t2 = threading.Thread(target=substruck,args=('sunstruct',1))
t3 = threading.Thread(target=divide,args=('devide',1))
t4 = threading.Thread(target=multiply,args=('multiply',1))
t5 = threading.Thread(target=power,args=('power',1,3))
try:
    t1.start()
except Exception:
    print('Nie można było wystartować wątku')
try:
    t2.start()
except Exception:
    print('Nie można było wystartować wątku')
try:
    t3.start()
except Exception:
    print('Nie można było wystartować wątku')
try:
    t4.start()
except Exception:
    print('Nie można było wystartować wątku')
try:
    t5.start()
except Exception:
    print('Nie można było wystartować wątku')

