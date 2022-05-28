# Write a python program to input marks of five subjects Physics, Chemistry, Biology,
# Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A Percentage >= 80% : Grade B Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D Percentage >= 40% : Grade E Percentage < 40% : Grade F

physics= int(input("enter physics mark: "))
chemistry= int(input("enter chemistry mark: "))
biology= int(input("enter biology mark: "))
math= int(input("enter math mark: "))
computer= int(input("enter computer mark: "))
if (physics+chemistry+biology+math+computer)/500*100>= 90:
    print("Grade A")
elif (physics+chemistry+biology+math+computer)/500*100>=80:
    print("Grade B")
elif (physics+chemistry+biology+math+computer)/500*100>=70:
    print("Grade C")
elif (physics+chemistry+biology+math+computer)/500*100>=60:
    print("Grade D")
elif (physics+chemistry+biology+math+computer)/500*100>=40:
    print("Geade E")
else:
    print("Grade F")