# Assignments
# -----------
# Assignment 1: Write a script that processes a list of temperature readings. If any temperature is above a certain threshold, print a warning.
temperatures = [23, 31, 26, 32, 21,29]
threshold = 30
for temp in temperatures:
    if temp > threshold:
        print(f"Warning: Temperature {temp} exceeds threshold of {threshold} degrees.")

# Assignment 2: Given a list of users with their subscription status, write a loop that sends an email to all subscribed users.
users = [{"email": "user1@example.com", "subscribed": True},
         {"email": "user2@example.com", "subscribed": False},
         {"email": "user3@example.com", "subscribed": True}]
for user in users:
    if user["subscribed"]:
        print(f"Sending email to {user['email']}.")


# Assignments
# -----------
# Assignment 1: Create a script that processes a dictionary of products, checking stock levels and generating restock alerts if necessary.
products = {
    "laptop": {"stock": 5, "min_required": 15},
    "smartphone": {"stock": 20, "min_required": 6}
}

for product, details in products.items():
    if details["stock"] < details["min_required"]:
        print(f"Alert: {product} stock is low. Please restock.")
    else:
        print(f"{product} stock is sufficient.")
