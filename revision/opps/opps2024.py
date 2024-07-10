# inhertance


# single


# class Father:
#
#     def __init__(self, fn, ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
#
# class Son(Father):
#     def __init__(self, fn, ln, sn):
#         super().__init__(fn, ln)
#         self.sonName = sn
#
#     def displaySonName(self):
#         print(self.sonName + self.lastName)
#
# obj1=Son("Naresh","Patil","Naman")
#
# (print(obj1.firstName))
# (print(obj1.lastName))
# (print(obj1.sonName))
#
# obj1.displayName()
# obj1.displaySonName()

# # multiple
# class GFather:
#
#     def __init__(self, gfn, ln):
#         self.GfirstName = gfn
#         self.lastName = ln
#
#     def displayGrandName(self):
#         print(self.GfirstName + self.lastName)
#
#
# class Father(GFather):
#     def __init__(self, gfn,ln,fn):
#         super().__init__(gfn,ln)
#         self.FatherName = fn
#
#     def displayFatherName(self):
#         print(self.FatherName + self.lastName)
#
# class Daughter(Father):
#     def __init__(self,gfn,ln,fn,dn):
#         super().__init__(gfn,ln,fn)
#         self.DaughterName =dn
#
#     def displayDaughterName(self):
#         print(self.DaughterName + self.lastName)
# obj2=Daughter("Motiram","Patil","Naresh","vrushaliii")
# print(obj2.GfirstName)
# print(obj2.FatherName)
# print(obj2.DaughterName)
#
#
# obj2.displayGrandName()
# obj2.displayFatherName()
# obj2.displayDaughterName()

# herarical

# class Mother:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayMName(self):
#         print(self.firstName + self.lastName)
#
# class Son(Mother):
#     def __init__(self, fn, ln,sn):
#         super().__init__(fn, ln)
#         self.sname = sn
#
#     def displaySName(self):
#         print(self.sname + self.lastName)
#
# class Daughter(Mother):
#     def __init__(self, fn, ln,dn):
#         super().__init__(fn, ln)
#         self.dname = dn
#
#     def displayDName(self):
#         print(self.dname + self.lastName)
#
#
#
# # multiilevel
# class  GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
# class Father(GrandFather):
#     def __init__(self, fn, ln,ffn):
#         super().__init__(fn, ln)
#         self.fname = ffn
#
#     def displayFName(self):
#         print(self.fname + self.lastName)
#
# class Son(Father):
#     def __init__(self, fn, ln, ffn,ssn):
#         super().__init__(fn, ln, ffn)
#         self.sname = ssn
#     def displaySName(self):
#         print(self.sname + self.lastName)

# # Method order resolution

# class A(object):
#     def method(self):
#         print('A class method is called')  # 3
#         super().method()

# class B(object):
#     def method(self):
#         print("B class method called")  # 5
#         super().method()

# class C(object):
#     def  method(self):
#         print("C class method called")  #6

# class X(A,B):
#     def method(self):
#         print("X class method called")  # 2
#         super().method()

# class Y(B,C):
#     def method(self):
#         print("Y class method is called")  #4
#         super().method()

# class P(X,Y,C):
#     def method(self):
#         print("P class method called") #1
#         super().method()
# p = P()
# p.method()

# --------------------------------------------------------------------

# duck typingg

# class Duck:
#     def talk(self):
#         print("QUCKK QUACKK")
#
# class Human:
#     def talk(self):
#         print('HELLO HII')
#
#
# def call_talk(obj):
#     obj.talk()
#
# call=Duck()
# # 1.
# # call.talk()
# # 2.
# call_talk(call)   # QUCKK QUACKK
#
# call2=Human()
#
# # 1.
# # call2.talk()
# # 2.
# call_talk(call2)   # HELLO HII


# ---------------------------------------
# class Human:
#     def talk(self):
#         print("hello vrushali")
#
# class Duckkk:
#     def talk(self):
#         print("Quackkkk")
#
# class Dog:
#     def Bark(self):
#         print("bow bow")
#
#
# def callTalk(obj):
#     if hasattr(obj,'talk'):
#         obj.talk()
#     elif hasattr(obj,'bark'):
#         obj.bark()
#
# a = Human()
# b = Dog()
# c = Duckkk()
#
# callTalk(a)   #hello vrushali
# callTalk(b)
# b.Bark()  #bow bow
# callTalk(c)    # Quackkkk


# # program 3
# # overloading --- same class , same methodName , different signature

# class Calculator:
#     def addition(self, a= None,b=None,c=None,d = None):
#         if(a != None and b != None and c != None and d != None):
#             print(a+b+c+d)
#         elif( a != None and b != None and c != None):
#             print(a+b+c)
#         elif(a != None and b != None):
#             print(a+b)
#
# a = Calculator()
# a.addition(12,3,4,3)
# a.addition(12,3,4)
# a.addition(12,3)


# # overriding  different class, same methodName , same signature

# class WorldBank:
#     def save(self):
#         print("I am saving method from worldBank")
#     def loan(self):
#         print("I am saving method from worldbank")
#
# class SBI(WorldBank):
#     def save(self):
#         print("I am saving method from SBI")
#     def loan(self):
#         print("I am saving method from SBI")
#
# class PNB(WorldBank):
#     def save(self):
#         print("I am saving method from PNB")
#         super().loan()
#     def loan(self):
#         print("I am saving method from PNB")
#
# d = SBI()
# d.save()
# d.loan()
#
# d = PNB()
# d.save()
# d.loan()


# Polmorphism -- operator overloading


class BookX:
    def __init__(self, x):
        self.pages = x


class BookY:
    def __init__(self, x):
        self.pages = x


# B1 = BookX(12)
# B2 = BookY(12)
# print(B1.pages+B2.pages)   # 24

# print(B1+B2)   # TypeError

print([11, 22, 33] + [1, 2, 3])  # [11, 22, 33, 1, 2, 3]
print([11, 22, 33] + [1 + 2 + 3])  # [11, 22, 33, 6]


# 2


# class BookA:
#     def __init__(self,x):
#         self.pages=x
#     #     method:
#     def __add__(self, other):
#         return self.pages + other.pages
#
# class BookB:
#     def __init__(self,x):
#         self.pages =x
#
#
# bookA=BookA(1)
# bookB=BookB(1)
#
# print(bookA+bookB)   # 2


# 3

class BookC:
    def __init__(self, x):
        self.pages = x

    def __gt__(self, other):
        return self.pages > other.pages


class BookD:
    def __init__(self, x):
        self.pages = x


bookC = BookC(12)
bookD = BookD(10)

print(bookC > bookD)


# 4.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class Attendance:
    def __init__(self, days):
        self.days = days


Emp1 = Employee('vrushali', 100)
atendance1 = Attendance(25)

Total1 = Emp1 * atendance1
print(Total1)  # 2500
