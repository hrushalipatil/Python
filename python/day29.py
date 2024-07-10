# overlodng and overiding

# overloading
class addition1:
    def __init__(self, add):
        self.add = add


class addition2:
    def __init__(self, add):
        self.add = add


A = addition1(12)
B = addition2(12)
# print(A+B)  # error
print(A.add + B.add)  # 24


# program 2:
class addition1:
    def __init__(self, add):
        self.add = add

    def __add__(self, other):
        return self.add + other.add


class addition2:
    def __init__(self, add):
        self.add = add


C = addition1(12)
D = addition2(12)
print(C + D)  # 24


# program 3

class greater1:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value


class greater2:
    def __init__(self, value):
        self.value = value


E = greater1(50)
F = greater2(100)
print(E > F)  # false


# print(E<F)


# program 4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class Attendance:
    def __init__(self, days):
        self.days = days


e1 = Employee("vrushali", 1)
e2 = Attendance(30)

G = e1 * e2
print(G)  # 30


# overloading and overriding
class Cal:
    # def addition(self,x,y):
    #     print(x+y)
    #
    # def addition(self,x,y,z):
    #     print(x+y+z)

    def addition(self, x=None, y=None, z=None, a=None):
        # print(x + y + z + a)
        if (x != None and y != None and z != None and a != None):
            print(x + y + z + a)
        elif (x != None and y != None and z != None):
            print(x + y + z)
        elif (x != None and y != None):
            print(x + y)


a = Cal()
a.addition(12, 13)
a.addition(12, 13, 45)
a.addition(12, 13, 45, 67)