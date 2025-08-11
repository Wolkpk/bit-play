def numberOfBites(n):
    ones = 0
    zeroes = 0
    while (n):
        if {n & 1 == 1}:
            ones += 1 
        else:
            zeroes += 1
        n >>= 1
    print("number of ones =", ones, "\nNumbers of zeroes =" ,zeroes)

number = int(input("enter your number"))
numberOfBites(number)