#Charlie Goodrich
#12/11/17
#warmup16.py - finds the words in the dictionary that start with first initial, end with last initial

dictionary = open("engmix.txt")

firstName = input("Enter your first name: ").lower()
lastName = input("Enter your last name: ").lower()

for words in dictionary:
    word = words.strip()
    if word != "":
        if word[0] == firstName[0] and word[-1] == lastName[0]:
            print(word)
