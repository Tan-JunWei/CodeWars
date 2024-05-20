# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters
# reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when 
# more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    
    wordlist = sentence.split()
    for word in wordlist:
        if len(word) >= 5:
            index = wordlist.index(word)
            wordlist.remove(wordlist[index])
            new_word = word[::-1]
            wordlist.insert(index,new_word)
    
    new_wordlist = " ".join(wordlist)
    return new_wordlist

spin_words("This sentence is a sentence")