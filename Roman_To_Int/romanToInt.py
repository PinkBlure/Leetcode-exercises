def romanToInt(s: str) -> int:

    switch_romanToInt = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number = 0
    aux = 0

    for index, value in enumerate(s):

        if (index == len(s) - 1) or \
                (switch_romanToInt.get(value) >= switch_romanToInt.get(s[index + 1])):
            if aux == 0:
                number += switch_romanToInt.get(value)
            else:
                number += switch_romanToInt.get(value) - aux
                aux = 0
        else:
            aux = switch_romanToInt.get(value)

    return number
