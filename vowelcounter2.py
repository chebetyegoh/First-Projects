# using regular expressions

import re


def vowel_counter(string):
    vowels = re.findall('a|e|i|o|u', string)
    print(vowels)
    number_vowels = len(vowels)
    print(number_vowels)


string = input("Enter the string that you would like to get the number of vowels in it:")
string1 = string.lower()
vowel_counter(string1)
