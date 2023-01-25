def reverseArray(arr):
    j = len(arr) - 1
    i = 0
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i = i + 1
        j = j - 1
    return arr

n = int(input("Enter the size : "))
print("Enter the elements : ")
arr = []

for i in range(0, n):
    element = int(input())
    arr.append(element)
    

print(reverseArray(arr))


str1 = str(input("Enter the string : "))
str1 = str1.casefold()
print(str1)
print("The consonant in thr string : ")
for i in str1:
    if i not in "aeiou":
        print(i, end=", ")
print("\nmo")
print("The wovels are in the string : ")
for i in str1:
    if i in "aeiou":
        print(i, end=", ")
        
print("\n")