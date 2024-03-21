
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