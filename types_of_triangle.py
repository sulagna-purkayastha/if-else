# Write a python program to check whether the triangle is equilateral, isosceles or
# scalene triangle.

length_1= int(input("enter length: "))
length_2= int(input("enter next length: "))
length_3= int(input("enter next length: "))
if length_1==length_2 and length_2==length_3 and length_3==length_1:
    print("This triangle is Equilateral")
elif length_1==length_2 or length_1==length_3 or length_2==length_3:
    print("This triangle is Isosceles")
elif length_1!=length_2 and length_2!=length_3 and length_1!=length_3:
    print("This triangle is Scalene")
else:
    print("This is not a triangle")