def vowels(string):
    return sum(ch in 'aeiou' for ch in string.lower())

print(vowels('Hello World'))
print(vowels('Python'))
print(vowels('Beautiful Day'))

