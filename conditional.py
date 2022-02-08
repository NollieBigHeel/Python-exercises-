# Else statement
deposit = 10
password = "password"

if 0 < deposit <= 100 and password == "password":
    print(f"Thank you for depositing £{deposit}!")
else:
    print("Failed to make a deposit.")

    
deposit = 0
password = "password"

if 0 < deposit <= 100 and password == "password":
    print(f"Thank you for depositing £{deposit}!")
else:
    print("Failed to make a deposit.")

# elif statement - exercise 1
age = int(input("Enter your age: "))

if age >= 85:
    print("You are above 85")
elif age >= 50:
    print("You are between 50 and 85")
elif age >= 20:
    print("You are between 20 and 50")
else:
    print("You are below 20 years old")   
        
# exercise 2

mark = int(input("Please input students mark:"))

if mark > 85:
   print("Distinction")
elif 65 <= mark <= 85:
    print("Pass")
else:
    print("Fail")



