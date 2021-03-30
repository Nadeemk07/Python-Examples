def sum():
    total_sum = 0
    for num in range(1, n+1):
        total_sum += num

    print(f"The sum is {total_sum}")


n = int(input("Enter the no. till which u need sum"))

sum()
