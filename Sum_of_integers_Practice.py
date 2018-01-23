def check_result(operators,input):
    exec_string =  "%s" + str(input[0]) + "%s" + str(input[1]) + "%s" + str(input[2]) + "%s" + str(input[3])
    # result=False
    for a in operators:
        for b in operators:
            for c in operators:
                for d in operators:
                    test= exec_string %(a,b,c,d)
                    # print eval(test)
                    if eval(test)==24:
                        print(test)
                        return eval(test)
    return False

input=[12,12,5,5]

operators=["+","-"]
print(check_result(operators,input))