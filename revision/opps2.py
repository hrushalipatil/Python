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
        print(self.firstName + self.lastName)


class Father(GrandFather):
    def __init__(self, fn, ln, ffn):
        super().__init__(fn, ln)
        self.fName = ffn

    def displayFanme(self):
        print(self.fName + self.lastName)


class Son(Father):
    def __init__(self, fn, ln, ffn, ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)


chinmay = Son("manohar", "deshpande", "shirsh", "chinmay")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.fName)
print(chinmay.sname)

chinmay.displaySname()
chinmay.displayFanme()
chinmay.displayGname()
