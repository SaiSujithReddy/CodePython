
# https://stackoverflow.com/questions/4806911/string-comparison-technique-used-by-python


def string_comparison(str1,str2):
    if str1 == str2:
        print("String1 same as String2")
    elif str1 > str2:
        print("String1 is greater than String2")
    else :
        print("String2 is greater than String1")


string1 = "hello"
string2 = "ha"
string_comparison(string1,string2)