list1 = ['Mohammad Tofik',"Lokesh",'Rahul']
list2 = list1
print(list2)
print(list2[-1])
print(len(list2))
print(len(list1))


string1 = "Mohammad"
string2 = "Tofik"
print(string2 + string1)
print(string2 +""+string1)
print(string1+''+string2)

variable1 = "Mohammad Tofik"
number = 12.3
boolean = True
list1 = ["mohammad","tofik","khan"]
print(variable1, number, boolean, list1)

#list, tuple, dictionary, set
list1 = ['mohammad','tofik',12.3, True]
tuple1 = ('mohammad','tofik',12.3, True)
dictionary = {'name':'mohammad', 'address':'Manipal', 'age':12.3, 'Male':True}
set1 = {'mohammad', 'tofik', 12.3, True}

print(type(list1), list1)
print(type(tuple1), tuple1)
print(type(dictionary), dictionary)
print(type(set1), set1)

print("\n---------------------------------------------------\n")
#You can declare in two different ways
#list, tuple, dictionary, set
list1 = list(['mohammad','tofik',12.3, True])
tuple1 = tuple(('mohammad','tofik',12.3, True))
dictionary = dict({'name':'mohammad', 'address':'Manipal', 'age':12.3, 'Male':True})
set1 = set({'mohammad', 'tofik', 12.3, True})
frozen = frozenset({"mohammad", "tofik",12.3, True})

print(type(list1), list1)
print(type(tuple1), tuple1)
print(type(dictionary), dictionary)
print(type(set1), set1)
print(type(frozen), frozen)

#Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

string = 'mohammad tofik khan'
print(string[2:5]) #ham
print(string[:])   #mohammad tofik khan
print(string[2:])  #hammad tofik khan
print(string[:2])
print(string[-2])  #a
print(string[-5:2]) #Nothing will be printed

#Modify String
#upper(), lower(), replace(), split(), strip()
string1 = ' Mohammad, tofik, khan'
print('The uppercase string is :', string1.upper())
print('The lowercase string is :', string1.lower())
print('After spliting the string is : ', string1.split(","))
print('After replacing the character o by u : ', string1.replace('o','u'))
print('After removing the white space : ', string1.strip())
print("Capitalize string is : ", string1.capitalize())
print("Title string is : ", string1.title())
'''
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''

#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
'''age = 36
txt = "My name is John, I am " + age
print(txt)'''

#But we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

integerNumber = 12
floatNumber = 12.3
string = 'Mohamad tofik {} and my age is {}'
print(string.format(integerNumber, floatNumber))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#List
#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#A list can contain different data types

myList = ['Mohammad', 'Tofik','Khan', 12, 12.4, True, False]
print('The list is : ', myList)
print('Updating the list ...')
myList = ['Mohammad', 'Tofik','Khan', 12, 12.4, True, False, 'Basti', 'Uttar Pradesh','Mohammad']
print('After updating the list : ', myList)
print('The element at first index is : ', myList[0])
print('The element at the end is : ', myList[-1])
myList[1:4] = ['Lucknow','Mumbai','Bhopal']
print('After changing the list : ', myList)
print('Changing 2nd and third value by replacing one value')
myList[1:3] = ['India']
print("After replacing 2nd and 3rd : ", myList)


#We can use the list constructor to create the list
myList = list(('mohammad', 12, 13.3, 'mohammad', True, False))
print('List suing list constructor is : ', myList)

#method to modify list append('banana'), insert(1, 'banana'), remove('mohammad'), pop(1)
#Even we can extend or merge the list
#list1.extend(list2), del list2

list1 = ['mohammad', 12, 13.2, True, False]
list2 = ['India', 1123, 123.4, False, True]
list1.extend(list2)
print('After extending the list : ', list1)
#List through loop

for x in list1:
	print(x)

#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print('The list is :', thislist[i])

#Copy the list from two method
thislist = ["apple", "banana", "cherry"]
mylist = ['mango','pineapple','papaya']
mylist2 = thislist.copy()
print('After copying the thislist into mylist2 : ', mylist2)
mylist3 = list(mylist) * 2
print("After copying the mylist into mylist3 : ", mylist3)


del list1
list2.clear()
print('Deleted list1 : ', list2, ' Cleared list2 : ',list2)

'''
List Methods
Python has a set of built-in methods that you can use on lists.

Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
'''


#Dictionary
#Method get('name'), keys(), values()

dictionary = {
	'name':'mohammad tofik',
	'address':'Manipal',
	'college':'Manipal Institute Of Technology',
	'colors':['Yellow','Orange','Blue'],
	'Gender':['Male','Female'],
	'year':2020
}

print('The dictionary is : ', dictionary)

key = dictionary.keys()
value = dictionary.values()

print('The key is : ', key)
print('The values are : ', value)

#Update the dictionary
print('Before updating : ', dictionary)
dictionary['year'] = 2022
print('After updating the dictionary is : ', dictionary)

#Dictionary method
#clear(), pop(), popitem(), items(), update(), del et cetra.


#Write a program to convert list into tuple

list = [1, 2, 3, 4]
print(type(list), list)

tuple = tuple(list)
print(type(tuple), tuple)

#Write a program to conver dictionary into list
myDict = {
	'name':'mohammad tofik',
	'address':'Manipal',
	'college':'Manipal Institute Of Technology',
	'colors':['Yellow','Orange','Blue'],
	'Gender':['Male','Female'],
	'year':2020
}
print('Before converting into list : ', type(dict), dict)
myResultList = list(myDict.items())
print('After converting into list :', myResultList)