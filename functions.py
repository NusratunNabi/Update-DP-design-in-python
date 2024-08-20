# Assignment 1: Write a function that calculates the factorial of a number and handles any potential errors.
def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("Error: The number must be a non-negative integer.")
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 10:", factorial(10))
