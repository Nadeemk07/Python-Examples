def findsum():
    a = 0
    b = n-1
    while(a < b):
        if(arr[a]+arr[b] == sum):
            return True
        elif(arr[a]+arr[b] < sum):
            a = a+1
        elif(arr[a]+arr[b] > sum):
            b = b-1
        else:
            return False


arr = [3, 5, 9, 2, 8, 10, 11]
sum = 18
n = len(arr)
print(findsum())
