# Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not 
# repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the 
# string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the 
# correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("");

# † Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode 
# character.

def first_non_repeating_letter(s):
    non_repeating_list = []
    for char in s:
        s = s.lower()
        count = s.count(char)
        if count == 1:
            non_repeating_list.append(char)
    return non_repeating_list[0] if len(non_repeating_list) > 0 else ''

first_non_repeating_letter('moonmen')