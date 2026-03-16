"""
Python Variables Tutorial
Author: Fahad Hossain
Description: Basic examples of Python variables, types, casting,
naming conventions, scope, and constants.
"""

# -----------------------------------
# 1. Declaring Variables
# -----------------------------------

month = "May"
age = 23

# Memory location of variables
print("Memory address of month:", id(month))
print("Memory address of age:", id(age))

# Direct memory address of values
print("Memory address of 'May':", id("May"))
print("Memory address of 23:", id(23))


# -----------------------------------
# 2. Different Types of Variables
# -----------------------------------

counter = 100        # Integer variable
miles = 1000.0       # Float variable
name = "Zara Ali"    # String variable

print(counter)
print(miles)
print(name)


# -----------------------------------
# 3. Deleting a Variable
# -----------------------------------

del counter
# print(counter)  # This would raise an error because the variable is deleted


# -----------------------------------
# 4. Checking Variable Types
# -----------------------------------

x = "Zara"
y = 10
z = 10.10

print(type(x))
print(type(y))
print(type(z))


# -----------------------------------
# 5. Type Casting
# -----------------------------------

x = str(10)
y = int(10)
z = float(10)

print("x =", x)
print("y =", y)
print("z =", z)


# -----------------------------------
# 6. Case Sensitivity
# -----------------------------------

age = 20
Age = 30   # Different variable

print("age =", age)
print("Age =", Age)


# -----------------------------------
# 7. Multiple Assignment
# -----------------------------------

a, b, c = 10, 20, 30
print(a, b, c)

# Same value assignment
a = b = c = 100
print(a, b, c)

# Different data types
a, b, c = 1, 2, "Zara Ali"

print(a)
print(b)
print(c)


# -----------------------------------
# 8. Naming Conventions
# -----------------------------------

counter = 100
_count = 100
name1 = "Zara"
name2 = "Nuha"
Age = 20
zara_salary = 100000

print(counter)
print(_count)
print(name1)
print(name2)
print(Age)
print(zara_salary)


# -----------------------------------
# Invalid Variable Names (Examples)
# -----------------------------------

# 1counter = 100      # Cannot start with number
# $_count = 100       # Special characters not allowed
# zara-salary = 100000  # Hyphen not allowed


# -----------------------------------
# 9. Local Variable Example
# -----------------------------------

def sum(x, y):
    result = x + y
    return result

print(sum(5, 10))


# -----------------------------------
# 10. Global Variable Example
# -----------------------------------

x = 5
y = 10

def sum():
    result = x + y
    return result

print(sum())


# -----------------------------------
# 11. Constant Example
# -----------------------------------

PI_VALUE = 3.1416