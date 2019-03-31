def splaszcz(lista):
    rezultat = []
    for el in lista:
        if isinstance(el, list):
            for e in splaszcz(el)
            rezultat.append(e)

        else:
            rezultat.append(el)
    return rezultat

# lista = ([1, 2, [3, 4, [5]]])
# def splaszcz(container):
#     for i in container:
#         if isinstance(i, (list,tuple)):
#             for j in splaszcz(i):
#                 yield j
#         else:
#             yield i
# print (list(splaszcz(lista))
#
# def flatten(sequence):
#     if isinstance(sequence, (list, tuple)):
#         result = []
#         if sequence: # niepusta lista/tupla
#             # rekurencja
#             result += flatten(sequence[0]) # spłaszcz mi [0] a wynik (sam) dołącze do już posiadanego w result
#             result += flatten(sequence[1:]) # spłaszcz mi [1:] a wynik (sam) dołącze do już posiadanego w result
#         return result # (sam) zwracam cały spłaszczony kawałek (lub pustą listę)
#     else: # warunek stopu
#         return [sequence] # nie ma już co spłaszczać więc przekazuje wynik jako listę

# def splaszcz():
#     rezultat = []
#     splaszcz([1, 2, [3, 4, [5]]])
#     if "[":
#         return ""
#     elif "]":
#         return ""
# print(splaszcz())

def test_splasz_pusta_lista():
    assert splaszcz([]) == []

def test_splasz_pusta_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_splasz_zagnieżdżona_lista():
    assert splaszcz([1, 2, [3, 4, [5]]]) == [1, 2, 3, 4, 5]
