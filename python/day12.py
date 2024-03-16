
# ******************** List ***************************
#       firstName   lastName  phone-number
info = ["vrushali", "patil",  8530420563,   23, 56]
print(info)
print(type(info))                          # list

# retrieve
print(info[0])
print(info[1])
print(info[2])

# update
info[1] = "wandhare"
print(info)

# append
info.append("kabir")
print(info)

# int
# float
# boolean
# List
# String
# dictionary

# ******************** dict ***************************

info2 = {
    # prop:value
    # key:value
    "first_Name": "vrushali",
    "last_Name": "patil",
    "age": 28,
    "rollNo": 56,
    "mobileNumber": 8530420563,
    "age": 45

}
print(info2)
print(type(info2))                 # dict


# dictionary stores the value by index???  No
# dictionary stores duplicate key - pair ?? NO

# retrieve
print(info2['first_Name'])
print(info2['age'])

# update
info2['first_Name'] = "tanmay"
print(info2)

# add
info2['city'] = "pune"
print(info2)

# delete
# info2.pop("age")
# print(info2)

print(len(info2))

# C  - create
# R  - retrieve
# U  - update
# D  -  delete

vehicle = {
    "color": "red",
    "type": "sedane"
}

# retrive
print(vehicle['color'])

# update
vehicle['color'] = "blue"
print(vehicle)

# add
vehicle['reNo'] = 123
print(vehicle)

# delete
vehicle.pop('color')
print(vehicle)

A = len(vehicle)
print(A)
