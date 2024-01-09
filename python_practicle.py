# Function to convert a number to binary
def convert_to_binary(num):
    binary_representation = bin(num)[2:]
    return binary_representation

# Function to grade marks
def grade_marks(marks):
    if marks >= 80:
        return "Grade O"
    elif 60 <= marks < 80:
        return "Grade A"
    else:
        return "Invalid"

# Function to check if a number is even or odd
def check_even_odd(a):
    return "Even" if a % 2 == 0 else "Odd"

# Function to determine gender
def determine_gender(gender):
    gender = gender.lower()
    if gender == "male":
        return "You are male"
    elif gender == "female":
        return "You are female"
    else:
        return "You are transgender"

# Function to find the greatest among three numbers
def find_greatest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is greater"
    elif num2 > num1 and num2 > num3:
        return f"{num2} is greater"
    elif num3 > num1 and num3 > num2:
        return f"{num3} is greater"
    else:
        return "Invalid"

# Function using break statement
def break_example(n):
    for i in range(n):
        if i == 7:
            break
        print(i)

# Function using continue statement
def continue_example(n):
    for i in range(n):
        if i == 7:
            continue
        print(i)

# Function using pass statement
def pass_example(n):
    for i in range(n):
        if i == 7:
            pass
        print(i)

# Function to calculate factorial
def calculate_factorial(n):
    factorial = 1
    if n < 0:
        return "Invalid"
    elif n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Function to check list mutability
def check_list_mutability():
    list1 = [1, 2, "yadav"]
    list1[1] = 'yadav'
    return list1

# Function to check tuple immutability
def check_tuple_immutable():
    tuple1 = (1, 2, "yadav")
    # The line below will raise an error since tuples are immutable
    # tuple1[2] = 'ayush'
    return tuple1

# Function to calculate sum until the user is satisfied
def calculate_sum_until_satisfied():
    total_amt = 0
    count = 0
    while True:
        amt = int(input("Enter subsequent amount (enter 0 to exit): "))
        if amt == 0:
            break
        total_amt += amt
        count += 1
        if count == 3:
            break
    return total_amt

# Function to count the number of digits in a number
def count_digits_in_number(number):
    num_digits = len(str(abs(number)))
    return num_digits

# Function to generate Fibonacci series
def generate_fibonacci_series(x):
    fibonacci_series = [0, 1]
    for i in range(2, x):
        fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
    return fibonacci_series

# Function to calculate factorial using recursion
def calculate_factorial_recursive(x):
    if x <= 1:
        return 1
    else:
        return x * calculate_factorial_recursive(x - 1)

# Example usage
if __name__ == "__main__":
    # You can call the functions here with appropriate arguments
    print(convert_to_binary(10))
    print(grade_marks(75))
    print(check_even_odd(7))
    print(determine_gender("Male"))
    print(find_greatest(5, 10, 7))
    break_example(10)
    continue_example(10)
    pass_example(10)
    print(calculate_factorial(5))
    print(check_list_mutability())
    print(check_tuple_immutable())
    print(calculate_sum_until_satisfied())
    print(count_digits_in_number(12345))
    print(generate_fibonacci_series(10))
    print(calculate_factorial_recursive(5))
