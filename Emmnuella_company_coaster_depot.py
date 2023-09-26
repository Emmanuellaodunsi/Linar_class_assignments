name=input("Hello....pls enter your name:")
print("Hello",name, "Welcome to Emmanuella coaster biscult depot :)\nOnly coaster biscult available and we only sell in bulks...only cartons and half cartons")
print("There are two type of coaster biscuits avaliable...\nThe big coaster which cost 50 naira per pieces.\nThe small coaster which cost 20 naira each per pieces")
#constant price and quantities for the 50naira coaster type 
def calculate_total_amount(coaster_type,carton_quantity,carton_size):
    """This function helps in calculating total amount...
    its takes only 3 parameters: coaster_type, carton quantity, and cartoon size"""
    """
    This variable stores the
    constant price and quantities
      for the 50naira coaster type"""
    coaster_type1=50
    small_carton_50naira_price=4000
    medium_carton_50naira_price= 5500
    large_carton_50naira_price=7000
    small_carton_50naira_quantity=45
    medium_carton_50naira_quantity=75
    large_carton_50naira_quantity=110
    """This variable stores the 
    constant price and quantities
      for the 20naira coaster type"""
    coaster_type2=20
    small_carton_20naira_price=4000
    medium_carton_20naira_price= 5500
    large_carton_20naira_price=7000
    small_carton_20naira_quantity=65
    medium_carton_20naira_quantity=100
    large_carton_20naira_quantity=140
    #
    if coaster_type==coaster_type1 and carton_size=="small":
        total_cost1=int(carton_quantity)*int(small_carton_50naira_price/small_carton_50naira_quantity)
        print("The total amount to be paid for the small cartoon size of the 50naira coaster biscult is:",total_cost1)
        #After taking the first order from the customer the software asks if the customerwants to order more cartons of biscuits
        if carton_quantity==carton_quantity:
            number_of_carton1=input("Will you like to order more carton of coaster biscult? (yes or no):\n")
            if number_of_carton1=="yes":
            #if yes,the software asks the customer to specify the biscuit carton size and the number of cartons
                carton_size_a=input("Enter the carton size you would like to order (large,meduim,small):\n")
                carton_number1=input("Enter the number of carton you would like to order (1,2 or more):\n")
                if carton_size_a=="large":
                    global total_cost_1
                    total_cost_1=int(carton_number1)*int(large_carton_50naira_price)+total_cost1
                    print("The total amount to be paid for the large carton size and small carton size of the 50naira coaster biscult you ordered is:",total_cost_1)
                elif carton_size_a=="meduim":
                    total_cost_2=int(carton_number1)*int(medium_carton_50naira_price)+total_cost1
                    print("The total amount to be paid for the meduim carton size and small carton size of the 50naira coaster biscult you ordered is:",total_cost_2)
                elif carton_size_a=="small":
                    total_cost_3=int(carton_number1)*int(small_carton_50naira_price)+total_cost1
                    print("The total amount to be paid for the small carton size and large carton size of the 50naira coaster biscuit you ordered is",total_cost_3)
                    if number_of_carton1=="no": #if the customer dont want to order more cartons of biscult,the software prints out the total amount from the first order
                        print("Dear",name,"\nSince you are not ordering more carton of coaster biscuit,the total cost for the small carton size of 50naira coaster biscult you ordered still remain the same.\nThanks for patronizing Emmanuella coaster depot:)\nHave a nice day....Hope to see you next time")
    elif coaster_type==coaster_type1 and carton_size=="large": 
        total_cost2=int(carton_quantity)*int(large_carton_50naira_price/large_carton_50naira_quantity)
        print("The total amount to be paid for the large carton size of the 50naira coaster biscult you ordered is:",total_cost2)
        if carton_quantity==carton_quantity:
            number_of_carton2=input("Will you like to order more carton of coaster biscult? (yes or no):\n")
            if number_of_carton2=="yes":
                carton_size_b=input("Enter the carton size you would like to order(large,meduim,small):\n")
                carton_number2=input("Enter the number of carton you would like to order  (1,2 or more):\n")
                if carton_size_b=="large":
                    total_cost_4=int(carton_number2)*int(large_carton_50naira_price)+total_cost2
                    print("The total amount to be paid for the large cartons size of the 50naira coaster biscult you ordered is:",total_cost_4)
                elif carton_size_b=="meduim":
                    total_cost_5=int(carton_number2)*int(medium_carton_50naira_price)+total_cost2
                    print("The total amount to be paid for the meduim carton size and large carton size of the 50naira coaster biscult you ordered is:",total_cost_5)
                elif carton_size_b=="small":
                    total_cost_6=int(carton_number2)*int(small_carton_50naira_price)+total_cost2
                    print("The total amount to be paid for the small carton and large carton size of the 50naira coaster biscult you ordered is:",total_cost_6)
            if number_of_carton2=="no":
                print("Dear",name,"\nSince you are not ordering more carton of coaster biscuit,the total cost for the large carton size of 50naira coaster biscult you ordered still remain the same.\nThanks for patronizing Emmanuella coaster depot:)\nHave a nice day....Hope to see you next time")
    elif coaster_type==coaster_type1 and carton_size=="meduim": 
        total_cost3=int(carton_quantity)*int(medium_carton_50naira_price/medium_carton_50naira_quantity)
        print("The total amount to be paid for the meduim carton size of the 50naira coaster biscult is:",total_cost3)
        if carton_quantity==carton_quantity:
            number_of_carton3=input("Will you like to order more carton of coaster biscult? (yes or no):\n")
            if number_of_carton3=="yes":
                carton_size_c=input("Enter the carton size you would like to order (large,meduim,small):\n")
                carton_number3=input("Enter the number of carton you would like to order(1,2 or more):\n")
                if carton_size_c=="meduim":
                    total_cost_7=int(carton_number3)*int(medium_carton_50naira_price)+total_cost3
                    print("The total amount to be paid for the meduim cartons size of the 50naira coaster biscult is:",total_cost_7)
                elif carton_size_c=="large":
                    total_cost_8=int(carton_number3)*int(large_carton_50naira_price)+total_cost3
                    print("The total amount to be paid for the large cartons size and meduim carton size of the 50naira coaster biscult is:",total_cost_8)
                elif carton_size_c=="small":
                    total_cost_9=int(carton_number3)*int(small_carton_50naira_price)+total_cost3
                    print("The total amount to be paid for the small carton size and meduim carton size of the 50naira coaster biscult you ordered is:",total_cost_9)
            if number_of_carton3=="no":
                print("Dear",name,"\nSince you are not ordering more carton of coaster biscuit,the total cost for the meduim carton size of 50naira coaster biscult you ordered still remain the same.\nThanks for patronizing Emmanuella coaster biscuit depot:)\nHave a nice day....Hope to see you next time")
    elif coaster_type==coaster_type2 and carton_size=="small":
        total_cost4=int(carton_quantity)*int(small_carton_20naira_price/small_carton_20naira_quantity)
        print("The total amount to be paid for the small cartoon size of the 20naira coaster biscult is:",total_cost4)
        if carton_quantity==carton_quantity:
            number_of_carton4=input("Will you like to order more carton of the 20naira coaster biscult? (yes or no):\n")
            if number_of_carton4=="yes":
                carton_size_d=input("Enter the size of carton you would like to order(large,meduim,small):\n")
                carton_number4=input("Enter the number of carton you would like to order (1,2 or more):\n")
                if carton_size_d=="small":
                    total_cost_10=int(carton_number4)*int(small_carton_20naira_price)+total_cost4
                    print("The total amount to be paid for the small cartons size of the 20naira coaster biscult is:",total_cost_10)
                elif carton_size_d=="meduim":
                    total_cost_11=int(carton_number4)*int(medium_carton_50naira_price)+total_cost4
                    print("The total amount to be paid for the small carton size of the 50naira coaster biscult is:",total_cost_11)
                elif carton_size_d=="large":
                    total_cost_12=int(carton_number4)*int(medium_carton_50naira_price)+total_cost4
                    print("The total amount to be paid for the large carton size and small carton size of the 20naira coaster biscult is:",total_cost_12)
                if number_of_carton4=="no":
                    print("Dear",name,"\nSince you are not ordering more carton of coaster biscuit,the total cost for the small carton size of 20naira coaster biscult you ordered still remain the same.\nThanks for patronizing Emmanuella coaster biscuit depot:)\nHave a nice day....Hope to see you next time")
    elif coaster_type==coaster_type2 and carton_size=="large":
        total_cost5=int(carton_quantity)*int(large_carton_20naira_price/large_carton_20naira_quantity)
        print("The total amount to be paid for the large carton size of the 20naira coaster biscult is:",total_cost5)
        if carton_quantity==carton_quantity:
            number_of_carton5=input("Will you like to order more catoon of coaster biscult? (yes or no):\n")
            if number_of_carton5=="yes":
                carton_size_e=input("Enter the size of carton you would like to order(large,meduim,small):\n")
                carton_number5=input("Enter the number of carton you would like to order (1,2 or more):\n")
                if carton_size_e=="large":
                    total_cost_13=int(carton_number5)*int(large_carton_20naira_price)+total_cost5
                    print("The total amount to be paid for the large carton size of the 50naira coaster biscult you ordered is:",total_cost_13)
                elif carton_size_e=="small":
                    total_cost_14=int(carton_number5)*int(small_carton_20naira_price)+total_cost5
                    print("The total amount to be paid for the small cartons size and large carton size of the 20naira coaster biscult you ordered is:",total_cost_14)
                elif carton_size_e=="meduim":
                    total_cost_15=int(carton_number5)*int(medium_carton_50naira_price)+total_cost5
                    print("The total amount to be paid for the meduim carton size and large carton size of the 50naira coaster biscult you ordered is:",total_cost_15)
                if number_of_carton5=="no":
                    print("Dear",name,"\nSince you are not ordering more carton of coaster biscuit,the total cost for the large carton size of 20naira coaster biscult you ordered still remain the same.\n Thanks for patronizing Emmanuella coaster biscuit depot:)\nHave a nice day....Hope to see you next time")
    elif coaster_type==coaster_type2 and carton_size=="meduim": 
        total_cost6=int(carton_quantity)*int(medium_carton_20naira_price/medium_carton_20naira_quantity)
        print("The total amount to be paid for the meduim carton size of the 50naira coaster biscult is:",total_cost6)
        if carton_quantity==carton_quantity:
            number_of_carton6=input("Will you like to order more carton of coaster biscult? (yes or no):\n")
            if number_of_carton6=="yes":
                carton_size_f=input("Enter the size of carton you would like to order (large,meduim,small):\n")
                carton_number6=input("Enter the number of carton you would like to order (1,2 or more):\n")
                if carton_size_f=="large":
                    total_cost_16=int(carton_number6)*int(large_carton_20naira_price)+total_cost6
                    print("The total amount to be paid for the large carton size and meduim carton size of the coaster biscuit you ordered is:",total_cost_16)
                elif carton_size_f=="small":
                    total_cost_17=int(carton_number6)*int(small_carton_20naira_price)+total_cost6
                    print("The total amount to be paid for the small cartons size and meduim carton size of the 20naira coaster biscuit you ordered is:",total_cost_17)
                elif carton_size_f=="meduim":
                    total_cost_18=int(carton_number6)*int(medium_carton_50naira_price)+total_cost6
                    print("The total amount to be paid for the meduim carton size of the 50naira coaster biscuit you ordered is:",total_cost_18)
                if number_of_carton6=="no":
                    print("Dear",name,"\nSince you are not ordering more carton of coaster biscuit,the total cost for the meduim carton size of 20naira coaster biscuit you ordered still remain the same.\nThanks for patronizing Emmanuella coaster biscuit depot:)\nHave a nice day....Hope to see you next time")
    else:
        print("Dear",name,"pls input a valid coaster type,carton quantity and carton size")
calculate_total_amount(coaster_type=int(input("Enter the biscuit type (50,20)")),carton_size=input("Enter the biscuit size (small,meduim,large)\n"),carton_quantity=input("Enter the quantity of the biscult:\n"))
