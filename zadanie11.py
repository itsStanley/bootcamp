unikalne_liczby = set()
while True:
    dana = input('Wprowadź lidzby ')
    if dana == "k":
        break
    unikalne_liczby.add(int(dana))
print(f"unikalnych liczb: {len(unikalne_liczby)}")
print(f"Z czeego parzystych w przedziale 0-100 jest {len(unikalne_liczby & set(range(0, 101, 2)))}")