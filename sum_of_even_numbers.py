def sum_of_even_numbers(start, end):
    even_sum = 0
    
    for number in range(start, end + 1):
        if number % 2 == 0:  
            even_sum += number  
    
    return even_sum

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = sum_of_even_numbers(start, end)
print(f" Start={start}, End={end} is: {result}")
