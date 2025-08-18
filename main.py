def power2(number):
    if number <= 0:
        return False
    return (number &(number - 1)) == 0

n = int(input("enter a number"))
if power2(n):
    print("\nthe poweris the a power of 2")
else:
    print("\nis not power of two")
    