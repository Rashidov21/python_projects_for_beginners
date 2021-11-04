# Variable lower_snake
first_name = 'Mike'

# Class and module CamelCase
class InvoiceDetail:

# Constant
MAX_USER = 100 # All uppercase

# Indentation : 4 spaces
if num > 9:
    print('Small number')

name = 'Mike' # string
age = 42 # int
price = 199.99 # float
is_active = True # boolean
colors = ['red', 'green', 'blue'] # list
products = { 'name': 'iPad Pro', 'price': 199.99 } # dict
MAX_USER = 100 # Constant


# Python is a strong type language
number = 50 + "50" # TypeError

# Convert to string
number = 50 + int("50") # 100

# Convert to string
my_text = str(199.99)   # "199.99"

# Convert to number
my_number = int('21.99') # 21
my_number = float('21.99') # 21.99

# Get type
type(my_text) # <class 'str'>
type(my_number) # <class 'float'>

# Check if number 0 to 9
isdigit('8') # True

# Check type
isinstance(my_number, int) # True


name = 'Mike'
# or
name = "Mike"
# or
message = """This is multiline
string that is easier to
read and assign"""

# escape characters \n will do a line break
message = "Hello \nWorld"

# raw string (ignore escape characters)
message = r"https:\\example.com\index.html"

# Convert to lower case
name.lower() # mike

# Convert to upper case
name.upper() # MIKE

# Convert first char to Capital letter
name.capitalize() # Mike

# Convert first char of all words to Capital letter
name = 'mike taylor'
name.title() # Mike Taylor

# Chain methods
name = 'MIKE'
name.lower().capitalize() # Mike

name = 'Mike'

# Start with ?
name.startswith('M') # true

# End with ?
name.endswith('ke') # true

# String length
len(name) # 4

# String concatenation
full_name = first_name + ' ' + last_name

# String format
full_name = f"{first_name} {last_name}"

# Remove leading and trailing characters (like space or \n)
text = ' this is a text with white space '
text.strip() # 'this is a test with white space'

name = 'Mike'
# Get string first character
name[0] # M

# Get string last character
name[-1] # e

# Get partial string
name[1:3] # ik

# Replace
name.replace('M', 'P') # Pike

# Find (return pos or -1 if not found)
name.find('k') # 2

# List to string
colors = ['red', 'green', 'blue']
', '.join(colors) # 'red, green, blue'


# Print to console
print('Hello World')

# Print multiple string
print('Hello', 'World') # Hello World

# Multiple print
print(10 * '-') # ----------

# Variable pretty printer (for debug)
from pprint import pprint
pprint(products) # will output var with formatting

# Get keyboard input
name = input('What is your name? ')

# Random (between 0 and 1)
from random import random 
print(random()) # 0.26230234411558273

# Random beween x and y
from random import randint
print(randint(3, 9)) # 5

# Rounding
number = 4.5
print(round(number)) # 5

number = 4.5163
print(round(number, 2)) # 4.52

# Path
import os
current_file_path = __file__
folder_name = os.path.dirname(current_file_path)
new_path = os.path.join(folder_name, 'new folder')

# Round number
solution = round(12.9582, 2) # 12.96


if x == 4:
    print('x is 4')
elif x != 5 and x < 11:
   print('x is between 6 and 10')
else:
   print('x is 5 or greater than 10')

#In or not in
colors = ['red', 'green', 'blue', 'yellow']
if 'blue' in colors:
if 'white' not in colors:

# Ternary
print('y = 10') if y == 10 else print('y != 10') 

# ShortHand Ternary
is_valid = 'Valid'
msg = is_valid or "Not valid" # 'Valid'

# Falsy
False, None, 0, empty string "", empty list [], (), {}

# Truthy
True, not zero and not empty value 


# iterating over a sequence (list, string, etc.)
for item in items:
    print(item)

# With index
for index, item in enumerate(items):
    print(index, item)

# Range
for i in range(10):  #0..9
    print(i)

for i in range(5, 10): #5..9
    print(i)

# While loop
while x > 10:
    print(x)
    # exit loop
    if x == 5:
        break
    # Jump to next while
    if x == 3:
        continue

    x += 1

# For loop dic
for key, value in my_dict.items():
    print(key, value)

# List comprehension: 
# values = [(expression) for (value) in (collection)]
items = [value*2 for value in items]

# List comprehension filtering
# values = [expression for value in collection if condition]
even_squares = [x * x for x in range(10) if x % 2 == 0]


# Create a list
fruits = ['orange', 'apple', 'melon']

# Append to List
fruits.append('banana')

# List length
nb_items = len(fruits)

# Remove from list
del fruits[1]   #remove apple

# List access
fruits[0]  # first item
fruits[-1] # last item

# Slice my_list[start:finish:step] ([::-1] reverse list) 
fruits = fruits[1:3]
fruits[:3]  # first 3
fruits[2:]  # last 2
copy_fruits = fruits[:] # copy

# List length
nb_entry = len(fruits) 

#Create list from string
colors = 'red, green, blue'.split(', ')

