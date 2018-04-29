class Calculation:
    _wynik = 0

    def __init__(self, l1 = 1, l2 = 2):
        self.liczba1 = l1
        self.liczba2 = l2

    def wyswietl(self):
        print(self.liczba1, self.liczba2)

    def add(self):
        print(self.liczba1 + self.liczba2)

    def subtract(self):
        print(self.liczba1 - self.liczba2)

    def divide(self):
        print(self.liczba1 / self.liczba2)

    def multiply(self):
        self.wynik = self.liczba1 * self.liczba2
        return self.wynik

class Show(Calculation):
    def printuj(self):
        print(Calculation.multiply(self))


kalkulacje = Calculation(12,22)
kalkulacje.multiply()
show = Show()
show.printuj()
