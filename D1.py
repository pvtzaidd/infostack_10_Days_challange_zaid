
no = int(input("Enter the number of elements (1 to 1000): "))
array = []

print("Enter the elements one by one:")
for i in range(no):
    number = int(input())
    array.append(number)
rev_array = []
for i in range(len(array) - 1, -1, -1):
    rev_array.append(array[i])

double_rev = []
for i in range(len(array) - 1, -1, -1):
    double_rev.append(array[i] * 2)
print("Original array:", array)
print("Reversed array:", rev_array)
print("Doubled and reversed array:", double_rev)