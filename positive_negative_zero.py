# Write a python program to check whether a number is negative, positive or zero.

num=input("enter no: ")
if int(num)>=0:
    print(num,"is positive no")
elif int(num)<0:
    print(num,"is negative no")
elif int(num)==0:
    print(num,"is zero")
else:
    print("Error")