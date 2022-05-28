# Write a python program to check whether a character is an alphabet or not.

char=input("enter character: ")
if char>="A" and char<="Z" or char>="a"and char<="z":
    print(char,"is character")
else:
    print(char,"is not character")