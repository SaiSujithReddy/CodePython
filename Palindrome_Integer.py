
def find_palindrome_integer(number):

    if number <0:
        print("No it is not a palindrome")
    elif str(number) == str(number)[::-1]:
        print("Yes it is a palindrome !")
    else:
        print("No it is not a palindrome")


'''

    # How to convert number to string
    c = []
    for digit in str(number):
        c.append(int(digit))
    print(c)

    # How to convert number to string
    lst = [int(i) for i in str(number)]
    print(lst)

    print(len(lst))


'''


number = 654876
find_palindrome_integer(number)