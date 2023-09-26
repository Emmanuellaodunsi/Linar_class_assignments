#A python code that calculate the take home balance for a staff member 
#print the equivalent tax deduction from their salary ,and then print the final take home balance

salary=float(input("Enter the salary amount"))
tax_percentage=0.87
tax_deduction=salary*(tax_percentage/100)
take_home_balance=salary-tax_deduction
print("The equivalent tax deduction is below:")
print(tax_deduction)
print("The take-home balance is below:")
print(take_home_balance)
