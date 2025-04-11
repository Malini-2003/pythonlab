n = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in n.split()]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate numbers are:", duplicates)



