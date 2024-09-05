Object Types/Data Types:

-Number     : 1234, 3.1415, 3+4j, 0b111, Decimal(), fraction()
-String     : 'spam', "Bob's",b'a\x01c',u'sp\xc4m'
-List       : [1, [2,'three'], 4.5] list(range(10))
-Tuple      :  (1, 'spam', 4, u), tuple('spam'), namedtuple
-Dictionary : {'food':'spam', 'taste':'yum'}, dict(hours=10)
-Set        : set('abc'), {a,b,c}
-File       : open('eggs.txt'),open(r'C:\ham.bin','wb')
-Boolean    :true,false
-None       :None

-Functions, modules, classes
-Advanced   :Decorators, Genatators, Iterators, MetaProgramming

 
//power shell
1. Open the Integrated Terminal in VS Code
Launch VS Code.
Open the integrated terminal by navigating to the top menu and selecting Terminal > New Terminal, or use the keyboard shortcut:
Ctrl + (backtick) on Windows/Linux.
2.
To start PowerShell in Visual Studio Code (VS Code) and use it to run a Python shell, follow these steps:

1. Open the Integrated Terminal in VS Code
Launch VS Code.
Open the integrated terminal by navigating to the top menu and selecting Terminal > New Terminal, or use the keyboard shortcut:
Ctrl + (backtick) on Windows/Linux.
Cmd + (backtick) on macOS.
2. Ensure PowerShell is the Active Terminal
If PowerShell is not already active:

Click on the dropdown arrow next to the + icon in the terminal tab.
Select PowerShell from the list of available terminals.
If PowerShell isn’t listed, you can manually set it as the default shell:

Open the Command Palette with Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (macOS).
Type Terminal: Select Default Profile and choose PowerShell from the options.
3. Start the Python Shell
With the PowerShell terminal open, you can start the Python shell by typing python and pressing Enter.
This will initiate the Python interactive shell, where you can execute Python commands directly.

//Methods in python
length-len()
username="Abhilash"
len(username)->8
username[0]
'A'
username[-1]
'h'
username[1:3]
'bh'
dir(username)
-List:
> mylist=[123,"Abhi",3.14]
>>> mylist
[123, 'Abhi', 3.14]
>>> len(mylist)--3
myDic={'one':'lemon', 'two':'ginger','comic':'nagaraaj'}
>>> myDic['one']
'lemon'
>>> myDic['comic']
'nagaraaj'
Tuple:
 myTup=(1,2,3,4)
>>> myTup[1]
2
>>> myTup[-1]
4
len(myTup)
4
getrefcount():
import sys
sys.getrefcount(24601)
3
sys.getrefcount('hitesh')
4294967295
sys.getrefcount('h')
4294967295
>>> sys.getrefcount(1)
4294967295

 myListOne=[1,2,3]   
>>> myListTwo=myListOne
>>> myListOne
[1, 2, 3]
>>> myListTwo
[1, 2, 3]
>>> myListOne[0]=33
>>> myListOne
[33, 2, 3]
>>> myListTwo
[1, 2, 3]
mutable:
l1=[1,2,3]
>>> l2=l1
>>> l1->[1, 2, 3]
>>> l2->[1, 2, 3]

//immutable
p1=[1,2,3]
>>> p2=p1
>>> p1->[1, 2, 3]
>>> p2->[1, 2, 3]
>>> p2=[1,2,3]
>>> p1[0]=55 
>>> p1->[55, 2, 3]
>>> p2->[1, 2, 3]
slicing--copying
h1=[1,2,3]
>>> h2=h1[:]
>>> h1->[1, 2, 3]
>>> h2->[1, 2, 3]
>>> h1[0]=55
>>> h1->[55, 2, 3]
>>> h2->[1, 2, 3]

import copy
>>> h2=copy.copy(h1)

 h2=copy.deepcopy(h1)
>>> h2->[55, 2, 3]

1=[1,2,3]
>>> c2=copy.copy(c1)
>>> c2->[1, 2, 3]
>>> c1[0]=11
>>> c2 ->[1, 2, 3]
>>> c1->[11, 2, 3]
c2=copy.deepcopy(c1)
>>> c2->[11, 2, 3]

