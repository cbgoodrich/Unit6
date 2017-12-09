#Charlie Goodrich
#12/07/17
#longShort.py - finds the longest and shortest words for each letter

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

wordList = [""]*26

dictionary = open("engmix.txt")

for words in dictionary:
    print(alphabet.index(words[0]))
    break
