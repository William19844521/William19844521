


print ("hello world")# 1. Store first name in all lowercase
first_name = "William"

# 2. Store last name in all uppercase
last_name = "Maina"

# 3. Print greeting with converted cases
print("Hello,",  last_name.lower())

# 4. Print two newlines
print("\n\n")

# 5. Combine names into a new variable
full_name = first_name + " " + last_name

# 6. Slice last name and print in one line
print(full_name.split()[1])  # Extracting and printing last name in one line

# 7. Replace last name with a new phrase and print
full_name_updated = full_name.replace(last_name, "Maina, Walsh College Student")
print(full_name_updated)

# 8. Print quote with quotation marks
print('"Start by doing what\'s necessary; then do what\'s possible; and suddenly you are doing the impossible - Francis of Assisi"')

# 9. Store two decimal numbers
num1 = 12.5
num2 = 3.5

# 10. Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# 11. Print each operation result using different methods
# Concatenation
print(str(num1) + " plus " + str(num2) + " equals " + str(addition))

# String formatting expression
print("%s minus %s equals %s" % (num1, num2, subtraction))

# String formatting method
print(()"{} times {} equals {}".format(num1, num2, multiplication))

# f-String
print(f"{num1} divided by {num2} equals {division}")

# 12. Calculate and print square root of multiplication result (rounded to 2 decimal places)
import math
sq_root = round(math.sqrt(multiplication), 2)
print(f"The square root of {multiplication} equals {sq_root}")

# 13. Store current month and day
month = "April"
day = 12

# Print formatted date, tabbed over twice, with a different method
print("\t\tToday is day {12} of the month of {4}.".format(day, month))
