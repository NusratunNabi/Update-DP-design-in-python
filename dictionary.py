# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.
# Write your code below:
student = {
    'name': 'Nusrat','roll_number': 55,'grades': {'Physics': 85, 'Math': 90, 'Chemistry': 80}
} 
print("Before:",student)
student['grades']['Biology']=82 #adding new subject and grade
removed_value = student['grades'].pop('Math') # removing
student['grades']['Biology'] = 90 #updating
print("After:",student)

# Section 2: Integrating Dictionaries with Lists and Tuples
# ---------------------------------------------------------
# Dictionaries can be used with lists and tuples to create complex data structures.

# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.
# Write your code below:
student_grades = {
    'Nusrat': [82, 85, 92],
    'Rafi': [89, 81, 75],
    'Nisha': [90, 78, 80]
}

average_grades = {}
for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    average_grades[student] = average_grade

print("Average Grades:")
for student, average_grade in average_grades.items():
    print(f"{student}: {average_grade:.3f}")
    
# Congratulations on completing the advanced section on Python dictionaries!
# Review the assignments, try to solve them, and check your understanding of this powerful data structure.
