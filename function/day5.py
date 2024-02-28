# 8 nov 2023
# program 1
# positional arguement
def add(x, y):
    return x + y


ans = add(12, 12)  # actual arguemnet
ans = add(y=20, x=10)
print(ans)  # 24 #30 update


# program 2    # default value

def add(p=100, q=10):
    return p + q


ans2 = add()
print(type(add))  # function
print(ans2)

# program 3

list = [11, 22, 33, 44, 55, 66]

total = 0

for item in list:
    total = total + item

print(total)

# ======================================================

# Example ------
# 1 :
# Packing values into a tuple

my_tuple = 1, 2, 3, 4, 5

print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# 2 :
# Unpacking values from a tuple

my_tuple = (1, 2, 3, 4, 5)
# Unpack the values into individual variables
a, b, c, d, e = my_tuple

print(a, b, c, d, e)  # Output: 1 2 3 4 5

# 3 :
# Example of Unpacking with the Asterisk (*) Operator:
first, *rest, last = my_tuple

print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4]
print(last)   # Output: 5

# 4 :
# Unpacking values from a mixed-type iterable

mixed_data = [1, 'two', 3.0, (4, 5)]

# Unpack the values into individual variables
first, second, third, fourth = mixed_data

print(first)   # Output: 1
print(second)  # Output: 'two'
print(third)   # Output: 3.0
print(fourth)  # Output: (4, 5)


# ======================================================


# program 4

def addition(*args):
    print(args)  # This line prints the arguments passed to the function as a tuple.

    total = 0
    for item in args:
        total = total + item
    return total


print(addition(11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 123))
