def generate(n):
    arr = []
    for i in range(n):
        if len(arr) == 0:
            arr.append(1)
            continue
        if (2*i) % 10 == 0:
            num = arr[i-1] + 2*(i+1)
            arr.append(num)
            continue
        element = arr[i-1] + 2*i
        arr.append(element)
    return arr

arr = generate(100)
print(arr)