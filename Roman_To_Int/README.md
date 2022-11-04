# Project's Title: Roman To Int #

### Project Description ###

#### What does the function do? ####
* This is a function to convert roman number into integer.

#### Why use Python? ####
* It use a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding ####
* The Roman numeral system uses only seven symbols: I, V, X, L, C, D, and M. I represents the number 1, V represents 5, X is 10, L is 50, C is 100, D is 500, and M is 1,000.

* You can add numbers together by putting the symbols in descending order from left to right. You’d add all of the symbols’ individual values together to get the total value.

* You can also subtract numbers from each other by placing a symbol with a smaller value to the left of one with a larger value. The value of the smaller symbol is subtracted from that of the larger symbol to get the total value.

* The subtractive principle has a few specific limitations. For instance, a numeral can only be placed in front of the two numerals that are closest to it in the Roman numeral system. That is, I can only be placed before V and X. It can’t be placed before L, C, D, or M. Further, you can only place one smaller numeral in front of a larger one for subtractive purposes.

#### How to run the function ####
* The function asks for a string composed only of roman numerals, that is, I, V, X, L, C, D, and returns an integer of the decimal value of the roman numeral.

```python
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

```

### Link to the source of the exercises ###
* https://leetcode.com/problems/roman-to-integer/

### Credits ###
* https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
* https://www.dictionary.com/e/roman-numerals/#:~:text=The%20Roman%20numeral%20system%20uses,500%2C%20and%20M%20is%201%2C000.
