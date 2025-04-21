all_customers = {"John", "Mary", "Steve", "Ana"}

returned_customers = {"Mary", "Ana"}

non_returning_customers = list(set(all_customers) - set(returned_customers))

print(non_returning_customers)
