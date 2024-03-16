from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    def color(self):
        print("white")


class Maruti_Suzuki(Car):  # marauti suzuki me pass likhte hai to vo bhi abstract class ban jaiga
    def mileage(self):
        print("mileage ia 30kmph")


class TATA(Car):
    def mileage(self):
        print("mileage is 35kmph")


class Duster(Car): 
    def mileage(self):
        print("mileage is 40kmph")


m1 = Maruti_Suzuki()
print(m1.mileage())

t1 = TATA()
t1.mileage()

d1 = Duster()
d1.mileage()

t1.color()
m1.color()
d1.color()


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def area(self):
        return self.width * self.height


circle = Circle(2)
print(circle.area())

rectangle = Rectangle(12, 4)
print(rectangle.area())


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


triangle = Triangle(5, 4)
print("Triangle Area:", triangle.area())

square = Square(3)
print("Square Area:", square.area())
