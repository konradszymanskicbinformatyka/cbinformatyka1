def gierka(wybor,check):
    wynik=''
    if check==wybor:
        wynik="remis"
        return wynik
    if check=='kamien':
        if wybor == 'papier':
            wynik="wygrywasz"
        # elif wybor == 'nozyce':
        #     wynik='przegrywasz'
    if check=="papier":
        if wybor == 'nozyce':
            wynik="wygrywasz"
        # elif wybor == 'kamien':
        #     wynik='przegrywasz'
    if check=="nozyce":
        if wybor == 'kamien':
            wynik="wygrywasz"
        # elif wybor == 'papier':
        #     wynik='przegrywasz'
    if wynik=='' :
        wynik='przegrywasz'
    return wynik