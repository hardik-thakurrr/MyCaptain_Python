# Write a Python Program for Fibonacci numbers.
elements = int(input("Enter the Number of elements  -> "))
a = 0
b = 1
print("The Fibonacci Series of ", elements, " Elements is -> ")
for i in range(1, elements+1, 1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

