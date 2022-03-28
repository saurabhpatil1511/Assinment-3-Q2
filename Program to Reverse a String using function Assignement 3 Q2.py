# Program to Reverse a String
def reverse_string(str):
    str1= ""
    for i in str:
        str1 = i + str1
    return str1
str = "1234abcd"
print(reverse_string(str))