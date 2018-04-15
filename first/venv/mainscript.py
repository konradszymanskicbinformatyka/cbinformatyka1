import gra
import random
import time
random.seed(time.time())
komp=['kamien','papier','nozyce']
wyjsc=''
ty=0
ja=0
while (wyjsc != 'n'):
    check=random.choice(komp)
    wybor=input('Podaj co wybierasz \nkamien papier czy nozyce')
    wynik = gra.gierka(wybor,check)
    print('komputer wybrał %s %s' % ( check,wynik))
    if wynik == 'wygrywasz':
        ty=ty+1
    elif  wynik == 'przegrywasz':
        ja=ja+1
    print('wynik ty:%s komputer:%s' % (ty, ja))
    wyjsc = input('Grasz dalej t tak n nie')


