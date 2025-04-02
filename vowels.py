def vowels(string):
    return sum(ch in 'aeiou' for ch in string.lower())

print(vowels('MALINI'))
