# inner class
# class Person:
#     def  __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#         self.db = self.DOB()
#
#     class DOB:
#         def __init__(self):
#             self.dt = 11
#             self.mn = 11
#             self.yy = 1989
#
#         def displayDate(self):
#             print(self.dt,self.mn,self.yy)
#
# amol = Person("amol","rao")
# print(amol.firstName)
# print(amol.lastName)
# e = amol.db
#
# print(e.dt)
# print(e.mn)
# print(e.yy)
# e.displayDate()


# program 2
class Person:
    def __init__(self, fn, ln, dd, mm, yy):
        self.firstName = fn
        self.lastName = ln
        self.db = self.DOB(dd, mm, yy)

    class DOB:
        def __init__(self, dd, mm, yy):
            self.dt = dd
            self.mn = mm
            self.yy = yy

        def displayDate(self):
            print(self.dt, self.mn, self.yy)


amol = Person("amol", "rao", 12, 34, 1990)
print(amol.firstName)
print(amol.lastName)
e = amol.db

print(e.dt)
print(e.mn)
print(e.yy)
e.displayDate()


# # program3
# class Person:
#     def __init__(self,name):
#         self.fullName = name
#
#     def displayName(self):
#         print(self.fullName)
#
#     class DOB:
#         def __init__(self):
#             self.dd = 12
#             self.mm = 7
#             self.yy = 1990
#
#         def displayDate(self):
#             print(self.dd,self.mm,self.yy)
#
#         class Display:
#                 greet = "hello"
#
# chinmay = Person("chinmay deshpande")
# chinmay.displayName()
#
# q1  = Person("amol rao").DOB()
# print(q1.yy)
# print(q1.mm)
# print(q1.dd)
# q1.displayDate()
#
#
# q2  = Person("ram dani").DOB().Display()
# print(q2.greet)

# 24 polymorphis, inheritance
# abstraction , interface

#    .......... 1.......
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"my name is {self.name}, age is {self.age}")

    class DOB:
        def __init__(self, dd, mm, yy):
            self.date = dd
            self.month = mm
            self.year = yy

        def display(self):
            print(f"my date of birth is {self.date}/{self.month}/{self.year}")


obj1 = Student("vrushali", 23)

obj2 = obj1.DOB(21, 6, 1999)  # my name is vrushali ,age is 23

obj2.display()  # my date of birth is 21/6/1999


# but i dont want to create more object for ineer class
class Student:

    def __init__(self, name, age, dd, mm, yy):
        self.name = name
        self.age = age
        self.dob = self.DOB(dd, mm, yy)

    def display(self):
        print(f"my name is {self.name}, age is {self.age}")
        self.dob.display()

    class DOB:
        def __init__(self, dd, mm, yy):
            self.date = dd
            self.month = mm
            self.year = yy

        def display(self):
            print(f"my date of birth is {self.date}/{self.month}/{self.year}")


person = Student("sanjeet", 26, 13, 10, 1996)
person.display()
