def script(a,b):

    a = a^b
    b = a^b
    a = a^b
    print("after swaping: a =",a,"and b =",b)


def swap2(a,b):
    a = (a&b)+(a|b)
    b = a+(~b)+1
    a = a+(~b)+1
    print("after swaping: a =",a,"and b =",b)

script(10,20)
swap2(4,5)