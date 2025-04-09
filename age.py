def ticket():
    age=int(input("Enter your age:"))
    if age < 5:
        print("Ticket price: FREE")
    elif 5 <= age < 18:
        print("Ticket price: $100")
    elif 19 <= age < 60:
        print("Ticket price: $200")
    elif age > 60:
        print("Ticket price: $150")
ticket()        

