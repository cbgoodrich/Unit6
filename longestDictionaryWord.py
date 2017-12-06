#Charlie Goodrich
#12/06/17
#longestDictionaryWord.py - prints the longest word in the dictionary

dictionary = open("engmix.txt")

longest = 0
word = ""

for words in dictionary:
    length = len(words)
    if length > longest:
        longest = length
        word = words
        
print("The longest word is", word, "with", longest, "characters")
