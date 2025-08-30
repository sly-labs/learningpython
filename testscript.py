# Define a constant for the acceleration due to gravity (in m/s²)
# Constants are typically named in uppercase to indicate they should not be modified
GRAVITY = 10

# Declare variables (values that can change)
mass = 5.0  # Mass of the object in kilograms
time = 10   # Time in seconds

# Calculate the velocity of a free-falling object after the given time
velocity = GRAVITY * time  # Formula: v = g * t

# Print the constant, variables, and result
print("Constant and Variable Values:")
print("Gravity:", GRAVITY, "m/s²")  # Output the constant
print("Mass:", mass, "kg")          # Output a variable
print("Time:", time, "s")           # Output another variable
print("Calculated Velocity:", velocity, "m/s")  # Output the result

# Update the mass variable to demonstrate mutability
mass = 10.0  # Changing the value of the variable
print("\nUpdated Mass:", mass, "kg")  # Print the updated value
# It does not work

