# inheritance with constructor
# 1.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f"my name is {self.name},age is {self.age}")
#
#
# class Student(Person):
#     pass
#
#
# S = Student("vrushali", 24)
# print(S.__dict__)
# # print(S.display())

# 2.           single level
# if you add constructor in student class  you access student class but you trying do
# access the person you got error ,cant access them thats why we use super that you
# can also access parent also


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayperson(self):
        print(f"my name is {self.name},age is {self.age}")


class Student(Person1):
    def __init__(self, marks, attendance, name, age):
        super().__init__(name, age)
        self.marks = marks
        self.attendance = attendance

    def displaystudent(self):
        print(f"i got {self.marks} marks , my attendance is {self.attendance}")


Q = Student(90, 30, "vaishali", 57)
Q.displaystudent()
Q.displayperson()


# print(Q.name)
# print(Q.age)

# multilevel inheritance
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayperson(self):
        print(f"my name is {self.name},age is {self.age}")


class Student(Person1):
    def __init__(self, marks, attendance, name, age):
        super().__init__(name, age)
        self.marks = marks
        self.attendance = attendance

    def displaystudent(self):
        print(f"i got {self.marks} marks , my attendance is {self.attendance}")


class Teacher(Student):
    def __init__(self, salary, bonus, marks, attendance, name, age):
        super().__init__(marks, attendance, name, age)
        self.salary = salary
        self.bonus = bonus

    def displayteacher(self):
        print(f"english teacher salary {self.salary} ,increment bonus {self.bonus}")


Q = Teacher(23000,"5%",80,20,"vrushali",23)
Q.displayteacher()
Q.displayperson()


# hierarchical inheritance ---one parent and multiple child classes
class Human:
    def __init__(self, name):
        self.name = name

    def display1(self):
        print(f"my name is {self.name}")


class Employee(Human):
    def __init__(self, salary, name):
        super().__init__(name)
        self.salary = salary

    def display2(self):
        print(f"salary will be {self.salary}")


class Managers(Employee):
    def __init__(self, bonus, salary, name):
        super().__init__(salary, name)
        self.bonus = bonus

    def display3(self):
        print(f"bonus will be {self.bonus}")


m1 = Managers(2000, 5000000, "vrushali")
m2 = Employee(9999999900, "kallo")
print(m2.name)
print(m2.salary)
m2.display2()
m1.display1()
m1.display2()
m1.display1()


# multiple inheritance ------two parents and single child

class Father:

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print("Father method called")
        print(self.firstName + self.lastName)

class Mother:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print("Mother method called")
        print(self.firstName + self.lastName)

class Son(Mother,Father):
    def __init__(self,firstName, lastName,sonname):
        super().__init__(firstName, lastName)
        self.sonname = sonname

    def displaySname(self):
        print(self.sonname + self.lastName)

vrushali = Son("aman","patil","rajkumar")
vrushali.displaySname()
vrushali.displayName()






# # single inheritance
# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#     def displayName(self):
#         print(self.firstName+ self.lastName)
#
# class Teacher(Student):
#     def __init__(self,fn,ln,sl):
#         super().__init__(fn,ln)
#         self.salary = sl
#
#     def displaySalary(self):
#         print(self.salary)
#
# amolT = Teacher("amol","rao",1000)
# print(amolT.salary)
# print(amolT.firstName)
# print(amolT.lastName)
# amolT.displayName()
# amolT.displaySalary()
#
#
# # multi-level
#
#
# class GrandFather:
#
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#     def displayGname(self):
#         print(self.firstName + self.lastName)
#
# class Father(GrandFather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fName = ffn
#
#     def displayFanme(self):
#         print(self.fName + self.lastName)
#
# class Son(Father):
#     def __init__(self,fn,ln,ffn,ssn):
#         super().__init__(fn,ln,ffn)
#         self.sname  = ssn
#     def displaySname(self):
#         print(self.sname + self.lastName)
#
# chinmay = Son("manohar","deshpande","shirsh","chinmay")
# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.fName)
# print(chinmay.sname)
#
# chinmay.displaySname()
# chinmay.displayFanme()
# chinmay.displayGname()
#
# # program 3
# class Mother:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayMName(self):
#         print(self.firstName + self.lastName)
#
# class SonM(Mother):
#
#     def __init__(self,fn,ln,sn):
#         super().__init__(fn,ln)
#         self.sname = sn
#
#     def displaySname(self):
#         print(self.sname + self.lastName)
#
#
# class DaughterM(Mother):
#
#     def __init__(self, fn, ln, dn):
#         super().__init__(fn, ln)
#         self.dname = dn
#
#     def displayDname(self):
#         print(self.dname + self.lastName)
#
# chinmay = SonM("kanchan","deshpande","chinmay")
# gauri = DaughterM("kanchan","deshpande","gauri")
#
# chinmay.displaySname()
# chinmay.displayMName()
#
# gauri.displayMName()
# gauri.displayDname()
#
# # program 4
#
#
# class FatherN:
#
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#
#     def displayName(self):
#         print("Father method called")
#         print(self.firstName + self.lastName)
#
# class MotherN:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#
#     def displayName(self):
#         print("Mother method called")
#         print(self.firstName + self.lastName)
#
# class SonN(MotherN,FatherN):
#     def __init__(self,firstName, lastName,sname):
#         super().__init__(firstName, lastName)
#         self.sname = sname
#
#     def displaySname(self):
#         print(self.sname + self.lastName)
#
# chinmayN = SonN("shirish","deshpande","chinmay")
# chinmayN.displaySname()
# chinmayN.displayName()
