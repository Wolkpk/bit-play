def TwoOdd(arr, size):
    xaraof2 = arr[0]
    x = 0
    y = 0
    SetBit=0
    for i in range(1,size):

        xaraof2 = xaraof2 ^ arr[i]
    SetBit = xaraof2 & ~(xaraof2-1)
    for i in range(size):
        if(arr[i]& SetBit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("TowOdd elements are",x,"&",y)

arr = []
arr_size = int(input("enter the size of aray"))
for i in range(0,arr_size):
    z = int(input("enter element"))
    arr.append(z)

TwoOdd(arr, arr_size)