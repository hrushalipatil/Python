


# x = 10
# print(x)

#           0         1         2       3      4
# names = ["vrushali","kabir","darsh","sanjeet","shruti"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

# program 2

fruits = ["apple", "mango", "banana", "grapes"]
# whether the element is present or not =======> true or false

# in operator

# print("apple" in fruits)
# print("Apple" in fruits)

# Program 3
# if "apple" in fruits:
#     print("Fruit available")
# else:
#     print("Fruit not available")

# program 4

# update the element for list
#            0       1          2          3          4
cities = ["pune", "mumbai", "banglore", "kolkata", "chennai"]
# print(cities[1])
# cities[1] = "nagpur"
# print(cities)


# looping through the list using range()
#                 0          1        2       3
vegetables = ["brinjal", "tomato", "potato", "onion"]

# end position not inclusive
# range(10)  # 0,1,2,3,4,5,6,7,8,9
# range(1,10) # 1,2,3,4,5,6,7,8,9
# range(1,10,2) # 1,3,5,7,9
# for i in range(10):
#     print(i)
# for i in range(1, 10):
#     print(i)
# for i in range(1, 10, 2):
#     print(i)

# print(len(vegetables))
# x = len(vegetables)
# print(x)
#
# for i in range(len(vegetables)):
#     # print(i)                # index
#     print(vegetables[i])      #element

# for i in vegetables:
#     print(i)
#
# print("potato" in vegetables)   # true

# program 5

#             0         1          2        3          4
country = ["india", "pakistan", "srilanka", "china", "usa"]
# print(country)                       # ---   print list   ['india', 'pakistan', 'srilanka', 'china', 'usa']
# q = len(country)                       # 5
# print(q)
# 1.
# for x in range(len(country)):
#      # print(x)
#     print(country[x])

# 2.
# for i in country:
#     print(i)


# program 6
flowers = ["rose", "lotus", "sunflower", "marrygold"]

for x in flowers:
    print(x)

# ========in range method ========

for i in range(len(flowers)):
    print(i)
    print(flowers[i])

# program 7
state = ["MH", "RJ", "MP", "UP", "UK"]
for x in range(len(state)):
    if x != 2:
        print(state[x])