# Array concact
color1 = ['red', 'blue']
color2 = ['green', 'yellow']
color3 = color1 + color2

# Concat by unpacking
color3 = [*color1, *color2]

# Multiple assignment
name, price = ['iPhone', 599]

#Create a Tuple (kind of read only list)
colors = ('red', 'green', 'blue')

# Sort
colors.sort() # ['blue', 'green', 'red']
colors.sort(reverse=True) # ['red', 'green', 'blue']
colors.sort(key=lambda color: len(color)) # ['red', 'blue', 'green']


# Create a empty dict
product = {}

#Create a dict with key/value
product = {'id': 100, 'name': 'iPadPro'}

# Access dict value by key
print(product['name']) # iPadPro

# Access dict
product.get('name') # if key not exist return None
product.get('name', 'default value') # if key not exist return default value

# Adding a new key/value
product['description'] = "Modern mobile device"

# Get dict keys
product.keys() # ['id', 'name', 'description']

# Get dic values
product.values() # ['100', 'iPadPro', 'Modern mobile device']

# Create a list of dict
products = [
    {'id': 100, 'name': 'iPadPro'},
    {'id': 200, 'name': 'iPhone 12'},
    {'id': 300, 'name': 'Charger'},
]

# Access list of dict
print(products[2]['name']) # Charger

# Search list dict
items_match = [item for product in products if product['id'] == 300]
# [{'id': 300, 'name': 'Charger'}]

# Sum list dict
total = sum([product['price'] for product in products])


# Create a function
def say_hello():
    print('Hello World')

# Function with argument (with default value)
def say_hello(name = 'no name'):
    print(f"Hello {name}") 

# Function with argument (with optional value)
def say_hello(name = None):
    if name:
        print(f"Hello {name}") 
    else:
        print('Hello World')

# Call a function
say_hello('Mike') # Hello Mike

# Call using keyword argument
say_hello(name = 'Mike') 

# Function returning a value
def add(num1, num2):
   return num1 + num2

num = add(10, 20) # 30

# Arbitrary numbers of arguments *args
def say_hello(*names):
    for name in names:
        print(f"Hello {name}")

# Arbitrary numbers of keywords arguments **kwargs
def say_hello(**kwargs):
    print(kwargs['name'])
    print(kwargs['age'])

say_hello(name = 'Mike', age = 45)

# Lambda function
x = lambda num : num + 10
print(x(20)) # 30



from datetime import datetime, timedelta

# Return the current date and time.
datetime.now()

# Create a date time object
date = datetime(2020,12,31) # Dec 31 2020

# Add to date/time (weeks, days, hours, minutes, seconds) 
new_year = date + timedelta(days=1) # Jan 1 2021

# Format a date to string
new_year.strftime('%Y/%m/%d %H %M %S') # 2021/01/01 00 00 00 
new_year.strftime('%A, %b %d') # Friday, Jan 01

# Extract from date
year = new_year.year # 2021
month = new_year.month # 01



# Reading a file and storing its lines
filename = 'demo.txt'
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line)

# Writing to a file
filename = 'settings.txt'
with open(filename, 'w') as file:
    file.write("MAX_USER = 100")

# File exist?
from os import path
path.exists('templates/index.html') # True/False

# CSV
import csv
csv_file = 'export.csv'
csv_columns = products[0].keys() # ['id', 'name']
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for item in products:
        writer.writerow(item)



age_string = input('Your age? ')

try:
	age = int(age_string)
except ValueError:
	print("Please enter a numeric value")
else:
	print("Your age is saved!")
finally:
    print("Finally block..")



# Create a class
class Product:
    pass

# Class attribute
class Product:
    nb_products = 0

print(Product.nb_products) # 0

# Create new object instance
product_1 = Product()

# Object instance attributes
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Create instance with attributes
product_1 = Product('iPadPro', 699.99)
product_2 = Product('iPhone12', 799.99)
print(product_1.name) # iPadPro

# instance method
class Product:
    def display_price(self):
        return f"Price : {self.price}"

print(product_1.display_price())

# class method
class Product:
    # ... 
    @classmethod
    def create_default(cls):
        # create a instance 
        return cls('Product', 0) # default name, default price

product_3 = Product.create_default() 

# static method
class Product:
    # ... 
    @staticmethod
    def trunc_text(word, nb_char):
        return word[:nb_char] + '...' 

product_3 = Product.trunc_text('This is a blog', 5) # This i... 

# Python Inheritance
class WebProduct(Product):
    def __init__(self, name, price, web_code):
        super().__init__(name, price)
        self.web_code = web_code

# Private scope (naming convention only)
def __init__(self, price):
    self.__price = price
# p = Product("Iphone11", 699.99)
# p.__price
# Getter and setter
class Product:
    def __init__(self):
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

# Mixins
class Mixin1(object):
    def test(self):
        print "Mixin1"

class Mixin2(object):
    def test(self):
        print "Mixin2"

class MyClass(Mixin2, Mixin1, BaseClass):
    pass

obj = MyClass()
obj.test() # Mixin2
