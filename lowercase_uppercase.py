# Write a python program to check whether a character is uppercase or lowercase alphabet.

char= input("enter character: ")
if char>="A" and char<="Z":
    print(char,"is uppercase")
elif char>="a" and char<="z":
    print(char,"is lowercase")
else:
    print("please enter character ,\U0001F910")