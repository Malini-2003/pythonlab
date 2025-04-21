names = ["Anusha", "Anandi", "Bobby", "Charlie", "Chandru", "Diya", "Dhanush", "Banu"]

grouped_names = {}

for name in names:
    first_letter = name[0]  

    if first_letter not in grouped_names:
        grouped_names[first_letter] = []

    grouped_names[first_letter].append(name)

print(grouped_names)
