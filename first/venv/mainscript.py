import gra
import random
import time
random.seed(time.time())
komp=['kamien','papier','nozyce']
check=random.choice(komp)
wybor=input('Podaj co wybierasz \nkamien papier czy nozyce')
print('komputer wybrał %s %s' % ( check,gra.gierka(wybor,check)))


