numbers =[10, 20, 5, 8, 25, 3]

def largest(numbers):
    num = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] > num:
            num = numbers[i]
    return num

print(largest(numbers))
