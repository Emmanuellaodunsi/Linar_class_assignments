'''A python code that calculate the take home balance for a staff member,
 prints the equivalent tax deduction from their salary and then prints the final take home balance'''
#Get the staff salary.
salary=float(input("Enter the salary amount:\n"))
#Constant Tax percentage
tax_percentage=0.87/100
#Calcualate the staff member's tax deduction.
tax_deduction=salary*tax_percentage
#Calcualte the staff member's take home balance.
take_home_balance=salary-tax_deduction
#Print the staff member's tax deduction.
print("The equivalent tax deduction is:",tax_deduction)
#Print the staff member's take home balance.
print("The staff member's take-home balance is:",take_home_balance)
