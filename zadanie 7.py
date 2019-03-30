napis = input('Podaj napis: ')
SAMOGŁOSKI = ('a', 'e', 'i', 'o', 'u', 'y')
SAMOGŁOSKI = "aeiouy"
licznik = 0
for litera in napis.lower():
    if litera in SAMOGŁOSKI:
        licznik += 1
        pass
print(f'Liczba samogłosek w tekście to: {licznik}')