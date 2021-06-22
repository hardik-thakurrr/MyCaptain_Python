# Functions of List
fruits = ["Banana", "apple", "Mango", "WaterMelon", "Kiwi", "apple"]
choice = 1
while choice != 14:
    print(" ")
    print("*********** Menu ************")
    print("*  1. Print List            *")
    print("*  2. Update List Element   *")
    print("*  3. Remove List Element   *")
    print("*  4. Length of List        *")
    print("*  5. Maximum in List       *")
    print("*  6. Minimum in List       *")
    print("*  7. Append in List        *")
    print("*  8. Count in List         *")
    print("*  9. Pop from the List     *")
    print("*  10. Sort The List        *")
    print("*  11. Positional Insert    *")
    print("*  12. Extend the List      *")
    print("*  13. Copy a List          *")
    print("*  14. Exit                 *")
    print("*****************************")
    choice = int(input("Enter your Choice -> "))
    if choice == 1:
        print("Fruits List -> ", fruits)
    elif choice == 2:
        ind = int(input("Enter Index Number to be Updated -> "))
        value = input("Enter New Value -> ")
        fruits[ind] = value
    elif choice == 3:
        ind = int(input("Enter Index Number to be Removed -> "))
        del fruits[ind]
    elif choice == 4:
        print("Length of the list is -> ", len(fruits))
    elif choice == 5:
        print("Maximum Element in the list is -> ", max(fruits))
    elif choice == 6:
        print("Minimum Element in the list is -> ", min(fruits))
    elif choice == 7:
        value = input("Enter Value to be Appended -> ")
        fruits.append(value)
    elif choice == 8:
        value = input("Enter Value to Count Occurrence -> ")
        print("The word '", value, "' occurs ", fruits.count(value), "in the List")
    elif choice == 9:
        ind = int(input("Enter Index Number to be Popped -> "))
        fruits.pop(ind)
    elif choice == 10:
        print("Sorted List is -> ", fruits.sort())
    elif choice == 11:
        ind = int(input("Enter Index Number to Insert new Value -> "))
        value = input("Enter New Value -> ")
        fruits.insert(ind, value)
    elif choice == 12:
        vegetables = ["Tomato", "Pumpkin", "Onion"]
        print(fruits.extend(vegetables))
    elif choice == 13:
        x = fruits.copy()
        print("Value of x -> ", x)
    elif choice == 14:
        print("Thank You !! ")
        break
    else:
        print("Invalid Choice ")