n=[1,2,3]
>>> m=n
>>> n->[1, 2, 3]
>>> m->[1, 2, 3]
>>> m==n->True
>>> m is n ->True
>>> m=[1,2,3]
>>> m==n->True
>>> m is n->False

operation preciding:
x=2   y=3     z=4
>>> x+y->5
>>> x+y+z->9
>>> x+y*z->14
>>> (x+y)*z->20
>>> x+(y*z)->14

int(2.23)->2
float(2)->2.0

Oprator overloading:
1. 'chai'+ 'code'->'chaicode'
2.'jai'+ 'hind'->'jaihind'

Tuple:
>>> x,y,z->(2, 3, 4)
>>> x+1,y*2->(3, 6)
>>> y%2->1
>>> z**2->16
>>> z**5->1024
>>> 100**2->10000
>>> 2**100->1267650600228229401496703205376
result=1/3
>>> result->0.3333333333333333

 repr('chai')->"'chai'"
 str('chai') ->'chai'
print('chai')->chai

Conditional operators:
----------------------
>>> 1<2->True
>>> 5.0==5.0->True
>>> 4.5!=5.5->True

Logical Operators:
------------------
 x,y,z
(2, 3, 4)
//AND Operator
>>> x<y<z->True  Same x<y and y<z->True
>>> x<y and y<z->True
 1==2<3->False Same 1==2 and 2>3->False

 Math:Floor->It gives Bottom values
  import math
>>> math.floor(3.5)->3
>>> math.floor(-3.5)->-4
>>> math.floor(3.9)->3

 Math:trunc->It gives value towards Zero (0)
 >>> math.trunc(2.3)->2
>>> math.trunc(-2.3)->-2

 complex numbers in Python:
 -------------------------
 2 + 1j is a complex number in Python. In Python, j is used to denote the imaginary unit (the square root of -1). So 2 + 1j represents a complex number with a real part of 2 and an imaginary part of 1.

 2+1j->(2+1j)
>>> (2+1j)*3->(6+3j)
->When you multiply (2 + 1j) * 3, Python multiplies both the real and imaginary parts of the complex number by 3:

Real part: 2 * 3 = 6
Imaginary part: 1 * 3 = 3
So, the result is (6 + 3j).

1.Octal     : 0o20->16
              oct(64)->'0o100'
2.Hexadecimal: 0xFF->255
               hex(64)->'0x40'
3.binary    : 0b1000->8
              bin(64)->'0b1000000'
-------------------------------------------------------------              
              int() function in Python
        ---------------------------------
1. Converting an Integer Directly              
int(64)->64
2.Converting a String to an Integer with a Base of 8
>>> int('64',8)
52
The octal number 64
(6×8^1+4×8^0) is equivalent to the decimal number 52.
3.Converting a String to an Integer with a Base of 16
>>> int('64',16)
100
6×16^1+16×8^0--is equivalent to the decimal number 100.
4.Converting a Binary String to an Integer
>>> int('10000',2)
16
The binary number 10000 (which is 
1×2^4+0×2^3+0×2^2+0×2^1+0×2^0=1×2^4+0×2^3+0×2^2+0×2^1+0×2^0 ) is equivalent to the decimal number 16.

Bitwise Operators:
x=1
x<<2
4

import random
>>> random.random()
0.22641757232592996
>>> random.randint(1,100)
66
>>> random.randint(1,100)
64

l1=['lemon','masala','ginger','mint']
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'mint'

random.shuffle(l1)
>>> l1-> ['masala', 'ginger', 'mint', 'lemon']

0.1+0.1+0.1-0.3 ->5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-->Decimal('0.3')  
Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3') -->Decimal('0.0')

>>> from fractions  import Fraction      
>>> myFra=Fraction(2,7)
>>> myFra
Fraction(2, 7)

setone={1,2,3,4}
>>> setone & {1,3}
{1, 3}
>>> setone | {1,3,7}
{1, 2, 3, 4, 7}
>>> setone
{1, 2, 3, 4}
>>> setone-{1,2,3,4}
set()
>>> setone-{1,2,3,4}
set()
>>>
>>> type({})    
<class 'dict'>
>>> type(True)
<class 'bool'>
>>> True==1
True
>>> False==0
True
>>>True+1->2

