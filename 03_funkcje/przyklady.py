def power(a, b=2):
    return a**b

print(power(2, 4))
print(power(2))

def say_hello(name)



def parent():
    a = 1
    print("Print z funkcji parent")
    def first_child():
        print("Printuję z first_child")
        print("Printuję a funkcji parent", a)
    def second_child()
        print("Printuję z second_child")

    print(locals())
    print(globals())

    first_child()
    second_child()

print('-'*90)
print(locals())
print(globals())
print('-'*90)
parent()