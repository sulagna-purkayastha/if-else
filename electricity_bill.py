# Write a python program to input electricity unit charges and calculate total electricity 
# bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit= int(input("enter unit charge: "))
if unit>=1 and unit<=50:
    total_bill= unit*0.50+20/100
    print("total bill=",total_bill)
elif unit>50 and unit<=151:
    total_bill= unit*0.75+20/100
    print("total bill=",total_bill)
elif unit>151 and unit<=251:
    total_bill= unit*1.20+20/100
    print("total bill=",total_bill)
elif unit>250:
    total_bill= unit*1.50+20/100
    print("total bill=",total_bill)
else:
    print("Not generate")