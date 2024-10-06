# Simple Python program to calculate the area of a rectangle

# Function to calculate area
def calculate_area(length, width):
    return length * width

# Main part of the program
if __name__ == "__main__":
    # Define the length and width of the rectangle
    length = 5
    width = 10
    
    # Call the function to calculate the area
    area = calculate_area(length, width)
    
    # Display the result
    print(f"The area of the rectangle is: {area}")
