# Python Modules, Packages, Libraries, and Pip: In-Depth Guide

"""
nUSRATUN NABI
ID: C193255
Email: c193255@ugrad.iiuc.ac.bd
"""

# Section 1: Modules
# ------------------
# A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix '.py'.

# Section 2: Packages
# -------------------
# A package is a collection of Python modules under a common namespace. In most cases, a package is a directory containing a special `__init__.py` file.

# Section 3: Libraries
# --------------------
# A library in Python is a collection of modules and packages aimed at solving particular problems or carrying out specific tasks.


# Assignments
# -----------
# Assignment 1: Create a simple package with at least two modules, each containing one function.

from Packages import module1, module2
print(module1.home())
print(module2.hobby())

# Assignment 2: Use pip to install any library that is new to you and write a small script to explore its functionality.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()

# Congratulations on completing the comprehensive section on Python's modules, packages, libraries, and pip!
# Review the assignments, try to solve them, and check your understanding of these essential Python features.
