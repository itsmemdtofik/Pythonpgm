def productArr(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum

n = int(input("Enter the size : "))
arr = []
print("Enter the elements : ")
for i in range(0, n):
    element = int(input())
    arr.append(element)
sum = productArr(arr)   
print("Sum of arra is : ", sum)