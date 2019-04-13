def add(*args):
    dims = set()

    for m in args:
        len_rows, len_cols = len(m), len(m[0])
        dims.add((len_rows, len_cols))
        len_cols_ = set()
        for row in m:
            len_cols_.add(len(row))
        if len(len_cols_) > 1:
            raise ValueError("Liczba kolumn w wierszach jest różna")

    if len(dims) > 1:
        raise ValueError("Wymiary macierzy się nie zgadzają")


    output = []
    for i in range(len_rows):
        row = []
        for j in  range(len_cols):
            suma = sum([ m[i][j] for m in args])
            row.append(suma)
        output.apend(row)
    return output


m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]

add(m1, m2)