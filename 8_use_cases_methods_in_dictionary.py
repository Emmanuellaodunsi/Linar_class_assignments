#Using 8 use cases methods in dictionary to solve some real life scenarios problems 
"""Using clear()method .....
having a dictionary of a customer information 
and want to delete all the data"""
Customer_info={"name":"Emmanuella odunsi",
               "address":"29 lekan adebisi street agric road",
               "phone_number":"12345679",
               "email_address": "emmanuellaodunsi67@gmail.com"}

Customer_info.clear()
print("Cleared user info",Customer_info)
"""Using copy() method
having a dictionary of employee records and you want to make a copy 
of it so that you can make changes ti the copy without affecting the original"""
Employee_records={"Katty Blacky":
                {"Employee_id":12345,
                 "Job_title":"software engineer",
                 "Salary":100000000000},
                 "Jane Ella":
                 {"Employee_id":67890,
                  "Job_title":"Accountant",
                  "Salary":128888876}}

Employee_records_copy=Employee_records.copy()
Employee_records_copy["Katty Blacky"]["Salary"]=12000000000000
print("The records of the employee are:\n",Employee_records)
print("The updated employee record is:\n",Employee_records_copy)


"""Using fromkeys() method....
creating a new dictionary with a specific key and values"""
keys=["name","address","phone_number","email address"]
values=["Ella","123 main street","1234567890","emmanuellaodunsi67@gmail.com"]
customer_info=dict.fromkeys(keys,values)
print("The customer info are:\n",customer_info)

"""Using get() methods
having a dictionary of product price
and you want to get the price of a specific product"""

product_prices={
    "apple":10000,
    "banana":1200,
    "orange":4300}

apple_price=product_prices.get("apple")
print("The price apple is:",apple_price)


"""using item() method
having a dictionary of customer information 
and you want to iterate over the key value pairs """

customer_info2={
    "name":"john smith",
    "adress":"123 main street",
    "phone_number":"1234567890",
    "email_adress":"johnsmith@gmail.com"}
for key,value in customer_info2.items():
    print(key,value)

"""using key() method
having a dictionary of product prices 
and you want to get a list of all the products"""

product_prices2={
    "apple":2344,
    "banana":188,
    "orange":32145}
products=list(product_prices2.keys())
print(products)

"""using pop() method
having a dictionary of customer information 
and you want to remove a specific customer """

customer_info3={
    "john smith":{ 
    "adress":"123 main street",
    "phone_number":"1234567890",
    "email_adress":"johnsmith@gmail.com"},
    "sara smith":{
    "adress":"178 main street",
    "phone_number":"1234867890",
    "email_adress":"sara smith@gmail.com"}
}
customer_info3.pop("john smith")
print(customer_info3)

"""using update() method
having two dictionary of values
and you want to merge them together"""

dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5,"f":6}
dict1.update(dict2)
print(dict1)