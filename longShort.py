#Charlie Goodrich
#12/07/17
#longShort.py - finds the longest and shortest words for each letter

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

longList = [""]*26
shortList = [""]*26

dictionary = open("engmix.txt")

for word in dictionary:
    if longList[alphabet.index(word[0])] == "":
        longList[alphabet.index(word[0])] = word
    else:
        if len(word) > len(longList[alphabet.index(word[0])]):
            longList[alphabet.index(word[0])] = word
    else:
        
    
