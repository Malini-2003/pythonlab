my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
    "date": 4
}

try:
    key = input("Enter a key (apple, banana, cherry, date): ").lower()  
    value = my_dict[key] 
    print(f"The value for '{key}' is: {value}")

except KeyError:
    print("Error: The key you entered does not exist in the dictionary.")
