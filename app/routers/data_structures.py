from fastapi import APIRouter
from app.models.data_structure_models import DataStructureExample, DataStructureResponse

router = APIRouter()

@router.get("/data-structures", response_model=DataStructureResponse)
async def data_structures_overview():
    """Provides an overview of basic Python data structures."""
    return DataStructureResponse(
        description="Basic Data Structures in Python",
        examples=[
            DataStructureExample(
                name="Lists",
                description="Ordered, mutable collections of items",
                code="""
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
print(fruits[0])       # First element
print(fruits[-1])      # Last element

# Slicing
print(fruits[1:])      # From second to the end
""",
                output="""
['apple', 'banana', 'cherry']
apple
cherry
['banana', 'cherry']
""",
                operations=[
                    {"operation": "append", "description": "Add an item to the end", "syntax": "list.append(item)"},
                    {"operation": "insert", "description": "Insert item at a position", "syntax": "list.insert(position, item)"},
                    {"operation": "remove", "description": "Remove first occurrence", "syntax": "list.remove(item)"},
                    {"operation": "pop", "description": "Remove & return item at position", "syntax": "list.pop(position)"},
                    {"operation": "sort", "description": "Sort the list in place", "syntax": "list.sort()"},
                    {"operation": "len", "description": "Get length of list", "syntax": "len(list)"}
                ],
                explanation="Lists are one of the most versatile and commonly used data structures in Python. They can store items of different types and offer various methods for manipulation."
            ),

            DataStructureExample(
                name="Tuples",
                description="Ordered, immutable collections of items",
                code="""
# Creating a tuple
coordinates = (10.5, 20.8)
print(coordinates)

# Tuple packing and unpacking
x, y = coordinates
print(f"X: {x}, Y: {y}")

# Immutability demonstration
try:
    coordinates[0] = 15  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")
""",
                output="""
(10.5, 20.8)
X: 10.5, Y: 20.8
Error: 'tuple' object does not support item assignment
""",
                operations=[
                    {"operation": "count", "description": "Count occurrences of value", "syntax": "tuple.count(value)"},
                    {"operation": "index", "description": "Find first occurrence", "syntax": "tuple.index(value)"}
                ],
                explanation="Tuples are similar to lists but are immutable, meaning their values cannot be changed after creation. They're commonly used for related values that shouldn't change, like coordinates or RGB color values."
            ),

            DataStructureExample(
                name="Dictionaries",
                description="Key-value pairs, unordered and mutable",
                code="""
# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)

# Accessing values
print(person["name"])

# Adding/modifying items
person["email"] = "john@example.com"
print(person)

# Dictionary methods
print(person.keys())
print(person.values())
print(person.items())
""",
                output="""
{'name': 'John', 'age': 30, 'city': 'New York'}
John
{'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}
dict_keys(['name', 'age', 'city', 'email'])
dict_values(['John', 30, 'New York', 'john@example.com'])
dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), ('email', 'john@example.com')])
""",
                operations=[
                    {"operation": "get", "description": "Get value with default", "syntax": "dict.get(key, default)"},
                    {"operation": "update", "description": "Update with another dict", "syntax": "dict.update(other_dict)"},
                    {"operation": "pop", "description": "Remove and return value", "syntax": "dict.pop(key)"},
                    {"operation": "clear", "description": "Remove all items", "syntax": "dict.clear()"}
                ],
                explanation="Dictionaries are useful when you want to associate keys with values, such as storing properties for an object or creating a mapping between related items."
            ),

            DataStructureExample(
                name="Sets",
                description="Unordered collections of unique items",
                code="""
# Creating a set
colors = {"red", "green", "blue", "red"}  # Duplicate removed
print(colors)

# Set operations
primary = {"red", "yellow", "blue"}
secondary = {"green", "purple", "orange"}

# Union (all elements from both sets)
print(primary | secondary)

# Intersection (elements in both sets)
rgb = {"red", "green", "blue"}
print(primary & rgb)

# Difference (elements in first set but not in second)
print(primary - rgb)
""",
                output="""
{'red', 'green', 'blue'}
{'red', 'yellow', 'blue', 'green', 'purple', 'orange'}
{'red', 'blue'}
{'yellow'}
""",
                operations=[
                    {"operation": "add", "description": "Add an element", "syntax": "set.add(item)"},
                    {"operation": "remove", "description": "Remove an element", "syntax": "set.remove(item)"},
                    {"operation": "union", "description": "Return union of sets", "syntax": "set.union(other_set)"},
                    {"operation": "intersection", "description": "Return intersection", "syntax": "set.intersection(other_set)"},
                    {"operation": "difference", "description": "Return difference", "syntax": "set.difference(other_set)"},
                    {"operation": "issubset", "description": "Test if subset", "syntax": "set.issubset(other_set)"}
                ],
                explanation="Sets are useful when you need to ensure elements are unique or when you need to perform mathematical set operations like unions, intersections, and differences."
            ),

            DataStructureExample(
                name="Strings",
                description="Immutable sequences of characters",
                code="""
# String operations
text = "Python data structures"
print(text.upper())
print(text.split())
print(text.replace("Python", "Basic"))

# String as sequence
print(text[0])         # First character
print(text[-1])        # Last character
print(text[7:11])      # Slice: "data"
""",
                output="""
PYTHON DATA STRUCTURES
['Python', 'data', 'structures']
Basic data structures
P
s
data
""",
                operations=[
                    {"operation": "upper/lower", "description": "Convert case", "syntax": "str.upper(), str.lower()"},
                    {"operation": "strip", "description": "Remove whitespace", "syntax": "str.strip()"},
                    {"operation": "split", "description": "Split into list", "syntax": "str.split(separator)"},
                    {"operation": "join", "description": "Join with string", "syntax": "separator.join(iterable)"},
                    {"operation": "find", "description": "Find substring position", "syntax": "str.find(substring)"},
                    {"operation": "replace", "description": "Replace occurrences", "syntax": "str.replace(old, new)"}
                ],
                explanation="Strings are sequences of characters and have many built-in methods for manipulation. They are immutable, meaning they cannot be changed after creation - methods that seem to modify strings actually create new strings."
            ),

            DataStructureExample(
                name="Arrays",
                description="Compact, typed arrays for numerical data (from the array module)",
                code="""
# Using Python's array module for homogeneous data
import array

# Create an array of integers (type code 'i')
numbers = array.array('i', [1, 2, 3, 4, 5])
print(numbers)

# Array operations
numbers.append(6)
print(numbers)

# Convert to list
print(list(numbers))

# Arrays support many list operations
print(numbers[0])     # First element
numbers[0] = 10       # Modify element
print(numbers)
""",
                output="""
array('i', [1, 2, 3, 4, 5])
array('i', [1, 2, 3, 4, 5, 6])
[1, 2, 3, 4, 5, 6]
1
array('i', [10, 2, 3, 4, 5, 6])
""",
                operations=[
                    {"operation": "append", "description": "Add item to end", "syntax": "array.append(item)"},
                    {"operation": "extend", "description": "Append items from iterable", "syntax": "array.extend(iterable)"},
                    {"operation": "insert", "description": "Insert before position", "syntax": "array.insert(i, x)"},
                    {"operation": "remove", "description": "Remove first occurrence", "syntax": "array.remove(x)"},
                    {"operation": "pop", "description": "Remove at index", "syntax": "array.pop([i])"},
                    {"operation": "fromlist", "description": "Append from list", "syntax": "array.fromlist(list)"}
                ],
                explanation="Arrays from the array module are more memory efficient than lists when storing large amounts of homogeneous numerical data. They require all elements to be of the same type, specified by a type code."
            ),

            DataStructureExample(
                name="Stacks",
                description="LIFO (Last-In-First-Out) data structure implementation with lists",
                code="""
# Using a list as a stack (LIFO - Last In, First Out)
stack = []

# Push operations (add to top)
stack.append("Task 1")
stack.append("Task 2")
stack.append("Task 3")
print(stack)

# Pop operations (remove from top)
last_task = stack.pop()
print(f"Processing: {last_task}")
print(f"Remaining: {stack}")

# Check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print(f"Stack has {len(stack)} items left")
""",
                output="""
['Task 1', 'Task 2', 'Task 3']
Processing: Task 3
Remaining: ['Task 1', 'Task 2']
Stack has 2 items left
""",
                explanation="Stacks follow the Last-In-First-Out (LIFO) principle. The last item added is the first one to be removed. In Python, a list can be used as a stack using append() to push and pop() to remove items."
            ),

            DataStructureExample(
                name="Queues",
                description="FIFO (First-In-First-Out) data structure using collections.deque",
                code="""
# Using collections.deque as a queue (FIFO - First In, First Out)
from collections import deque

queue = deque()

# Enqueue operations (add to end)
queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")
print(queue)

# Dequeue operations (remove from front)
first_customer = queue.popleft()
print(f"Serving: {first_customer}")
print(f"Waiting: {queue}")

# deque supports adding to both ends
queue.appendleft("VIP Customer")
print(queue)
""",
                output="""
deque(['Customer 1', 'Customer 2', 'Customer 3'])
Serving: Customer 1
Waiting: deque(['Customer 2', 'Customer 3'])
deque(['VIP Customer', 'Customer 2', 'Customer 3'])
""",
                explanation="Queues follow the First-In-First-Out (FIFO) principle. Python's deque from the collections module is optimized for fast appends and pops from both ends, making it ideal for queue implementations."
            ),

            DataStructureExample(
                name="Named Tuples",
                description="Tuple subclass with named fields",
                code="""
# Named tuples for more readable code
from collections import namedtuple

# Define the named tuple structure
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(1, 2)
p2 = Point(3, 4)

# Access by name or position
print(f"p1.x: {p1.x}, p1[0]: {p1[0]}")

# Unpack like regular tuples
x, y = p2
print(f"Unpacked: x={x}, y={y}")

# Immutable like regular tuples
try:
    p1.x = 5  # This will raise an error
except AttributeError as e:
    print(f"Error: {e}")
""",
                output="""
p1.x: 1, p1[0]: 1
Unpacked: x=3, y=4
Error: can't set attribute
""",
                explanation="Named tuples combine the benefits of tuples (immutability, unpacking) with the readability of accessing elements by name instead of position. They're great for representing simple objects or records with a fixed set of attributes."
            ),

            DataStructureExample(
                name="Default Dictionaries",
                description="Dictionaries with default values for missing keys",
                code="""
# Using defaultdict to handle missing keys
from collections import defaultdict

# Create a defaultdict that provides 0 for missing keys
word_count = defaultdict(int)

# Count words in a sentence
for word in "the quick brown fox jumps over the lazy dog".split():
    word_count[word] += 1

print(word_count)

# Defaultdict with list as default factory
groups = defaultdict(list)
people = [('Math', 'Alice'), ('Science', 'Bob'),
          ('Math', 'Charlie'), ('History', 'David')]

for subject, name in people:
    groups[subject].append(name)

print(groups)
""",
                output="""
defaultdict(<class 'int'>, {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
defaultdict(<class 'list'>, {'Math': ['Alice', 'Charlie'], 'Science': ['Bob'], 'History': ['David']})
""",
                explanation="defaultdict is a subclass of dict that calls a factory function to provide default values for missing keys. This eliminates the need to check if a key exists before modifying its associated value."
            )
        ]
    )

