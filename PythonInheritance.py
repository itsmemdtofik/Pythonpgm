'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''


class Person:
	def __init__(self, fname, lname, age):
		self.fname = fname
		self.lname = lname
		self.age = age

	def printDetails(self):
		print(self.fname, self.lname)

p1 = Person("Mohammad", 'Tofik', 24)
p1.printDetails()



#Create a child class 
#Create a class named student which will inherit the properties and method from the Person class.

class Student(Person):
	pass

p1 = Student('Rahul', 'Chaudhary', 24)
p1.printDetails()

#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

#Add the __init__() to student class.

#class Student(Person):
#	def __init__(self, fname, lname):

'''
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''
class Person:
	def __init__(self, fname, lname):
		self.firstName = fname
		self.lastName = lname

	def printDetails(self):
		print(self.firstName, self.lastName)

class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)


p1 = Student('Ria', 'Chaudhary')
p1.printDetails()

#Use the super() function
#Python also has a super() function that will make the child class inherit all the mehtid and properties from its parent.


class Person:
	def __init__(self, fname, lname):
	    self.fname = fname
	    self.lname = lname 

	def printAllName(self):
		print(self.fname, self.lname)

class Student(Person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)

p1 = Student('Salman', 'Khan')
p1.printAllName()

#Add Properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)


#Add method

class Person:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname

	def printDetails(self):
		print(self.fname, self.lname)

class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcome(self):
		print('welcome', self.fname, self.lname, 'to the class of', self.graduationyear)


p1 = Student('Rohan','Kumar', 2023)
p1.printDetails()
p1.welcome()