# Import the math module
import math

# Define the function to calculate the area of a circle
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    area = math.pi * (radius ** 2)  # Calculate the area
    return area  # Return the result

# Example usage
radius = 5
result = circle_area(radius)

# Print the formatted output
print(f"The area of a circle with radius {radius} is: {result:.2f}")
