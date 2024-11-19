





1. Creating a List

my_list = [1, 2, 3, 4, 5]

2. Accessing Elements

first_element = my_list[0]  # Access first element
last_element = my_list[-1]   # Access last element

3. Slicing

sub_list = my_list[1:4]  # Get elements from index 1 to 3
4. Adding Elements

my_list.append(6)  # Add an element to the end
my_list.insert(0, 0)  # Insert an element at a specific position
5. Removing Elements
my_list.remove(3)  # Remove the first occurrence of a value
popped_element = my_list.pop()  # Remove and return the last element
6. Finding Elements

index_of_value = my_list.index(2)  # Get the index of a value
exists = 4 in my_list  # Check if a value exists in the list
7. Sorting and Reversing

my_list.sort()  # Sort the list in place
my_list.reverse()  # Reverse the list in place
8. Length of a List

length = len(my_list)  # Get the number of elements in the list
9. Iterating Through a List

for item in my_list:
    print(item)
10. List Comprehensions
squared = [x**2 for x in my_list]  # Create a new list with squared values
nums = [1,4,9,16,25,36,49,64,81,100]

