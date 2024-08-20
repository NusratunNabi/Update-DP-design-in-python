# Assignment 1: Create a string that contains a simple bio data like name, age, and country. Extract each piece of information and print them separately.
# Write your code below:
# Simple bio data string
data = "Name: Nusrat, Age: 25, Country: Bangladesh, Blood_group: O+"

name = data.split(", ")[0].split(": ")[1]
age = data.split(", ")[1].split(": ")[1]
country = data.split(", ")[2].split(": ")[1]
blood_group= data.split(", ")[3].split(": ")[1]

print("Name:", name)
print("Age:", age)
print("Country:", country)
print("Blood_groupy:", blood_group)


# Section 2: Advanced String Operations
# -------------------------------------
# Strings can be used in more complex operations like formatting.

# Assignment 2: Create a formatted string that includes data from a list or dictionary. For example, use a dictionary to store a person's information and format a string to include it.
# Write your code below:
# Dictionary to store person's information
info = {
    'name': 'Nusrat',
    'age': 25,
    'country': 'Bangladesh'
}
intro = f"Name: {name}, Age: {age}, Country: {country}".format(info)
print(intro)


# Section 3: Advanced Slicing and Multiline Strings
# -------------------------------------
# Python strings are immutable, which means that every string operation creates a new string.

# Assignment 3: Write a function that takes a string and returns a dictionary with the counts of each character in the string.
# Write your code below:
def count_characters(s):
    
    char_counts = {} #empty dictionary for counts store

    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

string = "My name is Nusrat"
print("display the output like dictionary: ")
print(count_characters(string))


# Section 4: Regular Expressions
# ------------------------------
# Regular expressions are used for pattern matching in strings.
# Assignment: Write a regex to find all the hashtags in a string.

import re
text_with_hashtags = "This is a #great day to learn #regex in #Python!"
hashtags = re.findall(r"#(\w+)", text_with_hashtags)
print("Hashtags:", hashtags)

# Congratulations on completing the advanced section on Python strings!
# Review the assignments, try to solve them, and check your understanding of string manipulation techniques.
