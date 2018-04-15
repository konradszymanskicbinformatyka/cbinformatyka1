import random
import time
random.seed(time.time())
imiona = ["anna","olka","konrad","patryk","piotrek","aśka","damian","jacek","kamila","agata"]

def randomizer():
    wynik=random.choice(imiona)
    return wynik
