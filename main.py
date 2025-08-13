def checkIfSame(number1, number2):
    if((number1 ^ number2)!= 0):
        print("number are not equal")

    else:
        print("number are equal")

number1 = int(input("enter first num to compare"))
number2 = int(input("enter seconde num to compare"))
checkIfSame(number1, number2)