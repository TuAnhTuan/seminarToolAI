# Modify one line of code to make the code work
def foobar(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("foobar")
        elif i % 3 == 0:
            print("foo")
        elif i % 5 == 0:
            print("bar")
        else:
            print(i)

foobar(15)


# Create a function with comment and function name

# Function that computes the average of a dataset
def compute_average(dataset):
    sum = 0
    for number in dataset:
        sum += number
    return sum / len(dataset)

# Can you create a unit test for this function
def leap_year(year):
    """Determine if a year is a leap year or not"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Fix the code below
def divide_numbers(a, b):
    return a / b


