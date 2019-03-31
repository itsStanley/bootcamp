def sort_func(x):
    return x[1]

lista = [(2, "b"), (3, "a"), (1, "c")]

print(sorted(lista, key=sort_func))
print(sorted(lista, key=lambda x: x[0]))
# print(sorted(lista, reverse=True))

a = [1, 2, 3, 4, 5, 6, 7, 8]

def wybierz(dane):
    out = []
    for el in dane:
        if el%2 == 0:
            out.append(el)
    return out
pront(wybierz(a))

def podzielne_przez_2(x):
    return x%2 == 0

print(wybierz(a, podzielne_przez_2))

print(wybierz(a, lambda x: x>3))