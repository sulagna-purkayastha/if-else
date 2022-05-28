# Write a python program to check whether a year is leap year or not.

year=int(input("enter no: "))
if year%4==0 and year%100==0 and year%400==0:
    print(year,"is leapyear")
else:
    print(year,"is not leapyear")