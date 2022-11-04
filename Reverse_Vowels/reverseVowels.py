def reverseVowels(s: str) -> str:

    def listToString(array_list):

        aux_string = ""

        for character in array_list:
            aux_string += character

        return aux_string

    listOfVowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    new_list = list(s)

    pos_start = 0
    pos_end = len(new_list)-1

    while pos_start < pos_end:

        while (new_list[pos_start] not in listOfVowels) and (pos_start != (len(new_list)-1)):
            pos_start += 1

        while (new_list[pos_end] not in listOfVowels) and (pos_end != 0):
            pos_end -= 1

        if pos_start < pos_end:

            aux = new_list[pos_start]
            new_list[pos_start] = new_list[pos_end]
            new_list[pos_end] = aux

            pos_start += 1
            pos_end -= 1

    return listToString(new_list)
