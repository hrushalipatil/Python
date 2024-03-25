# single inheritance

class Student:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)


class Teacher(Student):
    def __init__(self, fn, ln, sl):
        super().__init__(fn, ln)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)


vrushali = Teacher("vrushali", "patil", 1000)
print(vrushali.salary)
print(vrushali.firstName)
print(vrushali.lastName)
vrushali.displayName()
vrushali.displaySalary()


# multi-level


class GrandFather:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayGname(self):
        print(self.firstName, self.lastName)


class Father(GrandFather):
    def __init__(self, fn, ln, ffn):
        super().__init__(fn, ln)
        self.fName = ffn

    def displayFanme(self):
        print(self.fName, self.lastName)


class Son(Father):
    def __init__(self, fn, ln, ffn, ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn

    def displaySname(self):
        print(self.sname, self.lastName)


A = Son("naresh", "patil", "vrushali", "moti")
print(A.firstName)
print(A.lastName)
print(A.fName)
print(A.sname)

A.displaySname()
A.displayFanme()
A.displayGname()


# hierarchical inheritance ---one parent and multiple child classes


class Papa:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayInfo(self):
        print(self.firstName + self.lastName)


class Son(Papa):

    def __init__(self, fn, ln, aadharNo):
        super().__init__(fn, ln)
        self.aadhar = aadharNo

    def displayInfo(self):
        print(self.firstName, self.lastName, self.aadhar)


class Daughter(Papa):
    def __init__(self, fn, ln, houseno, ):
        super().__init__(fn, ln)
        self.houseNo = houseno

    def displayInfo(self):
        print(self.firstName, self.lastName, self.houseNo)


kabir = Son("kabir", "wandhare", 12134)
print(kabir.firstName)
print(kabir.lastName)
print(kabir.aadhar)
kabir.displayInfo()

vrushali = Daughter("vrushali", "wandhare", 1234)

print(vrushali.firstName)
print(vrushali.lastName)
print(vrushali.houseNo)
vrushali.displayInfo()
