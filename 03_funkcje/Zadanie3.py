napis = "Ala ma <kota>, a kot ma Alę"

count = napis.count(litera)

def policz_znaki(tekst, start='<', end='>'):
    licznik = 0
    poziom = 0
    for znak in tekst:
        if znak == start:
            poziom += 1
        elif znak == end:
            poziom -= 1
        else:
            licznik += poziom
    return licznik

# # define string
# string = "Python is awesome, isn't it?"
# substring = "i"
#
# # count after first 'i' and before the last 'i'
# count = string.count(substring, 8, 25)
#
# # print count
# print("The count is:", count)

def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki('') == 0

def test_policz_znaki_w_napisie_bez_znacznikow():
    assert policz_znaki('ala ma kota') == 0

def test_policz_znaki_w__napisie_bez_znacznikow():
    assert policz_znaki('ala <ma> kota') == 2

def test_policz_znaki_wiele_poziomow_zaglebienia():
    assert policz_znaki('ala <m<a>> kota') == 3

def test_policz_znaki_inne_znaczki():
    assert policz_znaki('ala [m[a]] kota', "[", "]") == 3

# licznik = 0
# czy_zliczac = False
# for znak in napis:
#     if znak == "<":
#         czy_zliczac = True
#         continue
#     elif znak == ">":
#         czy_zliczac = False
#     if czy_zliczac:
#         licznik += 1
#
# print(f'Liczba liter w nawiasach to: {licznik}')