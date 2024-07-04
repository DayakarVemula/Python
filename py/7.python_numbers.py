"""
Python Numbers :

There are three numeric types in Python:

int
float
complex


x = 1    # int
y = 2.8  # float
z = 1j   # complex

To verify the type of any object in Python, use the type() function:

Example


print(type(x))
print(type(y))
print(type(z))

"""
x = 1    # int
y = 2.8  # float
z = 1j    #complex
print(type(x))
print(type(y))
print(type(z))

"""
Int :{integer}

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Example
Integers:
"""
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

"""
Float :

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Example
Floats:
"""

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


#Float can also be scientific numbers with an "e" to indicate the power of 10.



x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


"""
Complex :

Complex numbers are written with a "j" as the imaginary part:

Example
Complex:
"""

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


"""
Type Conversion :

You can convert from one type to another with the int(), float(), and complex() methods:

Example
Convert from one type to another:
"""


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#Note: You cannot convert complex numbers into another number type.

"""
Random Number :

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
 


Example
Import the random module, and display a random number between 1 and 9:
"""
import random

print(random.randrange(1, 10))

"""
Python Casting :


Specify a Variable Type :

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
ExampleGet your own Python Server
Integers:
"""

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)



x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
