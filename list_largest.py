n = input("Enter numbers separated by spaces: ")

numbers = [int(num) for num in n.split()]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("Largest number is:", largest)
