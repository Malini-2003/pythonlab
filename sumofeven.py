even= [n**2 for n in range(1, 21) if n % 2 == 0]

sum= sum(even)

print(f"The list of squares of even numbers from 1 to 20 is: {even}")
print(f"The sum of these squares is: {sum}")
