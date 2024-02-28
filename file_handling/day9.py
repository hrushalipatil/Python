# import os
#
# record_length = 10
# size = os.path.getsize("cities.bin")  # 30
# n = int(size / record_length)  #  3
# print("Total number of records " + str(n))
#
# with open('cities.bin', 'rb+') as file:
#     name = input("Enter the city to delete: ")  # "pune"
#     name = name + (record_length - len(name)) * " "  # "pune        "
#
#     name = name.encode()  # Encode the input city name
#
#     position = 0
#     found = False
#
#     for x in range(n):
#         file.seek(position)  # Move to the current position
#         data = file.read(10)
#         if data == name:
#             found = True
#             break
#
#         position = position + record_length
#
#     if not found:
#         print("City not found")
#     else:
#         # # Move back to the position of the found record
#         file.seek(position)
#
#         # # Overwrite the record with spaces to effectively "delete" it
#         file.write(record_length * b" ")
#         print("City deleted")


# import os
#
# record_length = 10
# size = os.path.getsize("Fruits.bin")  # 50
# n = int(size / record_length)  # n= 50/10 = 5
#
# print("Total number a fruits record " + str(n))  # Total number a fruits record 5
#
# with open("Fruits.bin", "r+b") as file:
#     fruit_name = input("enter a fruit to delete : ")  # "papaya"
#     fruit_name = fruit_name + (record_length - len(fruit_name)) * " "  # "papaya    "
#
#     fruit_name = fruit_name.encode()  # Encode the input city name
#
#     position = 0
#     found = False
#
#     for i in range(n):
#         file.seek(position)
#         file_read = file.read(10)
#         if file_read == fruit_name:
#             found = True
#             break
#         position = position + record_length
#
#     if not found:
#         print("fruit not found")
#
#     else:
#         file.seek(position)
#         file_read = file.read(10)
#         file.write(record_length * b" ")
#         print("Fruit deleted....")
#         # file.truncate(size - record_length)
#        # file.write(new_city_name)

import os

record_length = 10
file_path = "Fruits.bin"
size = os.path.getsize(file_path)
n = int(size / record_length)

print("Total number of fruit records: " + str(n))

fruit_name = input("Enter a fruit to delete: ")
fruit_name = fruit_name + (record_length - len(fruit_name)) * " "
fruit_name = fruit_name.encode()

with open(file_path, "r+b") as file:
    position = 0
    found = False

    for i in range(n):
        file.seek(position)
        file_read = file.read(record_length)

        if file_read == fruit_name:
            found = True
            break

        position += record_length

    if not found: 
        print("Fruit not found")

    else:
        file.seek(position)
        file.write(record_length * b" ")  # Blank out the record
        print("Fruit marked as deleted.")

print("File size after deletion: " + str(os.path.getsize(file_path)))