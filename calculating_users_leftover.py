#write a script that will calculate users leftover by asking for the users monthly salary and monthly expenses
#Asking for the users name
Name=input("Enter your name:\n")
#Ask the user for the monthly salary
monthly_salary=float(input("Enter your monthly salary:\n"))

#Ask the user for the monthly expenses
monthly_expenses=float(input("Enter your monthly expenses:\n"))

#Now calculate the user leftover by deducting the monthly expenses from the monthly salary
leftover=monthly_salary-monthly_expenses

#print out the leftover
print("Dear",Name,"your leftover for for this month salary is:",leftover)