#Charlie Goodrich
#12/08/17
#homework.py - the homework sheet boi

dictionary = open("engmix.txt")

def wordAsk():
    word = input("Enter a word: ")
    
    counter = 0
    for words in dictionary:
        if words.strip() == word:
            print("Your word is in the dictionary")
            counter += 1
            break
    if counter == 0:
        print("Your word is not in the dictionary")
        

def numberWord():
    number = int(input("Enter a number word: "))
    
    wordList = []
    for words in dictionary:
        word = words.strip()
        wordList.append(word)
    print("The number", number, "word in the dictionary is","'"+wordList[number-1]+"'")
    
def exclaimationPoint():
    file = open("howManyWords.py")
    for line in file:
        print(line.strip()+"!")

def letterSearch():
    letter = input("Enter a letter: ")
    
    letterCount = 0
    word = ""
    for words in dictionary:
        loopCount = words.count(letter)
        if loopCount > letterCount:
            letterCount = loopCount
            word = words
    print("The word with the most", letter+"'s is", word)


