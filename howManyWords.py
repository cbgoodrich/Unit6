#Charlie Goodrich
#12/06/17
#howManyWords.py - shows how many words there are of a given length

dictionary = open("engmix.txt")

def howManyWords(count): #where count is the number of letters in a word
    wordCount = 0
    for word in dictionary:
        if len(word.strip()) == count:
            wordCount += 1
    
    print("There are", wordCount, "words that have", count, "letters")
    
howManyWords(1)
    
