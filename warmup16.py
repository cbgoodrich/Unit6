#Charlie Goodrich
#12/11/17
#warmup16.py - finds the words in the dictionary that start with first initial, end with last initial

dictionary = open("engmix.txt")

first_Name = input("Enter your first name: ")
last_Name = input("Enter your last name: ")

firstName = first_Name.lower()
lastName = last_Name.lower()

for words in dictionary:
    word = words.strip()
    if word != "":
        if word[0] == firstName[0] and word[-1] == lastName[0]:
            print(word)

