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