String:
    In Python, a string is a sequence of characters enclosed within single quotes ('...'), double quotes ("..."), or triple quotes ('''...''' or """..."""). Strings are one of the most commonly used data types and are immutable, meaning once a string is created, it cannot be modified.  
    String Definitions
Single-quoted string:
single_quoted = 'Hello, World!'

Double-quoted string:
double_quoted = "Hello, World!"

Triple-quoted string (used for multi-line strings):
multi_line_string = """This is a string
that spans multiple
lines."""


chai="masala chai"
>>> first_char=chai[0]
>>> print(first_char)

slice_chai=chai[0:6]
>>> print(slice_chai)=>masala
>>>chai[-1]->'i'

num_list="0123456789"
>>> num_list[:]->'0123456789'
>>> num_list[3:]->'3456789'
>>> num_list[:7]->'0123456'
>>> num_list[0:7:2]->'0246'
>>> num_list[0:7:3]->'036'

chai="masala chai"
>>> print(chai.lower())->masala chai
>>> print(chai.upper())->MASALA CHAI
>>> chai->'masala chai'---strings are immutable

 chai=" Masala chai  "
>>> chai->' Masala chai  '
>>> print(chai.strip())->Masala chai--Remove spaces

>>> chai="Lemon Chai"
>>> print(chai.replace("Lemon","Ginger")) ->Ginger Chai

>>> chai="Lemon, Ginger, Masala, Mint" 
>>> print(chai.split())->['Lemon,', 'Ginger,', 'Masala,',Mint']
>>> print(chai.split(", "))->['Lemon', 'Ginger', 'Masala', 'Mint']

chai="Masala Chai"
>>> print(chai.find("Chai"))-->7

 chai="Masala Chai Chai Chai"
>>> print(chai.count("Chai"))->3

chai_type="Masala"
>>> quantity=2
>>> order="I ordered {} cups of {} chai"
 order->'I ordered {} cups of {} chai'
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai

chai_variety=["Lemon", "Masala", "Ginger"]
>>> chai_variety->['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))->LemonMasalaGinger
>>> print(" ".join(chai_variety))->Lemon Masala Ginger
>>> print("-".join(chai_variety))->Lemon-Masala-Ginger
>>> print(", ".join(chai_variety))->Lemon, Masala, Ginger

>>> chai="Masala Chai"
>>> chai->'Masala Chai'
>>> print(len(chai))->11

Enhanced for loop:
>>> for letter in chai:
print(letter)->M a s a l a   C h a i

chai="He said, \"Masala chai is awesome\" "
>>> chai->'He said, "Masala chai is awesome" '

>>> chai="Masala\nChai"
>>> chai->'Masala\nChai'
>>> print(chai)
Masala
Chai

>>> chai=r"Masala\nchai"
>>> chai->'Masala\\nchai'

>>> chai=r"c:\\user\\pwd\\"
>>> print(chai)->c:\\user\\pwd\\

>>> chai=r"c:user\name"
>>> print(chai)->c:user\name

>>> chai="c:\\user\\pwd"
>>> chai->'c:\\user\\pwd'
>>> print(chai)->c:\user\pwd

>>> chai="Masala Chai"
>>> print("Masala" in chai)->True
>>> print("Masalaa" in chai) ->False

 List:
  Python, a list is a versatile and commonly used data structure that can store a collection of items. Lists are ordered, mutable (i.e., you can change their content), and can contain elements of different data types, including other lists.
  
  Creating a List:
   Lists are created by placing elements inside square brackets [], separated by commas:
   # An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list with mixed data types
mixed_list = [1, "hello", 3.14, True]

# A nested list (a list within a list)
nested_list = [[1, 2], [3, 4], [5, 6]]

Accessing List Elements:  
You can access elements in a list by their index. Python uses zero-based indexing, meaning the first element is at index 0.
  fruits = ["apple", "banana", "cherry"]

# Accessing the first element
print(fruits[0])  # Output: apple

# Accessing the last element
print(fruits[-1])  # Output: cherry

# Accessing elements in a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1][0])  # Output: 3

In Python, a list is a versatile and commonly used data structure that can store a collection of items. Lists are ordered, mutable (i.e., you can change their content), and can contain elements of different data types, including other lists.

Creating a List
Lists are created by placing elements inside square brackets [], separated by commas:

python
Copy code
# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list with mixed data types
mixed_list = [1, "hello", 3.14, True]

# A nested list (a list within a list)
nested_list = [[1, 2], [3, 4], [5, 6]]
Accessing List Elements
You can access elements in a list by their index. Python uses zero-based indexing, meaning the first element is at index 0.

python
Copy code
fruits = ["apple", "banana", "cherry"]

# Accessing the first element
print(fruits[0])  # Output: apple

# Accessing the last element
print(fruits[-1])  # Output: cherry

# Accessing elements in a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1][0])  # Output: 3
Modifying Lists
Since lists are mutable, you can change, add, or remove elements after the list has been created.

1. Changing Elements:
You can modify an element by assigning a new value to a specific index.
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
2. Adding Elements
  1.append(): Adds an element to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
  2.insert(index, element): Inserts an element at a specified index.
  fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
3.extend(iterable): Adds elements from another list (or any iterable) to the end of the current list.
fruits = ["apple", "banana"]
more_fruits = ["cherry", "date"]
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
3. Removing Elements
remove(element): Removes the first occurrence of the specified element.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']

pop(index): Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.

fruits = ["apple", "banana", "cherry"]
fruit = fruits.pop(1)
print(fruit)  # Output: banana
print(fruits)  # Output: ['apple', 'cherry']

clear(): Removes all elements from the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []

List Methods
Python provides many built-in methods for working with lists. Here are some of the most commonly used ones:

1. len()
Returns the number of elements in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3
2. sort()
Sorts the elements of the list in ascending order.
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

You can sort in descending order by passing reverse=True.
numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]

3. reverse()
Reverses the order of the elements in the list.
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # Output: [4, 3, 2, 1]

4. index(element)
Returns the index of the first occurrence of the specified element.
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1
5. count(element)
Returns the number of occurrences of the specified element in the list.
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))  # Output: 2
6. copy()
Returns a shallow copy of the list.
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits)  # Output: ['apple', 'banana', 'cherry']

