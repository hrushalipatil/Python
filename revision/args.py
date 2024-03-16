

# program 1
def add(A, B):
    return A + B


X = add(12, 19)
print(X)  # 31

# program 2
addition = lambda x, y: x + y
Y = addition(12, 23)

print(Y)  # 35

# program 3


square = lambda x, y: x * y

Z = square(2, 2)
print(Z)  # 4


# program 4

# args----colloction
def additionofall(*args):
    print(args)  # (11,22,33,44,55,66,77,88)
    total = 0
    for item in args:
        total = total + item

    return total


P = additionofall(11, 22, 33, 44, 55, 66, 77, 88)

print(P)  # 396


# program 5

def updateCity(**kwargs):
    print(kwargs)  # {'firstname': 'vrushali', 'city': 'pune', 'age': 23}
    kwargs["firstname"] = "sayali"
    return kwargs


Q = updateCity(firstname="vrushali", city="pune", age=23)
print(Q)


# program 6

def addition(x=1, y=2):
    print(x + y)


addition()  # x=1, y=2  output: 3

addition(2, 10)  # x=2,y=10    output: 12


# program 7

def addition(P, Q, R):
    print(P + Q + R)


# P=1,Q=2,R=3
addition(1, 2, 3)  # 6


# i want value of P=3


def addition(L=3, M=2, N=1):
    print(L + M + N)


addition()  #6
