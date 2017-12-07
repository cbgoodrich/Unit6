#Charlie Goodrich
#12/07/17
#palindromes.py - finds the palindromes in a dictionary

dictionary = open("engmix.txt")

for word in dictionary:
    word = word.strip()
    reverse = list(word).reverse()
    if list(word) == reverse:
        print(word)


