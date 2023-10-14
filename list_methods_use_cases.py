#Reversing the order elements in list using reverse()method
Numbers=[10,9,8,7,6,5,4,3,2,1]
Numbers.reverse()
print("The reversed lists of numbers are:\n",Numbers)

#sorting a list of values in a ascending order
value=[2,9,3,7,5,8,4]
value.sort()
print("The sorted list of values are:\n",value)

#Counting the number of time a item occures in a list
Fruits=['apple','mango','orange','pawpaw','mango','apple','mango']
count=Fruits.count('mango')
print("The number of mango in the list is:",count)


#Counting the number of words in a sentence using the split()method and len() function
sentence=['python', 'is', 'awesome!.']
num_words=sentence.split()
word_count=len(num_words)
print("The number of words in the sentence is:",word_count)


#Clearing all element in a list...using clear()method
values=[1,2,3,4,5,6,7,4,6]
clear_value=values.clear()
print(clear_value)

#inserting an element at a specific index in a list....using insert()method
num1=[1,2,3,4,5,6,7]
num2=num1.insert(8,9)
print(num2)


#Sorting a list of name in class alphabetically....using sort()method
names=['Gbenro','Emmanuella','Samuel']
sorted_name=names.sort()
print(names)

#Removing a specific element in a list
num=[1,2,3,4,5,6,7,8,9]
remove_num=num.remove(4,6)
print(remove_num)
