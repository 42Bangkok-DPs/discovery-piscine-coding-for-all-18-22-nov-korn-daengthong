#!/usr/bin/env python3

# Define the original array of numbers
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Use a set to create a new array by adding 2 to each value in the original array that is greater than 5
new_array_set = {x + 2 for x in original_array if x > 5}

# Convert the set back to a sorted list for display purposes
new_array = sorted(new_array_set)

# Display both arrays
print(f"{original_array}$")
print(f"{new_array}$")