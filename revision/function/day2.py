# program 1
# x , y   ---- formal arguments
# 12, 13  ---- actual arguments

def addA(x, y):
    return x + y


A = addA(12, 13)
print(A)  # 23


# program 2  "positional argument"

def subA(x, y):
    return x - y


B = subA(y=30, x=80)

print(B)  # 50


# program 3  "default arguments"

def mulA(x=10, y=40):
    return x * y


C = mulA()

D = mulA(4, 5)
print(C)  # 400
print(D)  # 20


# program 4 - variable length arguments
def addAll(*args):
    # print(args)
    total = 0
    for i in args:
        total = total + i
    return total


E = addAll(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(E)  # 120


def city(*args):
    for i in args:
        print("welcome" + i)


city("Pune", "Mumbai", "Chanai", "NAgpur")


# welcomePune
# welcomeMumbai
# welcomeChanai
# welcomeNAgpur


# kwargs

def info(**kwargs):
    print(kwargs)

    for i in kwargs:
        print(i, ":", kwargs[i])


info(first_name="vrushalii", lastName="patil", age=34, city="pune")
# output:
# first_name vrushali
# lastName patil
# age 34
# # city pune
