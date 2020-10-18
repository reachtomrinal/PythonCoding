# Section 1.2: Creating variables and assigning values
# Integer
a = 2
print(a)
# Output: 2

# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807

# Floating point
pi = 3.14
print(pi)
# Output: 3.14

# String
c = 'A'
print(c)
# Output: A

# String
name = 'John Doe'
print(name)
# Output: John Doe

# Boolean
q = True
print(q)
# Output: True

# Empty value or null data type
x = None
print(x)
# Output: None

# list of keywords
import keyword

print(keyword.kwlist)

q = True
print(type(q))
# Output: <type 'bool'>


x = None
print(type(x))
# Output: <type 'NoneType'>

s = """w'o"w"""
print(repr(s))
print(str(s))
print(f"repr func value {eval(repr(s)) == s}")  # Output: True
print(f" str func value {eval(str(s)) == s}")  # Gives a SyntaxError