@router.get("/data-structures/lists", response_model=DataStructureResponse)
async def lists_examples():
    """Provides detailed examples of Python lists."""
    return DataStructureResponse(
        description="Lists in Python",
        examples=[
            DataStructureExample(
                name="List Creation",
                description="Different ways to create lists",
                code="""
# Empty list
empty_list = []
print(empty_list)

# List with initial values
numbers = [1, 2, 3, 4, 5]
print(numbers)

# List with mixed data types
mixed = [1, "Hello", 3.14, True]
print(mixed)

# List using the list() constructor
chars = list("Python")
print(chars)

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)
""",
                output="""
[]
[1, 2, 3, 4, 5]
[1, 'Hello', 3.14, True]
['P', 'y', 't', 'h', 'o', 'n']
[1, 4, 9, 16, 25]
"""
            ),
            DataStructureExample(
                name="List Manipulation",
                description="Common operations for modifying lists",
                code="""
numbers = [1, 2, 3, 4, 5]

# Append an item
numbers.append(6)
print(numbers)

# Insert at position
numbers.insert(0, 0)  # Insert 0 at beginning
print(numbers)

# Extend with another list
numbers.extend([7, 8, 9])
print(numbers)

# Remove by value
numbers.remove(0)  # Remove the first occurrence of 0
print(numbers)

# Remove by position
popped = numbers.pop(1)  # Remove item at index 1
print(f"Popped: {popped}, New list: {numbers}")

# Clear the list
numbers.clear()
print(numbers)
""",
                output="""
[1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Popped: 2, New list: [1, 3, 4, 5, 6, 7, 8, 9]
[]
"""
            ),
            DataStructureExample(
                name="List Operations",
                description="Other common list operations",
                code="""
fruits = ['apple', 'orange', 'banana', 'kiwi', 'mango']
print(f"Original list: {fruits}")

# Finding the length
print(f"Number of fruits: {len(fruits)}")

# Checking membership
print(f"Is 'apple' in the list? {'apple' in fruits}")
print(f"Is 'grape' in the list? {'grape' in fruits}")

# Index of an item
print(f"Index of 'banana': {fruits.index('banana')}")

# Count occurrences
fruits.append('apple')
print(f"Updated list: {fruits}")
print(f"Count of 'apple': {fruits.count('apple')}")

# Sort the list (in-place)
fruits.sort()
print(f"Sorted alphabetically: {fruits}")

# Reverse the list (in-place)
fruits.reverse()
print(f"Reversed: {fruits}")

# Copy a list
copy_of_fruits = fruits.copy()
print(f"Copy: {copy_of_fruits}")
""",
                output="""
Original list: ['apple', 'orange', 'banana', 'kiwi', 'mango']
Number of fruits: 5
Is 'apple' in the list? True
Is 'grape' in the list? False
Index of 'banana': 2
Updated list: ['apple', 'orange', 'banana', 'kiwi', 'mango', 'apple']
Count of 'apple': 2
Sorted alphabetically: ['apple', 'apple', 'banana', 'kiwi', 'mango', 'orange']
Reversed: ['orange', 'mango', 'kiwi', 'banana', 'apple', 'apple']
Copy: ['orange', 'mango', 'kiwi', 'banana', 'apple', 'apple']
"""
            ),
            DataStructureExample(
                name="List Slicing",
                description="Accessing parts of lists with slices",
                code="""
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:stop]
print(f"First three: {numbers[0:3]}")
print(f"Middle three: {numbers[3:6]}")
print(f"Last three: {numbers[-3:]}")

# Slicing with step [start:stop:step]
print(f"Every second item: {numbers[::2]}")
print(f"Every third item: {numbers[::3]}")

# Reverse with slicing
print(f"Reversed list: {numbers[::-1]}")

# Negative stepping
print(f"Every second item from the end: {numbers[::-2]}")

# Creating a copy with slicing
copy_of_numbers = numbers[:]
print(f"Copy with slicing: {copy_of_numbers}")
""",
                output="""
First three: [0, 1, 2]
Middle three: [3, 4, 5]
Last three: [7, 8, 9]
Every second item: [0, 2, 4, 6, 8]
Every third item: [0, 3, 6, 9]
Reversed list: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Every second item from the end: [9, 7, 5, 3, 1]
Copy with slicing: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
            )
        ]
    )

@router.get("/data-structures/dictionaries", response_model=DataStructureResponse)
async def dictionaries_examples():
    """Provides detailed examples of Python dictionaries."""
    return DataStructureResponse(
        description="Dictionaries in Python",
        examples=[
            DataStructureExample(
                name="Dictionary Creation",
                description="Different ways to create dictionaries",
                code="""
# Empty dictionary
empty_dict = {}
print(empty_dict)

# Dictionary with initial key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="Boston")
print(person2)

# Creating from sequence of key-value pairs
items = [("name", "Charlie"), ("age", 35), ("city", "Chicago")]
person3 = dict(items)
print(person3)

# Dictionary comprehension
squares = {x: x**2 for x in range(6)}
print(squares)
""",
                output="""
{}
{'name': 'Alice', 'age': 25, 'city': 'New York'}
{'name': 'Bob', 'age': 30, 'city': 'Boston'}
{'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
            ),
            DataStructureExample(
                name="Dictionary Access and Manipulation",
                description="Accessing and modifying dictionaries",
                code="""
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values by key
print(f"Name: {person['name']}")

# Using get method (safer, provides a default value)
print(f"State: {person.get('state', 'Unknown')}")

# Modifying values
person['age'] = 26
print(person)

# Adding new key-value pairs
person['email'] = 'alice@example.com'
print(person)

# Removing items
removed_age = person.pop('age')
print(f"Removed age: {removed_age}")
print(person)

# Remove and return an arbitrary item
item = person.popitem()
print(f"Popped item: {item}")
print(person)

# Clear the dictionary
person.clear()
print(person)
""",
                output="""
Name: Alice
State: Unknown
{'name': 'Alice', 'age': 26, 'city': 'New York'}
{'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
Removed age: 26
{'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}
Popped item: ('email', 'alice@example.com')
{'name': 'Alice', 'city': 'New York'}
{}
"""
            ),
            DataStructureExample(
                name="Dictionary Methods",
                description="Useful dictionary methods and operations",
                code="""
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Get all keys
print(f"Keys: {list(person.keys())}")

# Get all values
print(f"Values: {list(person.values())}")

# Get all key-value pairs as tuples
print(f"Items: {list(person.items())}")

# Check if a key exists
print(f"Has 'name'? {'name' in person}")
print(f"Has 'email'? {'email' in person}")

# Update with another dictionary
person.update({"email": "alice@example.com", "state": "NY"})
print(person)

# Using setdefault to add a key if it doesn't exist
phone = person.setdefault("phone", "555-1234")
print(f"Phone: {phone}")
print(person)
""",
                output="""
Keys: ['name', 'age', 'city']
Values: ['Alice', 25, 'New York']
Items: [('name', 'Alice'), ('age', 25), ('city', 'New York')]
Has 'name'? True
Has 'email'? False
{'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com', 'state': 'NY'}
Phone: 555-1234
{'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com', 'state': 'NY', 'phone': '555-1234'}
"""
            ),
            DataStructureExample(
                name="Nested Dictionaries",
                description="Working with nested dictionaries",
                code="""
# Nested dictionary - a dictionary of dictionaries
users = {
    "alice": {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "age": 25,
        "active": True
    },
    "bob": {
        "name": "Bob Johnson",
        "email": "bob@example.com",
        "age": 30,
        "active": False
    }
}

# Accessing nested values
print(f"Alice's email: {users['alice']['email']}")

# Adding a new nested dictionary
users["charlie"] = {
    "name": "Charlie Brown",
    "email": "charlie@example.com",
    "age": 22,
    "active": True
}

# Modifying a nested value
users["bob"]["active"] = True
print(f"Bob's status: {'Active' if users['bob']['active'] else 'Inactive'}")

# Iterating through nested dictionaries
for username, user_info in users.items():
    print(f"User: {username}")
    for key, value in user_info.items():
        print(f"  {key}: {value}")
    print()
""",
                output="""
Alice's email: alice@example.com
Bob's status: Active
User: alice
  name: Alice Smith
  email: alice@example.com
  age: 25
  active: True

User: bob
  name: Bob Johnson
  email: bob@example.com
  age: 30
  active: True

User: charlie
  name: Charlie Brown
  email: charlie@example.com
  age: 22
  active: True
"""
            )
        ]
    )

@router.get("/data-structures/sets", response_model=DataStructureResponse)
async def sets_examples():
    """Provides detailed examples of Python sets."""
    return DataStructureResponse(
        description="Sets in Python",
        examples=[
            DataStructureExample(
                name="Set Creation",
                description="Different ways to create sets",
                code="""
# Empty set (Note: {} creates an empty dict, not an empty set)
empty_set = set()
print(empty_set)

# Set with initial values (duplicates are automatically removed)
colors = {"red", "green", "blue", "red"}
print(colors)

# Using the set() constructor
vowels = set("aeiou")
print(vowels)

# Set from a list
numbers = set([1, 2, 2, 3, 4, 4, 5])
print(numbers)

# Set comprehension
even_numbers = {x for x in range(10) if x % 2 == 0}
print(even_numbers)
""",
                output="""
set()
{'red', 'green', 'blue'}
{'a', 'e', 'i', 'o', 'u'}
{1, 2, 3, 4, 5}
{0, 2, 4, 6, 8}
"""
            ),
            DataStructureExample(
                name="Set Manipulation",
                description="Adding and removing elements from sets",
                code="""
fruits = {"apple", "banana", "cherry"}
print(f"Original set: {fruits}")

# Add a single element
fruits.add("orange")
print(f"After adding 'orange': {fruits}")

# Try adding a duplicate element
fruits.add("apple")  # No effect as apple already exists
print(f"After trying to add 'apple' again: {fruits}")

# Add multiple elements
fruits.update(["mango", "grapes"])
print(f"After updating: {fruits}")

# Remove an element (raises KeyError if not found)
fruits.remove("banana")
print(f"After removing 'banana': {fruits}")

# Discard an element (no error if not found)
fruits.discard("kiwi")  # No error even though kiwi isn't in the set
print(f"After discarding 'kiwi': {fruits}")

# Pop a random element
popped = fruits.pop()
print(f"Popped element: {popped}")
print(f"Set after pop: {fruits}")

# Clear the set
fruits.clear()
print(f"After clearing: {fruits}")
""",
                output="""
Original set: {'apple', 'banana', 'cherry'}
After adding 'orange': {'apple', 'banana', 'cherry', 'orange'}
After trying to add 'apple' again: {'apple', 'banana', 'cherry', 'orange'}
After updating: {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}
After removing 'banana': {'apple', 'cherry', 'orange', 'mango', 'grapes'}
After discarding 'kiwi': {'apple', 'cherry', 'orange', 'mango', 'grapes'}
Popped element: apple
Set after pop: {'cherry', 'orange', 'mango', 'grapes'}
After clearing: set()
"""
            ),
            DataStructureExample(
                name="Set Operations",
                description="Mathematical set operations",
                code="""
# Define some sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")

# Union (elements in either set)
print(f"Union (A | B): {A | B}")
print(f"Union using method: {A.union(B)}")

# Intersection (elements in both sets)
print(f"Intersection (A & B): {A & B}")
print(f"Intersection using method: {A.intersection(B)}")

# Difference (elements in A but not in B)
print(f"Difference (A - B): {A - B}")
print(f"Difference using method: {A.difference(B)}")

# Symmetric Difference (elements in either set, but not both)
print(f"Symmetric Difference (A ^ B): {A ^ B}")
print(f"Symmetric Difference using method: {A.symmetric_difference(B)}")

# Subset and Superset
C = {1, 2}
print(f"C = {C}")
print(f"Is C a subset of A? {C.issubset(A)}")
print(f"Is A a superset of C? {A.issuperset(C)}")

# Disjoint sets (no common elements)
D = {10, 11, 12}
print(f"D = {D}")
print(f"Are A and D disjoint? {A.isdisjoint(D)}")
print(f"Are A and B disjoint? {A.isdisjoint(B)}")
""",
                output="""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
Union (A | B): {1, 2, 3, 4, 5, 6, 7, 8}
Union using method: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection (A & B): {4, 5}
Intersection using method: {4, 5}
Difference (A - B): {1, 2, 3}
Difference using method: {1, 2, 3}
Symmetric Difference (A ^ B): {1, 2, 3, 6, 7, 8}
Symmetric Difference using method: {1, 2, 3, 6, 7, 8}
C = {1, 2}
Is C a subset of A? True
Is A a superset of C? True
D = {10, 11, 12}
Are A and D disjoint? True
Are A and B disjoint? False
"""
            ),
            DataStructureExample(
                name="Set Comprehensions",
                description="Creating sets with comprehensions",
                code="""
# Base data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}")

# Set of squares
squares = {x**2 for x in numbers}
print(f"Squares: {squares}")

# Set of even numbers
even = {x for x in numbers if x % 2 == 0}
print(f"Even numbers: {even}")

# Set of characters from a string
word = "mississippi"
unique_chars = {char for char in word}
print(f"Unique characters in '{word}': {unique_chars}")

# Set with transformation
words = ["hello", "world", "python", "programming"]
word_lengths = {word: len(word) for word in words}  # This creates a dictionary
print(f"Word lengths: {word_lengths}")
""",
                output="""
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Squares: {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
Even numbers: {2, 4, 6, 8, 10}
Unique characters in 'mississippi': {'m', 'i', 's', 'p'}
Word lengths: {'hello': 5, 'world': 5, 'python': 6, 'programming': 11}
"""
            )
        ]
    )