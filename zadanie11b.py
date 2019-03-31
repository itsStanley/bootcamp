dane = input('Wprowadź lidzby rozdzielając je przecinkiem')
unikalne_liczby = {int(el) for el in dane.split(',')}
unikalne_liczby.add(int(dane))
print(f"Unikalnych liczb: {len(unikalne_liczby)}")
print(f"Z czego parzystych w przedziale 0-100 jest {len(unikalne_liczby & set(range(0, 101, 2)))}")