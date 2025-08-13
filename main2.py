def oddocuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n= int(input("enter srrays size"))
while(n):
    num = int(input("enter number:"))
    arr.append(num)
    n-=1

print("oddocuring number is",oddocuring(arr))