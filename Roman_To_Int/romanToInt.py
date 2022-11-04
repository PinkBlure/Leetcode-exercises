class Solution:

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

        index = 0
        number = 0
        aux = 0
        while index < len(s):

            if (index == len(s) - 1) or \
                    (switch_romanToInt.get(s[index]) > switch_romanToInt.get(s[index+1])):
                if aux == 0:
                    number += switch_romanToInt.get(s[index])
                else:
                    number += switch_romanToInt.get(s[index]) - aux
                    aux = 0
            else:
                aux = switch_romanToInt.get(s[index])

            index += 1

        return number
