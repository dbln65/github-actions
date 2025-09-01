# simple_app.py

# Function to calculate the square of a number
def square(x):
    return x * x

# Function to calculate the cube of a number
def cube(x):
    return x * x * x

# Main program
if __name__ == "__main__":
    numbers = [2, 3, 4]
    
    print("Squares:")
    for n in numbers:
        print(f"{n}^2 = {square(n)}")
    
    print("\nCubes:")
    for n in numbers:
        print(f"{n}^3 = {cube(n)}")

