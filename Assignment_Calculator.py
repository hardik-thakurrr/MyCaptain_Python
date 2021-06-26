# Arithmetic calculator
choice = 1
while choice != 7:
    print("********* Menu **********")
    print("*  1. Addition          *")
    print("*  2. Subtraction       *")
    print("*  3. Division          *")
    print("*  4. Multiplication    *")
    print("*  5. Modulo            *")
    print("*  6. Exponential       *")
    print("*  7. Exit              *")
    choice = int(input("Enter your Choice -> "))
    if choice == 1:
        print("Addition !!")
        n1 = float(input("Enter Number 1 -> "))
        n2 = float(input("Enter Number 2 -> "))
        Result = n1 + n2
    elif choice == 2:
        print("Subtraction !!")
        n1 = float(input("Enter Number 1 -> "))
        n2 = float(input("Enter Number 2 -> "))
        Result = n1 - n2
    elif choice == 3:
        print("Division !!")
        n1 = float(input("Enter Number 1 -> "))
        n2 = float(input("Enter Number 2 -> "))
        Result = n1 / n2
    elif choice == 4:
        print("Multiplication !!")
        n1 = float(input("Enter Number 1 -> "))
        n2 = float(input("Enter Number 2 -> "))
        Result = n1 * n2
    elif choice == 5:
        print("Modulo !!")
        n1 = float(input("Enter Number 1 -> "))
        n2 = float(input("Enter Number 2 -> "))
        Result = n1 % n2
    elif choice == 6:
        print("Exponential !!")
        n1 = float(input("Enter Base -> "))
        n2 = float(input("Enter Exponent -> "))
        Result = n1**n2
    elif choice == 7:
        print("Thank You !! ")
        break
    else:
        print("Invalid Choice ")
    print("Final Result is -> ", Result, "\n")
