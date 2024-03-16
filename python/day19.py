# # class and object        class method
# 1.
class Details:
    firstname = "vrushali"
    lastName = "patil"
    adharNo = 123

    def Displaydetails(self):
        print(self.firstname + self.lastName)
#
#
# # # obj 1
kabir = Details()
print(kabir.firstname)
print(kabir.lastName)
print(kabir.adharNo)
kabir.Displaydetails()

# # obj 2
kabir.firstname = "sanjeet"
kabir.lastName = "wandhare"
kabir.adharNo = 888888
kabir.Displaydetails()  # sanjeetwandhare


# # 2.
class Price:
    name = "vru"
    age = 23
    price = 2000

    def display(self):
        print("my name is", self.name)
        print("my age is", self.age)
        print("Saving i have", self.price, "rs")
xyz=Price()
print(xyz.name)
print(xyz.age)
print(xyz.price)
xyz.display()

kabir=Price()
kabir.name="oggy"
kabir.age=22
kabir.price=22222
kabir.display()

# program 3
# using constructor

class Person:
    # class level
    country = "India"

    # constructor
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

l2 = Person("komal2","dongre2",4562)
l3 = Person("komal3","dongre3",4563)
l4 = Person("komal4","dongre4",4564)

l2.displayName()
l3.displayName()
l4.displayName()

print(l2.country)
print(l3.country)
print(l4.country)

# program 4
class employee:
    # class level variable
    state = "maharashtra"

    # constructor
    def __init__(self, name, age, salary):  # member function/ member method.name,age,salary---argument
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"my name is {self.name},my age is {self.age},i got {self.salary} per month")

    # instance method

    def updateName(self, nm):
        self.name = nm

    def updateage(self, ag):
        self.age = ag

    @classmethod
    def ChangeState(cls, statename):
        cls.state = statename


a1 = employee("vrushali", 21, 2222222)
a2 = employee("sanny", 21, 9999999999)
a3 = employee("daisy", 21, 1111111111)
a1.display()
print(a1.state)  # maharashtra

a1.ChangeState("Goa")
print(a1.state)  # Goa
print(a2.state)  # Goa --------------it will change because class method is applied for all objects

a2.display()
print(a2.state)  # Goa
a3.display()
print(a3.state)  # Goa

a1.updateName("sanjeet")
print(a1.name)
print(a1.__dict__)  # {'name': 'sanjeet', 'age': 21, 'salary': 2222222}

a2.ChangeState("kerala")
print(a1.state)  # kerala

a1.state = "maharastra"
print(a1.state)      # maharastra

print(a3.state)      # keralaa
