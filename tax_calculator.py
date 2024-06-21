income = float(input("Enter the annual income: "))

#
# Write your code here.
base_income = 85528
low_tax = 556.02
high_tax = 14839.02

if(income <= base_income):
    tax = ((18/100) * income) - low_tax
else:
    diff = income - base_income
    tax = high_tax + ((32/100) * diff)
if(tax < 0):
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
