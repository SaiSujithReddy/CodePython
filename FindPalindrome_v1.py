
def find_palindrome(string):
    print("String is ", string)
    if string == "":
        return True
    if len(string) == 1:
        return True
    else :
        if string[0] == string[len(string)-1]:
            return find_palindrome(string[1:len(string)-1])
        return False

print(find_palindrome("ABCDEFDCBA"))

