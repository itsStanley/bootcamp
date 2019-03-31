def formatuj(*args, **kwargs):
    zlaczone = "\n".join(args)

    for k in kwargs:
        zlaczone = zlaczone.replace(f'${k}', str(kwargs[k]))

    return zlaczone





# x = formatuj('koszt $cena PLN', 'kwota $brutto brutto', cena=10, brutto=(cena*1.23))
#
# print(f'koszt () PLN \ kwota () brutto )


assert x == "koszt 10 PLN\nkwota 12.3 brutto"