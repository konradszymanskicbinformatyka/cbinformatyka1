class Liczby:
    def __init__(self,l1,l2):
        self.number1 = l1
        self.number2 = l2

    def __add__(self, liczbyklasa):
        wynik = self.number1 + liczbyklasa.number1
        return Liczby(wynik, 0)


class Stringi:
    def __init__(self,s1,s2):
        self.string1 = s1
        self.string2 = s2

    def __repr__(self):
        linked = self.string1 + self.string2
        return "połączone stringi to {0}".format(linked)



class Mieszne:
    def __init__(self,m11,m22):
        self.mixed1 = m1
        self.mixed2 = m2


L1 = Liczby(4,2)
L2 = Liczby(5,3)
L3 = L1 + L2
print(L3.number1)

S1 = Stringi('ala ma', 'Kota')
print(S1)