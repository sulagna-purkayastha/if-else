# A student will not be allowed to sit in an exam if his/her attendance is less than 75%.
# Take following input from the user. Number of classes held. Number of classes attended.
# And print, percentage of class attended. Is the student is allowed to sit in the exam or not.

classes_held= int(input("enter number of classes held: "))
classes_attended= int(input("enter number of classes attended: "))
percentage= classes_attended/classes_held*100
if percentage<75:
    print("not allowed to sit for exam")
else:
    print("allowed to sit for exam")