'''
Python is an object oriented programming lanugage.
Almost everything in python is object.
A class is like an object constructor or blueprint for creating a class.
To create a class we use class keyword.
'''


class demo1:
	x = 'mohammad'

print(demo1)

#We can use the class name demo1 to create an object.
p1 = demo1()
print(p1.x)


#The __init__() Function
#The example above are classes and object in their simplest form, and are not useful in real life application.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a fucntion called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign the values to the object properties, or other operations that are necessory to do when the object is being created.


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("mohammad", 24)
print(p1.name)
print(p1.age)

#Note : The __init__() function is called autoatically every time the class being used to create a new object.

#The __str__() Function controls what should be returned when the class object is represented as string.
#If the __str__() function is not set, the string representation of the object is returned.
#The string representation of an object whitought the __str__() function.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("JMohammad", 24)
print(p1)


#The string representation of an object with the __str__() function.

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return f"{self.name} {self.age}"

p1 = Person("mohammad", 24)
print(p1)


#Object Method : Objects can also contains method.Mehtods in objects are function that belong to the object.

#Let us create a method in the person class.

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def Name(self):
		print("Hello my name is : " + self.name)

p1 = Person("Mohammad", 24)
p1.Name()


#Note : The self parameter is a reference to the current instance of the class and is
#used to access variable that belong to the class

#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.
#use words mySillyObject and abc instead of self.

class Person:
	def __init__(mySillyObject, name, age):
		mySillyObject.name = name
		mySillyObject.age = age

	def demo1(mySillyObject):
		print("Hello I am : " + mySillyObject.name)

	def demo2(abc):
		print("I am an : " , abc.age)

p1 = Person("Mohammad", 24)
p1.demo1()
p1.demo2()

#Modify an Object Properties
#You can modify properties on object like this.

class Person:
	def __init__(mySillyObject, name, age):
		mySillyObject.name = name
		mySillyObject.age = age

	def demo1(mySillyObject):
		print("Hello I am : " + mySillyObject.name)

	def demo2(abc):
		print("I am an : " , abc.age)

p1 = Person("Mohammad", 24)
p1.demo1()
p1.demo2()

p1.age = 40
print(p1.age)

#Delete an object properties : You can delete properties on objects by using the del keyword.

del p1.age

#You can delete the object suing del keyword
del p1



#The pass Statement : class definition can not be empty, but if you for some reason have class definiton with no content, put in the pass statement to avoid getting an error.

class Student:
	pass

