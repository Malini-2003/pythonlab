
def reg_user(name,email):
    
    name=name.strip().title()
    email=email.strip().lower()
    if "@" not in email or "." not in email:
        return "Invalid email address"
    print(f"Welcome,{name}!")
    print(f"Registeration email:{email}")
    return "Registeration successful"

    
name=input("Enter the name:")
email=input("Enter the email:" )
result=reg_user(name,email)
print(result)
