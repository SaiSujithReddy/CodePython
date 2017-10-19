import numpy

class Calculator:
    def __init__(self):
        self.list = []

    def get_mean(self):
        print(numpy.mean(self.list))

    def get_std(self):
        print(numpy.std(self.list))

    def get_median(self):
        print(numpy.median(self.list))

    def put(self,input_string):
        if (input_string>-2^31  and input_string<2^31):
            self.list.append(input_string)
        else:
            print("Please input value within range")


calculator = Calculator()
calculator.put(5)
calculator.put(10)
calculator.put(15)
calculator.put(16)
calculator.get_mean() # should return 10 (because (5+10+15)/3 = 10)
calculator.get_std() # should return 4.08248290463863
calculator.put(20)
calculator.get_mean() # should return 12.5 (because (5+10+15+20) / 4 = 12.5)
calculator.put(20778999999999391029740972074027412747120472014774217740274021740712)
calculator.get_median()

'''

for i in range(0,5):
    #sys.stdin.readline()
    input_string = raw_input("Enter :")
        #raw_input('Enter a num or mean or std: ')
    print("you entered", input_string)

    try:
        int(input_string)
        print("Inside int")
        list.append(int(input_string))

    except: #elif (isinstance(input_string,str)):
        if(input_string == 'mean'):
            print(list)
            print(calculate_mean(list))
        else:
            print(list)
            print(calculate_std(list))
'''