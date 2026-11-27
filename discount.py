amount = float(input("Enter purchase amount: "))
if amount < 2000:
    discount = 5
elif amount <= 5000:
    discount = 10
else:
    discount = 15
discount_amount = amount * discount / 100
final_amount = amount - discount_amount
print("\n----- BILL DETAILS -----")
print("Purchase Amount:", amount)
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
