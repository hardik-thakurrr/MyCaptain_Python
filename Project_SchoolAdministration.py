# School Administration Program
import csv


def write_into_csv(student_list):
    with open('student_administration.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email-ID"])
        writer.writerow(student_list)


if __name__ == '__main__':
    condition = True
    num = 1
    while condition:
        student_Info = input("\nEnter Student #{} Information (Name,Age,Contact Number,Email-ID) -> ".format(num))
        print("Student #{} Information is -> {}".format(num, student_Info))

        student_Info_List = student_Info.split(",")
        print("Spilt up Student #{} Information is -> {}".format(num, str(student_Info_List)))
        print("\tEntered Information of Student #{} is:\n\tName -> {}\n\tAge -> {}\n\tContact Number " "-> {}"
              "\n\tEmail-ID -> {}" .format(num, student_Info_List[0], student_Info_List[1], student_Info_List[2],
                                           student_Info_List[3]))

        choice = input("\nEnter 'Y' to Confirm Details or 'N' to Re-enter -> ")
        if choice == 'Y' or choice == 'y':
            write_into_csv(student_Info_List)

            condition_Checker = input("Enter 'Y' to Continue to add Details of Student or 'N' to Discontinue -> ")
            if condition_Checker == "Y" or condition_Checker == "y":
                condition = True
                num = num + 1
            if condition_Checker == "N" or condition_Checker == "n":
                condition = False

        elif choice == 'N' or choice == 'n':
            print("Re-Enter Student Details !! ")
