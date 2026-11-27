
amount = float(input("Enter purchase amount: "))

if amount < 2000:
    discount = 5
elif amount <= 5000:
    discount = 10
else:
    discount = 15

discount_amount = amount * discount / 100
after_discount = amount - discount_amount

gst = after_discount * 5 / 100
final_amount = after_discount + gst

print("\n----- BILL DETAILS -----")
print("Purchase Amount:", amount)
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Amount After Discount:", after_discount)
print("GST (5%):", gst)
print("Final Amount:", final_amount)
