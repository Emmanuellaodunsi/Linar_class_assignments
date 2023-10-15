#Buildingg a python structure ....which is known to have 4 rooms and a toilet
#start
'''problem statement:
being the civil engineer of a civil construction company,
you are given a contract to construct a python structure,
which is known for having 4 rooms and a toilet,
with the customer specifying the dimensions of the rooms,
find the total number of blocks and total cost of the building with a constant height of 12ft using
    either 600naira block with 
    dimensions 6inch by 9inch by 15inch or 1000naira blocks with dimensions of 10inch by 12inch by 20inch.'''


Name=input("pls...Enter your name:")
print("Hello!",Name, "Welcome to Emmanuella Civil Contruction Company")
print("Building a python structure....which is known to have 4 room and a toilet,using the block cost of 1000 naira")

#constant for Block A
Height= 12
Block_A_price=1000
#Converting the blocks measurment from inches to feets
Block_A_length=(20/12) 
Block_A_height=(12/12)
Block_A_width=(10/12)

#constants for Block B
height= 12
Block_B_price=600
#Converting the blocks measurment from inches to feets
Block_B_length=(15/12) 
Block_B_height=(9/12)
Block_B_width=(6/12)




#The first rooms dimensions provided by the customers
Room1_lenght=float(input("pls...enter the lenght of the first room in feets"))
Room1_width=float(input("Enter the width of the first room in feets"))
Room1_height=12

 

#The second rooms dimensions provided by the customers
Room2_lenght=float(input("pls...enter the lenght of the second room in feets"))
Room2_width=float(input("Enter the width of the second room in feets"))
Room2_height=12

#The third rooms dimensions provided by the customers
Room3_lenght=float(input("pls...enter the lenght of the third room in feets"))
Room3_width=float(input("Enter the width of the third room in feets"))
Room3_height=12

#The fourth rooms dimensions provided by the customers
Room4_lenght=float(input("pls...enter the lenght of the fourth room in feets"))
Room4_width=float(input("Enter the width of the fourth room in feets"))
Room4_height=12

#The toilet dimensions provided by the customers
Toilet_lenght=float(input("pls...enter the lenght of the toilet in feets"))
Toilet_width=float(input("Enter the width of the toilet in feets"))
Toilet_height=12

#calculating the number of blocks required for building the first room lenght and height

Room1wall_1_lenght=Room1_lenght/Block_A_length
Room1Round1=round(Room1wall_1_lenght) +1
Room1Wall1_height=Room1_height/Block_A_height
Room1_wall1=Room1Round1*Room1Wall1_height
Room1_wall1_opposite=Room1_wall1*2

#calculating the number of blocks required for building the first room width and height

Room1wall_2_width=Room1_lenght/Block_A_length
Room1Round2=round(Room1wall_2_width) +1
Room1Wall2_height=Room1_height/Block_A_height
Room1_wall2=Room1Round2*Room1Wall2_height
Room1_wall2_opposite=Room1_wall2*2

Room1_num_blocks=Room1_wall1_opposite+Room1_wall2_opposite



#calculating the number of blocks required for building the second room lenght and height

Room2wall_1_lenght=Room2_lenght/Block_A_length
Room2Round1=round(Room2wall_1_lenght) +1
Room2Wall1_height=Room2_height/Block_A_height
Room2_wall1=Room2Round1*Room2Wall1_height
Room2_wall1_opposite=Room2_wall1*2


#calculating the number of blocks required for building the second room width and height

Room2wall_2_lenght=Room2_width/Block_A_length
Room2Round2=round(Room2wall_2_lenght) +1
Room2Wall2_height=Room2_width/Block_A_height
Room2_wall2=Room2Round2*Room2Wall2_height
Room2_wall2_opposite=Room2_wall2*2

Room2_num_blocks=Room2_wall1_opposite+Room2_wall2_opposite


#calculating the number of blocks required for building the third room lenght and height

Room3wall_1_lenght=Room3_lenght/Block_A_length
Room3Round1=round(Room3wall_1_lenght) +1
Room3Wall1_height=Room3_height/Block_A_height
Room3_wall1=Room3Round1*Room3Wall1_height
Room3_wall1_opposite=Room3_wall1*2



#calculating the number of blocks required for building the third room width and height

Room3wall_2_lenght=Room3_width/Block_A_length
Room3Round2=round(Room3wall_2_lenght) +1
Room3Wall2_height=Room3_width/Block_A_height
Room3_wall2=Room3Round2*Room3Wall2_height
Room3_wall2_opposite=Room3_wall2*2

Room3_num_blocks=Room3_wall1_opposite+Room3_wall2_opposite




#calculating the number of blocks required for building the fourth room lenght and height

Room4wall_1_lenght=Room4_lenght/Block_A_length
Room4Round1=round(Room4wall_1_lenght) +1
Room4Wall1_height=Room4_height/Block_A_height
Room4_wall1=Room4Round1*Room4Wall1_height
Room4_wall1_opposite=Room4_wall1*2



#calculating the number of blocks required for building the fourth room width and height

Room4wall_2_lenght=Room4_width/Block_A_length
Room4Round2=round(Room4wall_2_lenght) +1
Room4Wall2_height=Room4_width/Block_A_height
Room4_wall2=Room4Round2*Room4Wall2_height
Room4_wall2_opposite=Room4_wall2*2

Room4_num_blocks=Room4_wall1_opposite+Room4_wall2_opposite



#calculating the number of blocks required for building the toilet lenght and height

Toiletwall_1_lenght=Toilet_lenght/Block_A_length
ToiletRound1=round(Toiletwall_1_lenght) +1
ToiletWall1_height=Toilet_height/Block_A_height
Toilet_wall1=ToiletRound1*ToiletWall1_height
Toilet_wall1_opposite=Toilet_wall1*2

