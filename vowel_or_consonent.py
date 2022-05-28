# Write a python program to input any alphabet and check whether it is vowel or consonant.

chr= input("enter character: ")
if chr=="A" or chr=="a" or chr=="E" or chr=="e" or chr=="I" or chr=="i" or chr=="O" or chr=="o" or chr=="U" or chr=="u":
    print(chr,"is vowel")
elif chr>="A" and chr<="Z" or chr>="a" and chr<="z":
    print(chr,"is consonent")
else:
    print(chr,"not a character")