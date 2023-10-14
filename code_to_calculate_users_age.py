#write a script to calculate users age
#start
#Get user name
name=input("Enter your name:\n")
#Get the users birthyear
birthyear=int(input("Enter the birthyear:\n"))
#Get the current year
current_year=int(input("Enter the current year:\n"))
age=birthyear-current_year
print("Dear",name,"you are",age"years old")
#end