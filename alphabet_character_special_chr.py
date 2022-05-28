# Write a python program to input any character and check whether it is alphabet, digit
# or special character.

chr=input("enter character: ")
if chr>="A" and chr<="Z" or chr>="a" and chr<="z":
    print(chr,"is alphabet")
elif chr>="0" and chr<"0":
    print(chr,"is digit")
else:
    print(chr,"is special character")