# Project's Title: Reverse-Vowels-of-a-String #

### Project's Description

#### What does the function do?
* This is a  function to reverse the vowels of a string.

#### Why use Python?
* It use a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding
* The vowels has to admit uppercase and lowercase vowels ("y" its not considered as a vowel).
* The reverse works as the first vowel changes with the last vowel and so on until there is no more pairs.

#### How to run the function
* The function ask for a string with a lenght of more than one, and no more than 3 * 10^5.

```python
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
```

### Link to the source of the exercises
* https://leetcode.com/problems/reverse-vowels-of-a-string/
