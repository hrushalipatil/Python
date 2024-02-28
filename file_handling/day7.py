# # city hai toh true nhi hai  to false :
#
# import os
#
# record_length = 10
# size = os.path.getsize("cities.bin")
# n = int(size / record_length)
# print("Total number of record " + str(n))
#
# with open("cities.bin", "rb") as file:
#     name = input("Enter the city ")
#     name = name + (record_length - len(name)) * " "
#     name = name.encode()
#
#     position = 0
#     found = False
#
#     for i in range(n):
#         file.seek(position)
#         file_read = file.read(10)
#         if file_read == name:
#             found = True
#             break
#         position = position + record_length
# if not found:
#     print("city not found")
#
# else:
#     print("city found ")


# Fruits:

import os
record_length =10
size = os.path.getsize("Fruits.bin")
n = int(size/record_length) # 50/10

print("Total number of record :" + str(n)) # 5

with open("Fruits.bin","rb") as file:
    name = input("Enter the fruit :")
    name = name + (record_length - len(name)) * " "  # banana + (10- len(banana)) * " "
                                                  #  banana  + (10 -6) * ""
                                                  #  banana  + 4 * " "
                                                  #  "banana    "
    name = name.encode()

    position =0
    Found = False
    for i in range(n):
        file.seek(position)
        file_read = file.read(10)
        if file_read == name:
            Found = True
            break
        position = position + record_length
if not Found:
    print("fruit not found")

else:
    print("fruit found ")