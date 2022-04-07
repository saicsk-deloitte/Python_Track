import sys


#class FormulaError:
    #pass
#def Calculate(user_input):
   # input_list = user_input.split()
    #if len(input_list) != 3:
        #raise FormulaError('Input must consist three elements')
while (True):
    user_inp = input("enter the String: ")
    if (user_inp == "quit"):
        print(" Thank you!")
        sys.exit()
    ls1 = list(user_inp.split(" "))
    try:
        num1 = float(ls1[0])
        num2 = float(ls1[2])
        if (ls1[1] == "+"):
            print(num2 + num1)
        elif (ls1[1] == "-"):
            print(num1 - num2)
        else:
            raise Exception()

    finally:
        print("You can continue , until you enter quit")