#3 3 1 4 4 2 5 3 1 7 2 6 5 1

def dot_product(list_user_input):
    print("inside dot product")
    first_vector_length = list_user_input[0]
    second_vector_length = list_user_input[1]
    print("length of first vector is ",first_vector_length)

    if first_vector_length != second_vector_length:
        print("Incorrect input of vector lengths")
        return

    result = 0

    first_vector = list_user_input[2:2+(first_vector_length*2)]
    second_vector = list_user_input[2+(first_vector_length * 2):]

    if len(first_vector) != len(second_vector):
        print("Incorrect input of vectors")
        return

    print("elements of first vector",first_vector)
    print("elements of second vector",second_vector)
    # for x in range(len(first_vector)):
    #     for y in range(len(second_vector)):
    x=0
    y=0

    while x < len(first_vector) and y < len(second_vector):
        print("x,y are", x,y)
        if first_vector[x] == second_vector[y]:
            result += first_vector[x+1]*second_vector[y+1]
            x += 2
            y += 2
            print("values after incrementing by 2, x, y",x,y)
        elif first_vector[x] < second_vector[y]:
            x += 2
        else:
            y += 2
    print(result)






try:
    user_input = input('Enter your input: ')
    print(user_input)
except ValueError:
    print("Error in input")


list_user_input = list(user_input.replace(" ",""))

list_user_input_integer = [int(i) for i in list_user_input]
#find dot product
dot_product(list_user_input_integer)