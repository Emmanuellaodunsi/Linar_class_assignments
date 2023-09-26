#using the "or" logical operator
#checking if a student is eligible for scholarship based on their grade score
Physic_grade=90
English_grade=95
Physic_score=int(input("enter your physic score:"))
English_score=int(input("enter your english score:"))
if Physic_score>=Physic_grade or English_score>=English_grade:
    print("you are eligible for the scholarship")