List Comprehensions
List comprehensions provide a concise way to create lists. They are commonly used to apply an expression to each element in a sequence.
 # Example: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

List comprehensions can also include conditions:
# Example: Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

slicing Lists
You can retrieve a portion of a list (a slice) using the slicing syntax:
fruits = ["apple", "banana", "cherry", "date"]

# Get the first two elements
print(fruits[:2])  # Output: ['apple', 'banana']

# Get the last two elements
print(fruits[-2:])  # Output: ['cherry', 'date']

# Get every other element
print(fruits[::2])  # Output: ['apple', 'cherry']
Nesting Lists
Lists can contain other lists as elements, creating nested lists:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing an element in a nested list
print(nested_list[1][2])  # Output: 6

Example: Basic List Operations:
# Create a list of favorite fruits
favorite_fruits = ["apple", "banana", "cherry"]

# Add a new fruit
favorite_fruits.append("date")

# Insert a fruit at the beginning
favorite_fruits.insert(0, "elderberry")

# Remove a fruit
favorite_fruits.remove("banana")

# Sort the list
favorite_fruits.sort()

# Print the final list
print(favorite_fruits)  # Output: ['apple', 'cherry', 'date', 'elderberry']

 --------------------------------------------------------------------------------
Practice:
--------
>>> tea_varities=["Black", "Green", "Oolong", "White"]
>>> tea_varities->['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities)->['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0])->Black
>>> print(tea_varities[-1])->White
>>> print(tea_varities[1:3])->['Green', 'Oolong']
>>> print(tea_varities[:2])->['Black', 'Green']
>>> print(tea_varities[2:])->['Oolong', 'White']
>>> tea_varities[3]="Herbal"
>>> print(tea_varities)->['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varities[1:2]="Lemon"--Not Approach this 
>>> tea_varities->['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']

>>> tea_varities->['Black', 'Green', 'Oolong', 'White']
>>> tea_varities[1:2]->['Green']
>>> tea_varities[1:2]=["Lemon"]
>>> tea_varities->['Black', 'Lemon', 'Oolong', 'White'] 
>>> tea_varities[1:3]->['Lemon', 'Oolong']
>>> tea_varities[1:3]=["Green", "Masala"]
>>> tea_varities->['Black', 'Green', 'Masala', 'White']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1]=["test", "test"]
>>> tea_varities->['Black', 'test', 'test', 'Green', 'Masala', 'White']
>>> tea_varities[1:2]->['test']
>>> tea_varities[1:3]->['test', 'test']
>>> tea_varities[1:3]= []
>>> tea_varities->['Black', 'Green', 'Masala', 'White']

