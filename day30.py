# overriding
# same method , same signature , different class has a relationship
class WorldBank:
    def save(self):
        print("I am save from worldbank 7%")

    def loan(self):
        print("I am loan from worldbank 9 %")


class SBI(WorldBank):
    def save(self):
        print("I am save from SBI 17%")
        super().save()

    def loan(self):
        print("I am loan from SBI 19 %")
        super().loan()


class PNB(WorldBank):
    pass


a = SBI()
a.save()
a.loan()
# b = PNB()
# b.loan()
# b.save()

# Duck typing
# Operator overloading
# Method overloading
# Method overriding

# 7-8 --- abtraction and interface
# function ----> regular expression , filehandling , exception handling

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.ra = radius

    def area(self):
        return 3.14 * self.ra  * self.ra

class Rectangle(Shape):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

recA = Rectangle(12,4)
circleA = Circle(5)

recA.area()
circleA.area()