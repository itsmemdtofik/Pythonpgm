def arr(ProductArr):
	j = len(ProductArr) - 1
	i = 0
	while i < j:
		temp = ProductArr[i]
		ProductArr[i] = ProductArr[j]
		ProductArr[j] = temp
		i = i + 1
		j = j - 1
	return ProductArr

arr1 = [1, 2, 3, 4, 5]
print(arr(arr1))

def reverseString(string):
	if len(string) == 0:
		return string
	else:
		return reverseString(string[1:]) + string[0]

string = str(input("Enter the string : "))
print(reverseString(string))