# #           0         1          2       3
# names = ["vrushali", "patil", "Sanjeet", "kabir"]
# print(names)
# print(names[0])

# # Object - properties and method

# A = len(names)
# print(A)

# # append()

# fruits = ["apple", "mango", "banana"]
# fruits.append("graphs")
# print(fruits)

# reverse()

# fruits.reverse()
# print(fruits)

# # in --------it returns boolean value
# cities = ["pune", "banglore", "nagpur", "mumbai"]
# print("pune" in cities)

# # index
# vegetables = ["carrot", "cabbage", "onion", "cauliflower", "carrot", "onion"]
#
# B = vegetables.index("onion", 4)
# print(B)                              # 5
# C = vegetables.index("onion")
# print(C)                              # 2


# clear
# vegetables.clear()
# print(vegetables)

# numbers = [11, 22, 33]
# numbersB = numbers

# numbersB[0] = 111
# print(numbers)           # 111,22,33
# print(numbersB)           #111,22,33

# numbersC = numbersB.copy()
# numbersC[1] = 44444
#
# print(numbersC)
# print(numbersB)

# names = ["shivani","ram","sham","layman"]
# print("Shivani" in names)


# pop --------cannot store by element
# flowers = ["rose", "lily", "jasmine", "marigold","lotus"]
# E = flowers.pop()                                # remove default last element
# print(E)
# print(flowers)
#
# F = flowers.pop(2)                               # remove jasmine
# print(F)

# # remove --------cannot store by index
# flowers.remove("rose")
# print(flowers)


# #sort----- ascending order A to Z and a to z
# country = ["india", "pakistan", "srilanka", "bangladesh"]
# country.sort()
# print(country)

# num = [11, 22, 34, 56, 22, 112, 31, 13]
# num.sort()
# print(num)

# # extend-------- extend list by appending element
X = [11, 22, 33]
Y = [44, 55, 66, 55, 77, 55]

# X.extend(Y)
# print(X)                   # [11,22,33,44,55,66,55,77,55]

# Y.extend(X)
# print(Y)                    # [44,55,66,55,77,55,11,22,33]

# # update
# X[2] = 333
# print(X)

# #count-------- return number in occurrence of value
# Z = Y.count(55)
# print(Z)

# #insert : ------- 0 is a index and 555 is a value
#           ------- add element according to index which you give
#           ------- insert expected two argument
# X.insert( 555)
# print(X)

# # for x in range(startPosition,endPosition(not included)):
# #     print(x)

# for x in range(10):
#     print(x)          # 0,1,2,3,4,5,6,7,8,9

# for x in range(1, 10):
#     print(x)            # 1,2,3,4,5,6,7,8,9

# for x in range(1, 20, 2):
#     print(x)              # 1,3,5,7,9,11,13,15,17,19   -----start,end,step

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1.

# for x in range(len(b)):
#     #print(x)
#     print(b[x])

# 2.

# for x in b:
#     print(x)
