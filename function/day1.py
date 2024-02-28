# 1 nov 2023
# ========lamda========#
# program 1

def addition(x, y):
    return x + y


A = addition(12, 12)
print(A)  # 24

# function expressoion --- lamba functions
# functionName = lambda parameter:expression

# program 2
square = lambda sq: sq * sq
B = square(15)
print(B)  # 225

# program 3

addition = lambda add1, add2: add1 + add2
C = addition(10, 10)
print(C)  # 20

# program 4
sub = lambda P, Q: P - Q


def substraction(function, P, Q):
    # function = lambda P, Q: P - Q
    D = function(P, Q)
    return D


E = substraction(sub, 100, 10)

print(E)

# part 2
rectangle = lambda l, b: l * b


def rec(function, l, b):
    r = function(l, b)
    return r


call = rec(rectangle, 10, 20)
print(call)  # 200
