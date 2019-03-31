print([x/10 for x in range (11)])

print({(x, x**2, x**3) for x in range(11)})

zbior_napisow = ('jeden', 'dwa', 'trzy')
print({x: len(x) for x in zbior_napisow})