>>> for tea in tea_varities:
...  print(tea)
...
Black
Green
Masala
White
>>> for tea in tea_varities:
...  print(tea, end="=")
...
Black=Green=Masala=White=>>>

>>> tea_varities.append("Oolong")
>>> tea_varities
['Black', 'Green', 'Masala', 'White', 'Oolong']

>>> if "Oolong" in tea_varities:             
...  print("I have Oolong tea")
...
I have Oolong tea

>>> tea_varities->['Black', 'Green', 'Masala', 'White', 'Oolong']
>>> tea_varities.pop()->'Oolong'
>>> tea_varities->['Black', 'Green', 'Masala', 'White']
>>> tea_varities.remove("Green")
>>> tea_varities->['Black', 'Masala', 'White']
>> tea_varities.insert(1,"Green")
>>> tea_varities->['Black', 'Green', 'Masala', 'White']

>>> tea_varities_copy=tea_varities.copy()
>>> tea_varities_copy->['Black', 'Green', 'Masala', 'White']
>>> tea_varities_copy.append("Lemon")
>>> tea_varities_copy->['Black', 'Green', 'Masala', 'White', 'Lemon']
>>> tea_varities->['Black', 'Green', 'Masala', 'White']

List comprehention

range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y=range(10)
>>> y
range(0, 10)
>>> squared_num=[x**2 for x in range(10)]
>>> squared_num->[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cub_num=[y**3 for y in range(5)]
>>> cub_num->[0, 1, 8, 27, 64]



Dictionary:
In Python, a dictionary is a collection of key-value pairs. Each key in a dictionary is unique and maps to a corresponding value. Dictionaries are unordered (prior to Python 3.7, where they became insertion-ordered), mutable, and indexed by keys.
---------------------------------------------------------------------------------

# An empty dictionary
empty_dict = {}

# A dictionary with some key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
Adding and Updating Entries:
# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating an existing key
person["age"] = 31

print(person)
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}
Removing Entries:
# Using del to remove a key-value pair
del person["city"]

# Using pop() to remove a key and return its value
email = person.pop("email")

print(person)  # Output: {'name': 'Alice', 'age': 31}
print(email)   # Output: 'alice@example.com'

Dictionary Methods:
1. dict.keys()
Returns a view object containing the dictionary’s keys.
print(person.keys())  # Output: dict_keys(['name', 'age'])
2. dict.values()
Returns a view object containing the dictionary’s values.
print(person.values())  # Output: dict_values(['Alice', 31])
3. dict.items()
Returns a view object containing the dictionary’s key-value pairs as tuples.
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 31)])
4. dict.get(key, default=None)
Returns the value for the specified key if the key is in the dictionary; otherwise, it returns the default value (which is None if not provided).
print(person.get("name"))    # Output: Alice
print(person.get("address")) # Output: None
5. dict.update(other_dict)
Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
additional_info = {"city": "Los Angeles", "phone": "123-456-7890"}
person.update(additional_info)
print(person)
# Output: {'name': 'Alice', 'age': 31, 'city': 'Los Angeles', 'phone': '123-456-7890'}
6. dict.clear()
Removes all key-value pairs from the dictionary.
person.clear()
print(person)  # Output: {}

Iterating Through a Dictionary:
You can iterate through the keys, values, or items (key-value pairs) in a dictionary:
# Iterating through keys
for key in person.keys():
    print(key)

# Iterating through values
for value in person.values():
    print(value)

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

