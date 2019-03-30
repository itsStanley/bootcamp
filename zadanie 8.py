napis = "Ala ma <kota>,  akot ma Alę"
licznik = 0
czy_zliczac = False
for znak in napis:
    if znak == "<":
        czy_zliczac = True
        continue
    elif znak == ">":
        czy_zliczac = False
    if czy_zliczac:
        licznik += 1

print(f'Liczba liter w nawiasach to: {licznik}')