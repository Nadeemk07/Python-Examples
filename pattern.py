def pattern():
    store = ""
    pattern_char = input("enter pattern charcter:")
    for num in range(value):
        output = (num+1)*pattern_char
        store = store+"+" + output

    print(store[1:])


value = int(input("Enter the value"))
pattern()
