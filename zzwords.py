#Charlie Goodrich
#12/06/17
#zzwords.py - prints all the words from the dictionary that have 'zz' in them

dictionary = open("engmix.txt")

for word in dictionary:
    if "zz" in word:
        print(word.strip())
