#

# function :

# int as a parameter and int as return type

def add(x, y):
    return x + y


print(add(10, 10))


# float as a parameter float as return type

def sub(x, y):
    return x - y


print(sub(12.2, 8.1))


# boolen as a parameter and boolen as return type
def canDrive(age):
    if age >= 18:
        return True
    else:
        return False


print(canDrive(23))
print(canDrive(17))


# string as parameter and string as a return type

def string(word):
    return "shubh " + word


print(string("prabhat"))

# list as a parameter list as a return type:

Names = ["kabir", "vrushali", "shruti", "akash"]


def addnewlist(list):
    list.append("priya")
    return list


print(addnewlist(Names))

# dictionary as a parameter as a return type:

details = {
    "firstname": "vrushali",
    "lastname": "patil"

}


# 1 :
def addnewdetails(cityname):
    details["city"] = "nagpur"
    return cityname


print(addnewdetails(details))


# 2 :

def addnewdetails(details, age):
    details["age"] = age
    return details


print(addnewdetails(details, 23))

# set as parameter set as a return type:

setA = {11, 22, 33, 44, 55, 66}


def removeelemet(setB):
    setB.remove(22)
    return setB


print(removeelemet(setA))

# tuple as a parameter tuple as a return type

flower = ("lily", "jasmin", "rose", "sunflower")


def addnewflower(tupleA):
    tupleA = list(tupleA)  # ["lily", "jasmin", "rose", "sunflower"]
    tupleA.append("lotus")

    tupleA = tuple(tupleA)  # ("lily","lotus", "jasmin", "rose", "sunflower")
    return tupleA


print(addnewflower(flower))




