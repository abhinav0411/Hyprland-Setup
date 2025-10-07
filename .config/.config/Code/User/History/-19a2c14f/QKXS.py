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

def add(n):
    arr = generate(n)
    sum_n = 0
    for i in range(n):
        sum_n += arr[i]
    return sum_n

arr = generate(100)
print(arr)

sum_hundred = add(100)
print(sum_hundred)


# Level 2
def odd(arr):
    new_arr = []
    for i in range(len(arr)):
        digit = 0
        num = arr[i]
        while num > 0:
            digit = num % 10
            num = num // 10
        if digit % 2 != 0:
            new_arr.append(arr[i])
    return new_arr

odd_arr = odd(arr)
print(odd_arr)    
print(len(odd_arr))

# Level 3
def descending(arr):
    new_arr = []
    for num in arr:
        digit_arr = []
        element = num
        while num > 0:
            digit = num % 10
            num = num // 10
            digit_arr.append(digit)
        n = len(digit_arr)
        x = 0
        for i in range(1, n):
            if digit_arr[i-1] < digit_arr[i]:
                x += 1
        if x == n:
            new_arr.append(element)
    return new_arr

desc_arr = descending(arr)