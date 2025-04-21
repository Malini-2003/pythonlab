inventory = {
    "apple": 10,
    "banana": 8,
    "orange": 15,
    "mango": 5
}

print("Current Inventory:")
for item, qty in inventory.items():
    print(f"{item.capitalize()}: {qty}")

item_name = input("\nEnter the item name to sell: ").lower()
quantity_to_sell = int(input("Enter the quantity to sell: "))

if item_name in inventory:
    if quantity_to_sell <= inventory[item_name]:
        inventory[item_name] -= quantity_to_sell
        print(f"\nSold {quantity_to_sell} {item_name}(s). Remaining: {inventory[item_name]}")
    else:
        print(f"\nNo stock Only {inventory[item_name]} {item_name}(s) left.")
else:
    print(f"\nItem '{item_name}' not found in inventory.")

print("\nUpdated Inventory:")
for item, qty in inventory.items():
    print(f"{item.capitalize()}: {qty}")
