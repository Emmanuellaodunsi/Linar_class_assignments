#Python algorithm to solve some quadratic equations:
print("python algorithm to solve some quadratic equations")
#p=3+(4v*a)
#start
#ask the user to input the value for v
value1=int(input("enter the value for v:"))
#ask the user to input the value for a
value2=int(input("enter the value for a"))
#Multiply 4 by the value for v
value_1=4*value1
#Multiply the value 4v with the value for a
value_2=value_1*value2
#add the value 3 with the solution for 4v*a
solution=3+value_2
#print the solution to the equation
print("p=",solution)
#end

#a=3.14r*2
#start
#ask the user to input the value for r
R=int(input("enter the value for r:"))
#calulate the square of the value for r
VALUE=R*2
#multiply the value 3.14 with the square of r
Value=3.14*VALUE
solution2=Value
#print the solution to the equation
print("a=",solution2)
#end


#D=b*2-4ac
#start
#ask the user to input the value for a,b,c
VALUE1=int(input("enter the value for a"))
VALUE2=int(input("enter the value for b:"))
VALUE3=int(input("enter the value for c:"))
#calculate the square of b
Term1=VALUE2*2
#multiply the value for a with the value for c
Term2=VALUE1*VALUE3
#multiply the value 4 with the solution to a*c
Term3=4*Term2
#subtract the solution to the square of b from the solution to the mutiplication of 4*(a*c)
solution3=Term1-Term3
print("D=",solution3)
#end

