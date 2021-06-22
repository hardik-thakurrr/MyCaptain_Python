# Write a Python program to accept a filename from the user and print the extension of that.
name = input("Enter the name of the File -> ")
extension = name.split(".")
final_extension = extension[-1]
if final_extension == "py":
    print("Extension of the file is : 'python'")
else:
    print("Extension of the file is : " + final_extension)
