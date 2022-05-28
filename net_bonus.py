# A company decided to give a bonus of 5% to an employee if his/her year of service is more
# than 5 years. Ask users for their salary and year of service and print the net bonus amount.

year_of_service= int(input("enter year of service"))
salary= int(input("enter salary"))
if year_of_service>5:
    net_bonus= salary*5/100+salary
    print("Net bonus Amount=",net_bonus)
else:
    print("Salary without bonus=",salary)