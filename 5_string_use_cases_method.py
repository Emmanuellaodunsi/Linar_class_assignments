"""5 use cases in string"""
#finding the index of a specific character in a string
"""using find()method"""
sentence="Python is awesome"
index=sentence.find("s")
print("The index of 's' is:",index)

#entering password for login
"""using isalnum()method"""
password=input("Enter your password...(containing alphabeth and numbers)")
if password.isalnum():
    print("valid and secured password")
else:
    print("weak password")

#Checking if a sentence ends with a specific word
"""using endswitch()method"""
word="Hello,World!"
if word.endswith("World!"):
    print("The given word ends with 'World!'.")
else:
    print("The given word does not end with'World!'.")


#Checking if the word contains only alphabetic characters
"""using isalpha()method"""
User_name=input("Emter your user name....using just alphabetic letters:\n")
if User_name.isalpha():
    print("The given username contains only alphabetic characters.")
else:
    print("The given username does not contain only alphabetic cahracters.")

#Checking if the call number conatains only numbers
"""Using isnumeric()method"""
phone_number=input("Enter your call number:\n")
if phone_number.isnumeric():
    print("Valid phone number.")
else:
    print("Pls enter a valid phone number!.")