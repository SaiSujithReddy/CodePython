
def find_palindrome(string):

    length_of_string = len(string) -1

    for x in range(0,int(length_of_string/2 +1)):
        if string[x] == string[length_of_string]:
            print("string of x is ",string[x])
            length_of_string -= 1
        else:
            return False
    return True

string = "Hiih"
string = "HiiH"
print(find_palindrome(string))