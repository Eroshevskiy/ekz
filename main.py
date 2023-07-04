def together_ekz(list1, list2):
    return set(list1).intersection(list2)

ekzamen = ['neiron',
    'detec',
    'video',
    "otchet"

]
zadanie = [
    'neiron',
    'detec',
    "py"
    ]

together_ekzzad = together_ekz(ekzamen, zadanie)
for ekz in together_ekzzad:
    print("Хочу 5 по -",ekz)