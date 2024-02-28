# pickle
import pickle
class Student:
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollnumber = rollno
        self.age = age

    def display(self):
        print(f"My name is {self.name}")
        print(f"My roll number is {self.rollnumber}")
        print(f"My age is {self.age}")


# Create instances (objects) of the Student class
X = Student("Vrushali", 1, 24)
Y = Student("Kabir", 2, 27)
Z = Student("Shruti", 3, 27)

# Create a list of student objects
A = [X, Y, Z]
#
# # Display the details of each student
# for item in A:
#     item.display()

# we save the list of A objects to a file using pickle
with open('students.pkl', 'wb') as file:
    pickle.dump(A, file)


# dump
# Load the student objects from the file using pickle
with open('students.pkl', 'rb') as file:
    loaded_students = pickle.load(file)

# load
# Display the details of each loaded student
for student in loaded_students:
    student.display()


# pickle
# To verify that the data is being loaded correctly, you can modify the code to print the loaded objects.

#obj   ------ file ----- dump ===> pickle
#file  ------ obj  ----- load ===> pickle