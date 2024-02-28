class Employee:
    # constructor
    def __init__(self, nm, sal, ag):
        # attributes
        self.name = nm
        self.salary = sal
        self.age = ag

        # methods

    def display(self):  # this is a instance method . (self ---object e1 ka reference as a parameter)
        print(f"my name is  {self.name},my salary is {self.salary},my age is{self.age}")

    def change_data(self):
        self.name = "name"
        self.salary = 2544444
        self.age = 100


e1 = Employee("vrushali", 24000, 21)
e2 = Employee("sanjeet", 26000, 25)

# accessing attributes outside the class
print(e1.salary)
print(e2.salary)

e1.display()
e2.display()

# update
e1.name = "shruti"
print(e1.name)
e1.display()  # my name is  shruti,my salary is 24000,my age is21

# add
e1.marks = 30
print(e1.__dict__)  # {'name': 'shruti', 'salary': 24000, 'age': 21, 'marks': 30}

# retrive
print(e1.name)  # shruti
print(e1.age)  # 21
print(e1.salary)  # 24000
# delete
# del e2.name
# print(e2.name)
# e2.display()

e1.change_data()
print(e1.__dict__)

# ---------------------------------------------------------------------------

# class Person:
#     # properties
#     first_Name = "amol"
#     last_Name = "rao"
#     age = 12
#     rollNo = 44
#
#     # attribute
#     def walk(self):
#         print("I am walking")
#     def talk(self):
#         print("I am talking")
#
# amol = Person()
# print(amol.first_Name)
# print(amol.last_Name)
# print(amol.age)
# print(amol.rollNo)
# amol.talk()
# amol.walk()
#
# chinmay = Person()
# # retrive
# print(chinmay.first_Name)
# print(chinmay.last_Name)
# print(chinmay.age)
# print(chinmay.rollNo)
#
# #update
# chinmay.first_Name = "chinmay"
# chinmay.last_Name = "deshpande"
# chinmay.age = 12
# chinmay.rollNo = 77
# chinmay.city = "pune"
#
# print(chinmay.first_Name)
# print(chinmay.last_Name)
# print(chinmay.age)
# print(chinmay.rollNo)
# print(chinmay.city)
#
# del chinmay.city
# chinmay.talk()
# chinmay.walk()
# #print(chinmay.city)
#
#
# print(amol.first_Name)
