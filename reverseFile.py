#Charlie Goodrich
#12/06/17
#reverseFile.py - asks the user for a file, reverses the lines in the file

file = open(""+input("Enter a file: ")+"")

fileList = []

for line in file:
    fileList.append(line)
    
fileList.reverse()

for line in fileList:
    print(line.strip())
