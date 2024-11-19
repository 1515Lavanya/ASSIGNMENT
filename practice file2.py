Built-in Functions
Python provides a variety of built-in functions that are commonly used. Here are some examples:

len()

Returns the length of an object (e.g., string, list).
python
Copy code
my_list = [1, 2, 3]
print(len(my_list))  
max() and min()

Returns the largest or smallest item in an iterable.
python
Copy code
numbers = [10, 20, 5, 30]
print(max(numbers))  
print(min(numbers))  
sum()

Returns the sum of all items in an iterable.
python
Copy code
total = sum([1, 2, 3, 4])
print(total)  
sorted()

Returns a new sorted list from the items of an iterable.
python
Copy code
my_list = [3, 1, 4, 2]
print(sorted(my_list))  
type()

Returns the type of an object.
python
Copy code
print(type(42))  
str(), int(), float()

Convert values to a specified type.
python
Copy code
print(int("42"))      
print(float("3.14"))  
range()

Generates a sequence of numbers.
python
Copy code
for i in range(5):
    print(i)  
print()

Outputs data to the console.
python
Copy code
print("Hello, World!") 
Custom Functions
Custom functions are user-defined functions created to perform specific tasks that are not covered by built-in functions. Here are some examples:

Basic Custom Function
python
Copy code
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  
Function to Calculate Factorial
python
Copy code
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  
Function with Default Parameters
python
Copy code
def power(base, exponent=2):
    return base ** exponent

print(power(3))      
print(power(3, 3))   
Function with Variable Arguments
python
Copy code
def average(*args):
    return sum(args) / len(args) if args else 0

print(average(1, 2, 3, 4))  
Function to Filter Odd Numbers
python
Copy code
def filter_odd(numbers):
    return [num for num in numbers if num % 2 != 0]

print(filter_odd([1, 2, 3, 4, 5]))  
Function with Keyword Arguments
python
Copy code
def describe_pet(name, animal_type="dog"):
    print(f"{name} is a {animal_type}.")

describe_pet("Buddy")  
describe_pet("Whiskers", "cat")  
