# Write a python program to input angles of a triangle and check whether triangle is
# valid or not.

angle_1=int(input("enter angle: "))
angle_2=int(input("enter angle: "))
angle_3=int(input("enter angle: "))
if angle_1+angle_2+angle_3==180:
    print("This triangle is valid")
else:
    print("This triangle is not valid")