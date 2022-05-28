# Write a python program to input all sides of a triangle and check whether the triangle is
# valid or not.

side_1= int(input("enter first side: "))
side_2= int(input("enter second side: "))
side_3= int(input("enter third side: "))
if side_1+side_2>side_3 or side_2+side_3>side_1 or side_3+side_1>side_2:
    print("this triangle is valid")
else:
    print("this triangle is not valid")