Dictionary Comprehensions
Like list comprehensions, you can create dictionaries using dictionary comprehensions:
# Example: Squaring numbers
squares = {x: x**2 for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Nested Dictionaries
Dictionaries can contain other dictionaries as values, creating a nested structure:
students = {
    "Alice": {"age": 30, "city": "New York"},
    "Bob": {"age": 25, "city": "Los Angeles"}
}

print(students["Alice"]["city"])  # Output: New York

Practice:
---------

>>> chai_types->{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]->'Spicy'
>>> chai_types.get("Ginger")->'Zesty'
>>> chai_types.get("Gingery")
>>> chai_types.get["Masalaa"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable

>>> chai_types->{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"]="Fresh"
>>> chai_types->{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

>>> for chai in chai_types:
...  print(chai, chai_types[chai])     
... 
Masala Spicy
Ginger Zesty
Green Fresh

>>> for key, value in chai_types.items():
...  print(key, value)
...
Masala Spicy
Ginger Zesty
Green Fresh

>>> if "Masala" in chai_types:
...  print("I have Masala chai")
...
I have Masala chai

>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> print(len(chai_types))
3

>>> chai_types["Earl Grey"]="citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'citrus'}

>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'citrus'}

>> chai_types.popitem()
('Earl Grey', 'citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}

>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}

//Reference was be copied
>>> chai_types_copy=chai_types.copy()
>>> chai_types_copy
{'Masala': 'Spicy'}
>>> chai_types
{'Masala': 'Spicy'}

>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
KeyError: 'Green'
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> squared_num={x:x**2 for x in range(10)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> squared_num.clear()
>>> squared_num
{}

>>> keys=["Masala", "Ginger", "Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value="Delicious"
>>> new_dict=dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict=dict.fromkeys(keys, keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}

Tuple:
 In Python, a tuple is an immutable sequence type, meaning that once a tuple is created, its elements cannot be changed, added, or removed. Tuples are often used to group related data together and are similar to lists, but with the key difference of immutability.

 Creating a Tuple
Tuples are created by placing elements inside parentheses () separated by commas:
# An empty tuple
empty_tuple = ()

# A tuple with some elements
t = (1, 2, 3)

# A tuple with mixed data types
mixed_tuple = (1, "hello", 3.14)

# A nested tuple
nested_tuple = ((1, 2), (3, 4))

# A tuple without parentheses (optional)
t = 1, 2, 3
Single Element Tuples
When creating a tuple with a single element, you need to include a comma after the element; otherwise, Python will not recognize it as a tuple.

single_element_tuple = (5,)
not_a_tuple = (5)  # This is just an integer, not a tuple

print(type(single_element_tuple))  # Output: <class 'tuple'>
print(type(not_a_tuple))           # Output: <class 'int'>

Accessing Tuple Elements
Like lists, tuple elements can be accessed using indexing:
t = (1, 2, 3, 4)

# Accessing the first element
print(t[0])  # Output: 1

# Accessing the last element
print(t[-1])  # Output: 4

# Accessing elements in a nested tuple
nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1][1])  # Output: 3
 
 Tuple Operations
Tuples support various operations similar to lists:

1. Concatenation
You can concatenate two or more tuples using the + operator.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 6)

2. Repetition
You can repeat a tuple a given number of times using the * operator.
t = (1, 2, 3)
t_repeated = t * 3
print(t_repeated)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

3. Slicing
You can slice a tuple to access a subset of its elements.
t = (1, 2, 3, 4, 5)
print(t[1:4])  # Output: (2, 3, 4)

Tuple Methods
Since tuples are immutable, they have fewer methods compared to lists. The two main methods for tuples are:

1. count()
Returns the number of times a specified value appears in the tuple.
t = (1, 2, 3, 1, 1, 4)
print(t.count(1))  # Output: 3
2. index()
Returns the index of the first occurrence of a specified value.
t = (1, 2, 3, 4)
print(t.index(3))  # Output: 2

Tuple Unpacking
Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single statement:
t = (1, 2, 3)
a, b, c = t

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
You can also use the unpacking syntax to skip certain values:
t = (1, 2, 3, 4)
a, _, c, _ = t

print(a)  # Output: 1
print(c)  # Output: 3

Immutable Nature of Tuples
One of the main characteristics of tuples is that they are immutable. This means you cannot change the elements of a tuple after it is created:
t = (1, 2, 3)
# t[0] = 10  # This would raise a TypeError
However, if a tuple contains a mutable object (like a list), the mutable object can be modified:
t = (1, 2, [3, 4])
t[2][0] = 10
print(t)  # Output: (1, 2, [10, 4])

When to Use Tuples vs Lists
Tuples are used when you want to ensure that the data remains unchanged throughout the program. They are also more memory-efficient compared to lists.
Lists are preferred when you need a mutable sequence that can be modified during the program's execution.

>>> tea_types=("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0] 
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1]="Lemon"
TypeError: 'tuple' object does not support item assignment

>>> len(tea_types)
3
>>> tea_types
('Black', 'Green', 'Oolong')
>>> more_tea=("Herbal", "Erly grey")
>>> all_tea = tea_types + more_tea
>>> all_tea-> ('Black', 'Green', 'Oolong', 'Herbal', 'Erly grey')
>>> if "Green" in all_tea:
...  print("I have Green tea")
...
I have Green tea
>>> more_tea = ("Herbal", "Earl Grey", "Herbal")
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("Herb")
0
Unpacking of tuple:
-------------------
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, oolong) = tea_types
>>> black
'Black'
>>> green
'Green'
>>> oolong
'Oolong'


Questions on conditionals:
--------------------------
1.Age Group Categorization
Classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+).

