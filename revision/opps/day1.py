# program 1
class Person:
    firstName = "vrushali"
    lastName = "patil"

    def walk(self):
        print("im walking")

    def talk(self):
        print("im talking")


A = Person()

print(A.firstName)  # vrushali
print(A.lastName)  # patil

A.talk()  # im talking
A.walk()  # im waling


# program 2

class Person1:
    # property / instance variable
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    # instance method
    def talk(self):
        print("talkkkk")

    def walk(self):
        print("walkk")


B = Person1('sayali', 'jogi')
print(B.firstName)
print(B.lastName)

B.talk()
B.walk()
