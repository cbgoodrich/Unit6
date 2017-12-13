#Charlie Goodrich
#12/13/17
#quiz.py - last quiz boi

dictionary = open("engmix.txt")

"""def program1():
    for words in dictionary:
        p_count = words.count("p")
        c_count = words.count("c")
        if p_count == 2 and c_count == 3:
            print(words.strip())
program1()
"""

"""def program2():
    r_counter = 0
    for word in dictionary:
        if word.strip() != "":
            if word[0] == "r":
                r_counter += 1
    print("There are", r_counter, "words that start with 'r'")
program2()
"""

"""def program3():
    num = int(input("Enter how many letters you want in your word: "))
    for words in dictionary:
        word = words.strip()
        if len(word) == num:
            print("Your word is", "'"+word+"'")
            break
program3()
"""

def program4():
    letter = input("Enter a letter: ")
    not_counter = 0
    for words in dictionary:
        if words != "" and letter not in words:
            not_counter += 1
    print("There are", not_counter, "words without the letter", "'"+letter+"'")
program4()

    
    