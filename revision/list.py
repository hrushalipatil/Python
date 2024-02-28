names = ["vrushali", "kabir", "sayali"]

# retrive
print(names[0])
print(names[1])
print(names[2])

# update
names[1] = "kabir"
print(names)

# add
names.append("aboli")
print(names)  # add in last

# insert
names.insert(0, "zoya")
print(names)  # ['zoya', 'vrushali', 'kabir', 'sayali', 'aboli']

# pop
names.pop(1)
print(names)  # remove by index

# remove
names.remove("zoya")
print(names)  # remove by name

# loop
#
# for item in names:
#     print(item)

#     sayali chhod kar list as it is print karo

for item in names:
    if item != "sayali":
        print(item)

# 1
new_list = []
for item in names:
    if item != "sayali":
        new_list.append(item)

print(new_list)

#  list comprehension

names = ["vrushali", "kabir", "sayali"]

new_list = [item for item in names if item != "sayali"]

print(new_list)

