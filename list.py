def remove(string,char_to_remove):
    return input_string.replace(char_to_remove, '')

string = input("Enter the string: ")
char_to_remove = input("Enter the character to remove: ")

result = remove(string, char_to_remove)
print("Modified string:", result)
