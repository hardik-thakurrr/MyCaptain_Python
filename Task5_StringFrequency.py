# Write Python code to create a function called most_frequent that takes a string
# and prints the letters in decreasing order of frequency. Use dictionaries.
import operator
def most_frequent(str_func):
    string_dict = {}
    for n in str_func:
        if n in string_dict:
            string_dict[n] += 1
        else:
            string_dict[n] = 1
    return string_dict

str_input = input("Enter a String -> ")
print(" Final Output:\n", sorted(most_frequent(str_input).items(), key=operator.itemgetter(1), reverse=True))
