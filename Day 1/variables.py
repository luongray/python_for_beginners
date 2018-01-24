# Think of variables in programming like empty containers that you put stuff in.
# The stuff you store in variables have different types.
my_string = "hello"
my_int = 5
my_float = 5.5
my_list = [1,2,3]
my_set = {4,5,6}


# You can see the type of a variable by passing it into type()
print type(my_string)
print type(my_int)
print type(my_float)
print type(my_list)
print type(my_set)


# You can also type cast in python, but you can't do some translations like str to dict
print str(5)
print int("5")
print list("this is my string") #breaks up string into letters and appends them to a list


# Since python is object oriented, you can perform methods on objects. Every variable in python is an object.
# Use dir() to list all the 'methods' you can perform on an object
print dir("this is my string")
"""
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',  
... 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""


# Use help() to get detailed description of what these methods do
help(5)
"""
Help on int object:

class int(object)
 |  int(x=0) -> int or long
 |  int(x, base=10) -> int or long
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is floating point, the conversion truncates towards zero.
 |  If x is outside the integer range, the function returns a long instead.
 ...
 """

# Python variables refer to a location in memory. If 2 variables are the same, they will have the same memory address.
# You can get a variable's memory address by passing it into 'id()'.
a = 5
print id(5)
print id(a)

# But, for mutable variables, we see that, even though the values are the same, the address is different
a = [5]
b = [5]
print id(a)
print id(b)

# This means that a == b returns True, but a is b returns False
print a == b
print a is b



