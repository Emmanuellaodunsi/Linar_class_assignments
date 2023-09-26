#Voting 
Age=int(input("How old are you?"))
if Age >= 18:
    print("You are eligible to vote")
else:
    print("Wait till your are above 18")

 #Game
Game_score=int(input("Enter your game score:"))
if Game_score < 50:
    print("Game over!")
    print("Try again")
elif Game_score >=50:   
    print("Congratulation you passed")

#Battery percentage
Phone_battery_percentage=int(input("Enter your phone percentage:"))
if Phone_battery_percentage == 100:
    print("Battery full")
elif Phone_battery_percentage < 50:
    print("Battery low....")
else:
    print("battery almost full")

#bank balance
Bank_balance= 1000
Money_withdraw=int(input("How much do you want to withdraw?"))
if Money_withdraw> Bank_balance:
    print("Insufficient balance")
elif Bank_balance==Money_withdraw:
    print("Withdraw successful")
else:
    print("still have some money in account")

#facebook login
user_name= " Emmanuella"
password="emma1234"
User_Name=input("Enter your user name:")
Password=input("Enter your password:")
if User_Name== user_name: 
    Password== password
    print("Login successfull")
else:
    print("Incorrect login details")
