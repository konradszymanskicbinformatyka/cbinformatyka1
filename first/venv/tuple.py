t1 = (2,5,8,1,3)
t2 = (3.5,'a',5,'b')
t3 = t1+ t2
t4 = 2 * t3
# t2[1]=2
lenght = len(t2)
index = t4.index(2)
c = t4.count(5)
lista = list(t4)
lista1 = [3,5,3,2]
tupleme = tuple(lista1)
print('suma to: %s dlugosc to %s ilosc powtorzen to %s mnożenie to %s' % (t3, lenght, c, t4))
print('to samo suma to', t3, 'dlugosc to', lenght, 'index to ', index)
print(lista)
print(tupleme)