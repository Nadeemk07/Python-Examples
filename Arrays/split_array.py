def split(arr, n):
    temp = [None]*(2*n)
    for i in range(0, n):
        temp[i] = temp[i+n] = arr[i]
    return temp


def split_array(arr, n, k, temp):
    start = k % n
    for i in range(start, start+n):
        print(temp[i], end=" ")
    print(" ")


arr = [12, 10, 5, 6, 52, 36]
k = int(input("Enter the No:-"))
n = len(arr)
temp = split(arr, n)
split_array(arr, n, k, temp)
