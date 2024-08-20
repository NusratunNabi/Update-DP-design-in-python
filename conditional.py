# Assignment 1: Write a Python script that determines if a number is positive, negative, or zero using if-elif-else.
# Write your code below:

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Section 2: Logical and Boolean Operations
# -----------------------------------------
# Logical operators (and, or, not) are used to combine conditional statements.

# Assignment 2: Create a script that checks if a person is eligible for a senior citizen discount based on age and residency.
# Write your code below:
# Input age and residency status
age = int(input("Enter age: "))
residency = input("a resident?: ").lower()

if age >= 60 and residency == "yes":
    print("eligible for a senior citizen discount.")
else:
    print("not eligible for a senior citizen discount.")


# Section 3: Real-World Applications
# -----------------------------------
# Applying conditional logic to solve real-world problems.
# Assignment 3: Write a script that simulates a basic login system. Check username and password correctness.
# Write your code below:
# Dictionary to store usernames and passwords
details = {
    'Nusrat1': '1234',
    'Shari2': '5678',
    'Shifa3': '9876'
}

def login(username, password):
    if username in details and details[username] == password:
        return True
    else:
        return False

username = input("Enter your username: ")
password = input("Enter your password: ")

if login(username, password):
    print("Login successful! Welcome, {}.".format(username))
else:
    print("Invalid username or password. Please try again.")


# Assignment 4: Implement a system that categorizes a day based on temperature and weather conditions.
# Use nested if-elif-else and logical operators to determine if it's a beach day, skiing day, or a stay-home day.
temperature = 30  # in Celsius
weather = "sunny"

if weather == "sunny":
    if temperature > 25:
        print("It's a perfect beach day.")
    elif temperature > 15:
        print("It's a nice day for a walk.")
    else:
        print("It's sunny but too cold, stay home.")
elif weather == "snowy":
    if temperature < 0:
        print("Great day for skiing.")
    else:
        print("Snowy but not ideal for skiing, stay home.")
else:
    print("Not a sunny or snowy day, best to stay indoors.")
