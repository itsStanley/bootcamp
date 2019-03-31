def wiecej_niz(tekst, prog):
    rezultat = set()
    licznik_liter = {}
    for znak in tekst:
        licznik_liter[znak] = licznik_liter.get(znak, 0) + 1
    for znak in licznik_liter:
        if licznik_liter[znak] > prog:
            rezultat.add(znak)
    return rezultat
def wiecej_niz(tekst, prog):
    rezultat = set()
    for znak in set(tekst):
        if tekst.count(znak) > prog:
            rezultat.add(znak)
    return rezultat
def wiecej_niz(tekst, prog):
    return {znak for znak in tekst if tekst.count(znak) > prog}

print(f"wpisz tekst aby policzyć litety [tekst])
def test_wiecej_niz_dla_pustego_napis():
    assert wiecej_niz('', 1) == set()
def test_wiecej_niz_dla_nie_pustego_napis():
    assert wiecej_niz('abbasas', 2) == {'a'}