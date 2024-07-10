# function

# program

# int
# int as param and inter as a return type
def add(x, y):
    return x + y


A = add(12, 13)
print(A)


# float
# float as a parameter and float as return type
def add(x, y):
    return x + y


B = add(4.5, 5.39)
print(B)


# string
# string as parameter and string a return
def greet(name):
    return "hello " + name


C = greet("sunset")
print(C)


# boolean
# boolean as parameter and boolean as return type

def canDrive(above18):
    if above18:
        return True
    else:
        False


D = canDrive(True)
if (D):
    print("Allowed to drive ....!")
else:
    print("Not allowed to drive")

# list
# list as parameter and list as return type
city = ["pune", "mumbai", "banglore", "kolkata"]


def addCity(addelement):
    addelement.append("Goa")
    return addelement


E = addCity(city)
print(E)
print(city)

# dict
# dict as parameter and dictionary as return type

dict = {
    "firstName": "vrushali",
    "lastName": "patil"
}


def addCityToInfo(info):
    info['city'] = "pune"
    return info


F = addCityToInfo(dict)
print(F)


# tuple
# tuple as parameter and tuple as return type
def addNum(tupA):
    tupA = list(tupA)
    tupA.append(555)
    tupA = tuple(tupA)
    return tupA


a, b, c = addNum((2, 3))
print(a)
print(b)
print(canDrive)

# set
# set as parameter and set as return type

setA = {11, 12, 13}


def addToSetA(ss):
    ss.add(44)
    return ss


G = addToSetA(setA)
print(setA)  # {11, 12, 13, 44}

# --------------------------------------------------------------------
# 11.6.24


# lambda functions
add = lambda a, b: a + b
a = add(1, 4)
print(a)  # 5


# function as parameter to another function

def addition(fn, a, b):
    x = fn(a, b)
    return x


print(addition(add, 3, 5))  # 8

def substraction(fn,x,y):
    return fn(x,y)
s = substraction(lambda x,y:x-y ,12,3)
print(s)       # 9



def greet():
    return lambda