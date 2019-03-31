def dodaj(*args):
    print(args)
    return sum(args)
dodaj(1,2,3,4,5,6,7,7)
def test_dodaj
    assert dodaj(1, 2) == 3
    assert dodaj(1, 2, 3, 4, 5) == 15