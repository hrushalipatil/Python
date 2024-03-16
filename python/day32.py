#
# # function which takes other functions as input,add additioal funtion and return it
# # it is callable python object which modifies other class/function
#
#
#
#
# def decor(fun):
#     def inner():
#
#         e = input("enter a something...")
#         return e , fun()   # Call fun() to execute the decorated function
#     return inner
# @decor
# def printer():
#     print("welcome")
#     print("welcome")
#
# # printer()
#
# answer = printer()
# print("User input:", answer)
#
#
#
def decor(fun):
    def inner():
        fun()  # Print "Welcome" messages first
        e = input("Enter something: ")
        print("User input:", e)

    return inner


@decor
def printer():
    print("Welcome")
    print("android phone ")


printer()  # No need to assign the result to a variable


# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
#
# def num():
#     return 10
#
# q1 = decor(num)
# print(q1())

# def decor(fun):
#     def inner():
#         value = fun() + 10
#         return value
#     return inner
#
# @decor
# def num():
#     return 10
# print(num())

# program 3
def decor(addition):
    def inner():
        return addition() + 2

    return inner


def decor1(mul):
    def inner():
        return mul() * 2

    return inner


@decor
@decor1
def add():
    A = int(input("Enter a number :"))
    return A


# q1 = decor1(decor(add))  # 10+2 = 12*2 = 24
# print(q1())
#
# q2 = decor(decor1(add))  # 10*2 = 20+2 = 22
# print(q2())

# print(add())


# # program 4
def split_string(word):
    def inner():
        a = word().split(" ")
        return a

    return inner


@split_string
def word():
    return "Octomber 2023"


@split_string
def date():
    return "10 November 1989"


print(date())

dict = {
    "firstname": "vrushali",
    "lastname": "patil",
    "age": 23
}

for key, value in dict.items():
    if key != "age":
        print(key, value)
#
#
#
# # Creating a dictionary
# person_info = {'firstname': 'Vrushali', 'lastname': 'Patil', 'age': 24}
#
# # Printing all key-value pairs excluding 'age'
# for key, value in person_info.items():
#     if key != 'age':
# #         print(f"{key}: {value}")
#
# 
#
# python
# Copy code
# # Creating a dictionary
# person_info = {'firstname': 'Vrushali', 'lastname': 'Patil', 'age': 24}
#
# # Removing 'age' key from the dictionary
# age_value = person_info.pop('age', None)
#
# # Printing the remaining key-value pairs
# print(person_info)