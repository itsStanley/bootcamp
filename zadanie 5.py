liczby = [5, 2, 1, 4, 3]
#i_max = liczby.index(max(liczby))
#i_min = liczby.index(min(liczby))
#temp = liczby[i_min]
#liczby[i_min] = liczby[i_max]
#liczby[i_max] = temp
temp_max = liczby[0]
temp_min = liczby[0]
#liczby[i_min], liczby[i_max] = liczby[i_max], liczby[i_min]
for el in liczby:
    if el > temp_max:
        temp_max = el
    if el < temp_min:
        temp_min = el
for el in range(len(liczby)):
    if liczby[el] > temp_max:
        temp_max = liczby[el]
        temp_max_i = el
    if liczby[el] < temp_min:
        temp_min = liczby[el]
for i, v in enumerate(liczby):
    print(i, v)

#liczby[i_min] = liczby[0]
#liczby[i_max] = liczby[-1]
print(liczby)
assert liczby == [1, 2, 3, 4, 5]