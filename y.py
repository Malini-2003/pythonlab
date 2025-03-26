#Tking user input
y=int(input("Enter a year:"))

leap_y="LEAP YEAR"if(y%4==0 and y%100!=0)or(y%400==0)else"NOT LEAP YEAR"
print(f"{y} is a {leap_y}")
