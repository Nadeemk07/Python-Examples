# rotating element By d

def rotation(arr, n, d):
    for i in range(0, d):
        rotate_by_one(arr, n)

# rotating element one by one


def rotate_by_one(arr, n):
    temp = arr[0]
    for i in range(0, n-1):

        arr[i] = arr[i+1]
    arr[n-1] = temp

# Printing the rotated array


def rotated_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# checking with same output
arr = [1, 2, 3, 4, 5, 6, 7]
rotation(arr, 7, 3)
rotate_by_one(arr, 7)
rotated_array(arr, 7)

# TC=O(N*D) SC=O(1)
