# A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000.
# Ask the user for quantity, Suppose, one unit will cost 100. Judge and print total cost for
# user.

quantity= int(input("enter purchased quantity"))
if quantity*100>1000:
    total_cost= (quantity*100)-10/100
    print("Total cost with 10% discount=",total_cost)
else:
    print("Total cost without discount=",quantity*100)