def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True
def test_czy_jest_pierwsz_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(3) is True
    assert czy_jest_pierwsza(5) is True
    assert czy_jest_pierwsza(17) is True
    assert czy_jest_pierwsza(2) is True
def test_czy_jest_pierwsz_dla_liczby_niepierwszej():
    assert czy_jest_pierwsza(12) is False
    assert czy_jest_pierwsza(8) is False
