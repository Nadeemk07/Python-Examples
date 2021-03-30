def first_last():
    for num in range(n):
        value = input("enter the value to add:")
        list.append(value)

    print(f"The first and last values are {list[0]},{list[n-1]} respectively.")


list = []
n = int(input("enter the no. values that are added to the list:"))

first_last()
