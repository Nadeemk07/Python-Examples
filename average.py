

def average():
    total_sum = 0
    for num in range(n):
        number = int(input("enter the number:"))
        total_sum = total_sum+number
    output = total_sum/n
    print(output)


n = int(input("Enter how many no:"))

average()
