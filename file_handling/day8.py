import os.path

# city replace
#
# import os
# record_length = 10
# size = os.path.getsize("cities.bin")
# n = int(size / record_length)
#
# with open("cities.bin", "r+b") as file:
#     old_city_name = input("please enter a city to replace :")
#     old_city_name = old_city_name.encode()  # goa
#
#     new_city_name = input("please enter the new city ")  # ujjain
#     new_city_name = new_city_name + (record_length - len(new_city_name)) * " "  # "ujjain    "
#
#     new_city_name = new_city_name.encode()
#
#     position = 0
#     found = False
#
#     for i in range(n):
#         file.seek(position)
#
#         file_read = file.read(10) #record_length=10
#
#         if old_city_name in file_read:
#             found = True
#  # Update the position to move to the next record
#             file.seek(-10,1)
#             file.write(new_city_name)
#  # Update the position to move to the next record
#         position = position + record_length
#
#     if not found:
#         print("city not found ")

# import os
#
record_length = 10
size = os.path.getsize("Fruits.bin")
n = int(size / record_length)

with open("Fruits.bin", "r+b") as file:
    old_fruitName = input("enter a fruit to replace : ")
    old_fruitName = old_fruitName.encode()

    new_fruitName = input("enter a new fruit :")
    new_fruitName = new_fruitName + (record_length - len(new_fruitName)) * " "
    new_fruitName = new_fruitName.encode()

    position = 0
    found = False

    for i in range(n):
        file.seek(position)  # 0 ==> start
        # Read the next record (10 bytes) from the file
        file_read = file.read(10)

        if old_fruitName in file_read:
            found = True
            # Move the file pointer back to the start of the current record
            file.seek(-10, 1)
            # Write the new city name to replace the old city name
            file.write(new_fruitName)
        # Update the position to move to the next record
        position = position + record_length  # 0+10==> 10 ==> then next 20
    if not found:
        print("fruit not found ")
