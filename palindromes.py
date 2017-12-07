#Charlie Goodrich
#12/07/17
#palindromes.py - finds the palindromes in a dictionary

dictionary = open("engmix.txt")

for word in dictionary:
    word = word.strip()
    setUp = list(word)
    setUp.reverse()
    if list(word) == setUp:
        print(word)