#calculating the number of blocks required for building the toilet width and height

Toiletwall_2_lenght=Toilet_lenght/Block_A_length
ToiletRound2=round(Toiletwall_2_lenght) +1
ToiletWall2_height=Toilet_height/Block_A_height
Toilet_wall2=ToiletRound2*ToiletWall2_height
Toilet_wall2_opposite=Toilet_wall2*2

Toilet_num_blocks=Toilet_wall1_opposite+Toilet_wall2_opposite



#calculating the total number of blocks needed to build the python struction (4 rooms and a toilet)
Total_num_blocks=Room1_num_blocks+Room2_num_blocks+Room3_num_blocks+Room4_num_blocks+Toilet_num_blocks

#calculate the cost of blocks for the python structure
Python_stucture_blocks_cost=Total_num_blocks*Block_A_price


print("Hello",Name)
print("The total number of blocks needed to build the python structure(4 room and a toilet) using block price of 1000 naira is:",Total_num_blocks)
print("The cost of building the python structure is:", Python_stucture_blocks_cost)




print("Building the python structure....using the block cost of 600 naira")



#calculating the number of blocks required for building the first room lenght and height
room1wall_1_lenght=Room1_lenght/Block_B_length
room1Round1=round(room1wall_1_lenght) +1
room1Wall1_height=Room1_height/Block_B_height
room1_wall1=room1Round1*room1Wall1_height
room1_wall1_opposite=room1_wall1*2

#calculating the number of blocks required for building the first room width and height

room1wall_2_width=Room1_lenght/Block_B_length
room1Round2=round(room1wall_2_width) +1
room1Wall2_height=Room1_height/Block_B_height
room1_wall2=room1Round2*room1Wall2_height
room1_wall2_opposite=room1_wall2*2

room1_num_blocks=room1_wall1_opposite+room1_wall2_opposite



#calcualting the number of blocks required for building the second room lenght and height
room2wall_1_lenght=Room2_lenght/Block_B_length
room2Round1=round(room2wall_1_lenght)+1
room2wall1_height=Room2_height/Block_B_height
room2_wall1=room2Round1*room2wall1_height
room2_wall1_opposite=room2_wall1*2

#calculating the number of block required for building the second room width and height 
room2wall_2_lenght=Room2_width/Block_B_length
room2Round2=round(room2wall_2_lenght)+1
room2Wall2_height=Room2_height/Block_B_length
room2_wall2=room2Round2*room2Wall2_height
room2_wall2_opposite=room2_wall2*2

room2_num_blocks=room2_wall1_opposite+room2_wall2_opposite




#calculating the number of blocks required for building the third room lenght and height

room3wall_1_lenght=Room3_lenght/Block_B_length
room3Round1=round(room3wall_1_lenght) +1
room3Wall1_height=Room3_height/Block_B_height
room3_wall1=room3Round1*room3Wall1_height
room3_wall1_opposite=room3_wall1*2



#calculating the number of blocks required for building the third room width and height

room3wall_2_lenght=Room3_width/Block_B_length
room3Round2=round(room3wall_2_lenght) +1
room3Wall2_height=Room3_width/Block_B_height
room3_wall2=room3Round2*room3Wall2_height
room3_wall2_opposite=room3_wall2*2

room3_num_blocks=room3_wall1_opposite+room3_wall2_opposite




#calculating the number of blocks required for building the fourth room lenght and height

room4wall_1_lenght=Room4_lenght/Block_B_length
room4Round1=round(room4wall_1_lenght) +1
room4Wall1_height=Room4_height/Block_B_height
room4_wall1=room4Round1*room4Wall1_height
room4_wall1_opposite=room4_wall1*2



#calculating the number of blocks required for building the fourth room width and height

room4wall_2_lenght=Room4_width/Block_B_length
room4Round2=round(room4wall_2_lenght) +1
room4Wall2_height=Room4_width/Block_B_height
room4_wall2=room4Round2*room4Wall2_height
room4_wall2_opposite=room4_wall2*2

room4_num_blocks=room4_wall1_opposite+room4_wall2_opposite



#calculating the number of blocks required for building the toilet lenght and height

toiletwall_1_lenght=Toilet_lenght/Block_B_length
toiletRound1=round(toiletwall_1_lenght) +1
toiletWall1_height=Toilet_height/Block_B_height
toilet_wall1=toiletRound1*toiletWall1_height
toilet_wall1_opposite=toilet_wall1*2

#calculating the number of blocks required for building the toilet width and height

toiletwall_2_lenght=Toilet_lenght/Block_B_length
toiletRound2=round(toiletwall_2_lenght) +1
toiletWall2_height=Toilet_height/Block_B_height
toilet_wall2=toiletRound2*toiletWall2_height
toilet_wall2_opposite=toilet_wall2*2

toilet_num_blocks=toilet_wall1_opposite+toilet_wall2_opposite



#calculating the total number of blocks needed to build the python struction (4 rooms and a toilet)
total_num_blocks=room1_num_blocks+room2_num_blocks+room3_num_blocks+room4_num_blocks+toilet_num_blocks

#calculate the cost of blocks for the python structure
python_stucture_blocks_cost=total_num_blocks*Block_B_price


print("Hello",Name,)
print("The total number of blocks needed to build the python structure(4 room and a toilet) using block price of 600 naira is:",total_num_blocks)
print("The cost of building the python structure is:", python_stucture_blocks_cost)
print("Thank you for contacting Emmanuella Civil Contruction Company :).....")
#end