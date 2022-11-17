#Write a numpy program to capitalize the first letter, lower case, upper case and swap case of all the elements of a given array.
import numpy as np
word_list = np.array(input().split())
print(np.char.capitalize(word_list))
print(np.char.lower(word_list))
print(np.char.upper(word_list))
print(np.char.swapcase(word_list))
