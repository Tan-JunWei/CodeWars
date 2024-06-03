# Implement a function which behaves like the uniq command in UNIX.

# It takes as input a sequence and returns a sequence in which all duplicate elements following 
# each other have been reduced to one instance.

# Example:

# ["a", "a", "b", "b", "c", "a", "b", "c"]  =>  ["a", "b", "c", "a", "b", "c"]

def uniq(seq): 
    if len(seq) > 0: #check if list is empty 
        result = [seq[0]] #initialise the list, by adding the first element into "result" list,
                          #since first element will always be include in the result.

        for i in range(1,len(seq)): # use a for loop starting at index 1 to iterate through the remaining list
            if seq[i] != result[-1]: #if seq[i] is not equal to the last character in the "result" list, append
                result.append(seq[i])
        return result
    
    else:
        return [] #return empty list if empty list was given as arg
uniq(["a", "a", "b", "b", "c", "a", "b", "c"])