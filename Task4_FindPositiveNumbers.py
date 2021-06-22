# Write a Python program to print all positive numbers in a range.
elements1 = int(input("Enter the Number of elements in List 1 -> "))
list1 = []
list2 = []
print("Enter the Values of List 1:")
for i in range(0, elements1, 1):
    values = int(input())
    list1.append(values)

elements2 = int(input("\nEnter the Number of elements in List 2 -> "))
print("Enter the Values of List 2:")
for i in range(0, elements2, 1):
    values = int(input())
    list2.append(values)

print("\nList1 = ", list1)
print("List2 = ", list2)
print("\nPositive Values in List 1: ", end='')
for i in range(0, elements1, 1):
    if list1[i] >= 0:
        print(list1[i], end=' ')

print("\nPositive Values in List 2: ", end='')
for i in range(0, elements2, 1):
    if list2[i] >= 0:
        print(list2[i], end=' ')

