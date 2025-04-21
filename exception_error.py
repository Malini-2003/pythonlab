my_dict = {
    0: "apple",
    1: "banana",
    2: "cherry",
    3: "date",
    4: "elderberry"
}

try:
    key = int(input("Enter a key (0 to 4): "))
    
    value = my_dict[key]
    
    print(f"The value at key {key} is: {value}")

except KeyError:
    print("Error: The key you entered does not exist in the dictionary.")
except ValueError:
    print("Error: Please enter a valid number.")
