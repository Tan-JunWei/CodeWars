# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    text_list = text.split(" ")
    pig_latin = ""
    for word in text_list:

        if word[0].isalpha(): #check if its an alphabet to distinguish from any punctuation marks
            first_letter = word[0]
            new_word = word[1:]
            new_word += first_letter + "ay"

        else:
            new_word = word

        pig_latin += new_word + " "
    pig_latin = pig_latin.strip()

    return pig_latin

pig_it('Hello world !')



'''
def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)
'''