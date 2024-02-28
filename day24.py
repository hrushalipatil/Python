# inheritance
class Student:

    def setFullName(self, fn):
        self.fullName = fn

    def getFullName(self):
        return self.fullName

    def setAge(self, ag):
        self.age = ag

    def getAge(self):
        return self.age

    def setAdharNo(self, no):
        self.adharNo = no

    def getAdharNo(self):
        return self.adharNo


A = Student()

A.setFullName("vrushali patil")
A.setAge(27)
A.setAdharNo(89201010100)

print(A.fullName)
print(A.getFullName())

print(A.age)
print(A.getAge())

print(A.adharNo)
print(A.getAdharNo())



# program  2
class Teacher:

    def setFullName(self, fn):
        self.fullName = fn

    def getFullName(self):
        return self.fullName

    def setAge(self, ag):
        self.age = ag

    def getAge(self):
        return self.age

    def setAdharNo(self, no):
        self.adharNo = no

    def getAdharNo(self):
        return self.adharNo

    def setSalary(self,salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

AA= Teacher()
AA.setFullName("sanjeet wandhare")
print(AA.fullName)
print(AA.getFullName())

AA.setAge(12)
print(AA.getAge())

AA.setSalary(1000)
print(AA.getSalary())

AA.setAdharNo(123)
print(AA.getAdharNo())
