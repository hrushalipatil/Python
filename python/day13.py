# #          0         1        2   3
# list = ["vrushali", "patil", 23, 45]
#
# # retrive
# print(list[0])
# print(list[1])
# # update
# list[1] = "wandhare"
# print(list)
#
# list.append("pune")
# print(list)
#
# # delete
# list.pop(2)
# print(list)
#
# # delete
# list.remove("vrushali")
# print(list)

# dictA = {
#     # property:value
#     # key:value
#     "firstName": "vrushali",
#     "lastName": "patil",
#     "age": 23,
#     "rollNo": 45
# }
#
# # print(dictA[0])
# q1 = dictA['firstName']
# print(q1)
#
# # update
# dictA['lastName'] = "dani"
# print(dictA)
#
# # add
# dictA['age'] = 34
# dictA['city'] = "pune"
# print(dictA)
#
# dictA.pop('city')
# print(dictA)
#
# #  C  R  U  D
# # Create
# # Retrieve
# # Update
# # Delete
#
# # type()
vehicle = {
    "color": "red",
    "type": "sedane"
}
# print(vehicle)
# print(type(vehicle))
print(len(vehicle))

# # allows duplicate property ??  - NO
# vehicle = {
#     "color": "red",
#     "type": "sedane",
#     "color": "blue"
# }
# print(vehicle)
#
# # loop
# names = ["VRUSHALI", "KABIR", "SHRUTI"]
#
# for item in range(len(names)):
#     print(names[item])
#
# for item in names:
#     print(item)
#
# dictB = {
#     "rule": 1,
#     "rule1": 2,
#     "rule2": 3
# }
#
# for key in dictB:
#     # print(key)                        # only gives a key
#     # print(dictB[key])                 # only gives a value
#      print(key, dictB[key])             # gives a key and its value
# dictB = {
#
#     "firstName": "VRUSHALI",
#     "lastName": "PATIL",
#     "age": 11,
#     "rollNo": 45
# }
# # for key in dictB:
# #     print(key, dictB[key])

vehicle = {
    "color": "red",
    "regNo": 123
}

# vehicleB = vehicle
# vehicleB['color'] = "blue"
#
# print(vehicleB)   # blue
#
# print(vehicle)    # blue



# # copy()
vehicleC = vehicle.copy()
print(vehicleC)    # {'color': 'red', 'regNo': 123}

print(vehicle)     # {'color': 'red', 'regNo': 123}

vehicleC['color'] = "purple"
print(vehicleC)  # {'color': 'purple', 'regNo': 123}

print(vehicle)   # {'color': 'red', 'regNo': 123}

#
# vehicle = {
#     "color": "red",
#     "regNo": 123,
#     "city": "pune"
# }

# # keys()
# for x in vehicle.keys():
#     print(x)
#
# # values()
# for x in vehicle.values():
#     print(x)
#
# # items()
# for x, y in vehicle.items():
#     print(x, y)
#
# # clear()
# vehicle.clear()
# print(vehicle)

student = {
    "marks": [11, 22, 33, 4],
    "school": "DPS",
    "language": "English"
}

print(student)
# popitem()
student.popitem()
print(student)
# student.popitem()
# print(student)

# #
# # #pop()
student.pop('school')
print(student)

student.update({"age": 25})
print(student)

q1 = student.get("age")
print(q1)
# dict copy
