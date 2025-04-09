def login():
    username=input("Enter the username:")
    password=input("Enter the password:")

    if username=="admin" and password=="1234":
        print("Login successful")
    else:
        print("Invalid Credentials")
login()
