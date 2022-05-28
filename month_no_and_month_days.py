# Write a python program to input the month number and print the number of days in that month.

month_num= int(input("enter month number: "))
if month_num==1 or month_num==3 or month_num==5 or month_num==7 or month_num==8 or month_num==10 or month_num==12:
    print("31 days")
elif month_num==4 or month_num==6 or month_num==9 or month_num==11:
    print("30 days")
elif month_num==2:
    print("28/29 days")
else:
    print("enter correct input")