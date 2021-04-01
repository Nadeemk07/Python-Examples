def search(arr):
    for i in range(0, len(arr)):
        if (arr[i] == value):
            print(f"Number found at index {i}")

        else:
            continue


arr = [1, 2, 3, 4, 5, 6, 7, 8]
value = int(input("Enter the No you want to search:-"))
search(arr)
