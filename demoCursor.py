# Recommendation: refactor the code with multiple cursors

def foobar(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fixbug")
        elif i % 3 == 0:
            print("fix")
        elif i % 5 == 0:
            print("bug")
        else:
            print(i)

foobar(15)

# Function to compute the average of a dataset
def compute_average(dataset):
    total = sum(dataset)
    average = total / len(dataset)
    return average

dataset = [10, 20, 30, 40, 50]
average = compute_average(dataset)
print("The average is: ", average)

# Create test for the function
def leap_year(year):
    """Determine if a year is a leap year or not"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Fix the code below
def divide_numbers(a, b):
    return a / b

print(divide_numbers(10, 2))