def occurrences(string, char_to_count):
    return string.count(char_to_count)

string = input("Enter the string: ")
char_to_count = input("Enter the character to count: ")

result =occurrences(string, char_to_count)
print(f"The character '{char_to_count}' occurs {result} times in the string.")
