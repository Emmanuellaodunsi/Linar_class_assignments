#creating an algorithm to solve the quadratic equation 
#x=-b+-(b**2-4ac*(0.5))/2a

#start
#input the value for a,b,c
value_a=float(input("Emter the value for a:"))
Value_b=float(input("Enter the value for b:"))
Value_c=float(input("enter the value for c:"))

#first....break the equation down by solving the numerator (b**2-4ac*(0.5))
#calculate the square of value b
Value_1=Value_b**2

#multiply a by c
Value_2=value_a*Value_c
Value_3=4*Value_2

#subract b**2 from 4ac
Value_4=Value_1-Value_3

#calculate the square root of b**2-4ac **0.5
Value_5=Value_4**0.5

#now the subraction of -b+-(b**2-4ac*(0.5))
X_1=-Value_b+Value_5
X_2=+Value_b-Value_5

#now solving the denominator (2a)
#multiply 2**a
Value_6=2*value_a

#calculate the division of the numerator and denominator
Value_x=X_1/Value_6
Value_y=X_2/Value_6

#print out the solution to the quadratic equation
print("x=",-Value_x)
print("x=",Value_y)
#end