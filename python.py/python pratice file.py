Defining a Function
You define a function using the def keyword followed by the function name and parentheses. You can also include parameters.

python
Copy code
def greet(name):
    print(f"Hello, {name}!")
Calling a Function
You call a function by using its name followed by parentheses. You can pass arguments into the function through these parentheses.

python
Copy code
greet("Alice")  
Parameters and Arguments
Functions can take parameters, which are specified in the function definition. When you call the function, you provide arguments for these parameters.

python
Copy code
def add(a, b):
    return a + b

result = add(5, 3)  
Default Parameters
You can assign default values to parameters. If the caller does not provide an argument for that parameter, the default value is used.

python
Copy code
def multiply(a, b=1):
    return a * b

print(multiply(5))   
print(multiply(5, 2))  
Return Statement
The return statement is used to exit a function and send back a value.

python
Copy code
def square(x):
    return x ** 2

print(square(4))  
Variable Scope
Variables defined inside a function are local to that function. They cannot be accessed outside of it.

python
Copy code
def my_function():
    local_var = 10
    return local_var

print(my_function())  
Lambda Functions
Python also supports anonymous functions, or lambda functions, which are defined using the lambda keyword. These are typically used for short, throwaway functions.

python
Copy code
square = lambda x: x ** 2
print(square(5))  
Examples
Function with Multiple Parameters:

python
Copy code
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(10, 2))  
Function with Keyword Arguments:

python
Copy code
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="hamster", pet_name="Harry")
Function with Arbitrary Arguments:

python

def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, "pepperoni", "mushrooms", "extra cheese")