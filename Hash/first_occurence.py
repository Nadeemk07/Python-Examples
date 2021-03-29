def first_occurance(arr):
    h = {}
    for ch in arr:
        if ch in h:
            return ch
        else:
            h[ch] = 0
    return '\0'


arr = [1, 2, 2, 3, 3, 4]
print(first_occurance(arr))
