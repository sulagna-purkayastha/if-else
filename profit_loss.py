# Write a python program to calculate profit or loss.

cost_price= int(input("enter cost price: "))
selling_price= int(input("enter selling price: "))
if cost_price<selling_price:
    print("profit")
elif cost_price>selling_price:
    print("loss")
else:
    print("no profit, no loss")