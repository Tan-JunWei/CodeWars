# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters 
#can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


def scramble(s1, s2):
    
    for char in set(s2):
        if s2.count(char) > s1.count(char):
            return False
        
    return True

'''
def scramble(s1,s2):
    return all(s1.count(c) >= s2.count(c) for c in set(s2))

The all() function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function also returns True.
list = []
print(all(list)) #True

'''