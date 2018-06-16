import threading
import time

def add(a,b):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        wynik = a + b
        print("name: " + name + " " +time.ctime(time.time()))

def print_time(name,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("name: " + name + " " +time.ctime(time.time()))

def print_time(name,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("name: " + name + " " +time.ctime(time.time())

def print_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("name: " + name + " " + time.ctime(time.time()))

def print_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("name: " + name + " " + time.ctime(time.time()))



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

t1 =threading.Thread(target=print_time,args=('watek1',2))
t2 =threading.Thread(target=print_time,args=('watek2',1))
t3 =threading.Thread(target=print_time,args=('watek3',4))
t1.start()
t2.start()
t3.start()