age=25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age  < 60:
    print("Adult")
else:
    print("Senior")

2.Movie Ticket Pricing
problem: movie tickets are priced based on age:$12 for adults (18 and over),
$8 for children. Everyone gets a $2 discount on wednesday.

age=22
day="wednesday"
price=12 if age>=18 else 8
if day=="wednesday":
    price-=2
print("Ticket price for you is $",price)
 

3.Grade Calculator
 Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79),
 D(60-69),F(below 60)

 ANS:
   score=199
if score >=101:
    print("please verify your grade again")
    exit()
if score >= 90:
    grade="A"
elif score >=80:
    grade="B"
elif score >=70:
    grade="C"
elif score <=60:
    grade="D"
else :
    grade="F"
print("Grade:",grade)


4.Fruit Ripeness Ckecker
    Problem:
      Determine if a fruit is ripe,overripe or unripe based on its color. 
      (e.g:Banana: Green-Unripe, Yellow-Ripe, Brown-Overripe)
    Ans:
      fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    else :
        print("OverRipe")


5.Weather activity suggestion
   Suggest an activity based on the weather 
   (e.g. Sunny- Go for a walk, Rainy-Read a book, Snowy-Build a snowman)
   Ans:
       weather="Sunny"

if weather == "Sunny":
    activity= "Go for a walk"
elif weather == "Rainy":
    activity = "Read a Book"
else :
    activity = "Build a snowman"
    
print(activity)

6.Transportation Mode Selectio
  probelm: Choose a transportation based on the distance 
  (e.g., <3km: Walk, 3-15km-Bike, >15km-Car)
     distance = 5

if distance < 3:
    trasport ="Walk"
elif distance <=15:
    trasport ="Bike"
else :
    trasport = "Car"
print("AI recommends you the transport of: ",trasport)

7.Coffee Customization:
  problem: Customize a coffee order: "Small", "Medium" or "Large" with an option for
  "Extra shot" of espresso.
  Ans:
    order_size = "Midium"
extra_shot= True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else :
    coffee  = order_size + " coffee"

print("Order: ",coffee)
    
8.Password Strength Checker:
  Problem: Check if a possword is "Weak", "Medium" or "Strong".
  Criteria: <6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
  Ans:
   password="Secure3P@ss"
password_length=len(password)

if password_length <6:
    strength = "Weak"
elif password_length <=10:
    strength ="Medium"
else :
    strength = "Strong"

print("Password strength is: ",strength)


9.Leap Year Checker:
Prooblem : Determine  if a year is a leap year.
(Leap year are divisible by 4, but not divisible by 100 unless also divisible by 400).
Ans:
   year = 2024
if (year % 400 == 0) or (year % 4 == 0  and year % 100 != 0):
    print(year,"is a Leap Year")
else:
    print(year,"Not a Leap Year")

10.Pet Food Recommendation
Problem: Recommended a type of pet food based on the pet's species and age.
(e.g., Dog: <2 years- puppy food, Cat: >5 years -Senior cat food)
    
    
pet = "Dog"
age=6 
if (pet == "Dog" and age < 2) :
        print("puppy food")
else:
    if age > 5:
        print("Senior Cat Food")
    

Loops in python:
----------------
>>> userscore=input("Give me a score value: ")
Give me a score value: 200
>>> userscore
'200'
>>> userscore_in_int=int(userscore)
>>> userscore_in_int
200