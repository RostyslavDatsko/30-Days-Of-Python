# Check the data type of all your variables using type() built-in function
# Using the len() built-in function, find the length of your first name
# Compare the length of your first name and your last name
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
# Subtract num_two from num_one and assign the value to a variable diff
# Multiply num_two and num_one and assign the value to a variable product
# Divide num_one by num_two and assign the value to a variable division
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# Calculate num_one to the power of num_two and assign the value to a variable exp
# Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names


first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Ross', 'Datsko', 'Rostyslav Datsko', 'Canada', 'Toronto', 24, 2026, False, True, False

print(type(first_name), type(last_name), type(full_name), type(country), type(city), type(age), type(year), type(is_married), type(is_true), type(is_light_on))
print(len(first_name))
print(max(len(last_name), len(first_name)))

num_one = 5
num_two = 4
print("Total:", num_one + num_two)
print("Difference:", num_one - num_two)
print("Product:", num_one * num_two)
print("Division:", num_one / num_two)
print("Remainder:", num_one % num_two)
print("Exponentiation:", num_one ** num_two)
print("Floor Division:", num_one // num_two)

r = 30
print("Area of Circle:", 3.14 * r ** 2)
print("Circumference of Circle:", 2 * 3.14 * r)

input_radius = input("Enter radius: ")
print("Area of Circle:", 3.14 * int(input_radius) ** 2)

input_first_name = input("Enter first name: ")
input_last_name = input("Enter last name: ")
input_country = input("Enter country: ")
input_age = int(input("Enter age: "))

print("First Name:", input_first_name)
print("Last Name:", input_last_name)
print("Country:", input_country)
print("Age:", input_age)