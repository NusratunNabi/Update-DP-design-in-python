# Section 1: Math Module
# ----------------------
# The math module provides access to mathematical functions and constants.
import math
# Section 2: Datetime Module
# --------------------------
# The datetime module allows you to manipulate dates and times.
# Assignments
# -----------
# Assignment 1: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).
def compound_interest(principal, rate, time, n):
    amount = principal * (1 + r / n) ** (n * t)
    interest = amount - principal
    return interest

p = 5000
r = 0.08  
t = 6     
n = 10   
interest = compound_interest(p, r, t, n)
print("Compound interest earned:", round(interest, 2))

# Assignment 2: Create a script that prints the current time and updates every second.
import datetime
import time

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    print("Current Time:", current_time)
    
    time.sleep(1)
