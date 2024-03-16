
# setA = {11,22,33}
# setB  = set([11,22,33])
# setC = set()
# # for item in setB:
# #     print(item)                         #33 11 22

# for item in setC:
#     print(item) #blank

# for item in setA:
#     print(item)                          #33 11 22

# # remove()

# setA = {11 ,22 ,33}
# setA.remove(11)
# # print(setA)                    # {33,22 }

# discard()
# setA.discard(33)
# print(setA)                     #{11,22}

# pop()
# setA.pop()
# print(setA)                       # remove  random element automatically

#
# setName = {"aaa","bbb","ccc","ddd","eee"}
# setNameB = setName.copy()
# setNameB.pop()
# print(setNameB)
# print(setName)

setCities = {"pune" ,"mumbai" ,"banglore" ,"chennai"}
# setCities.add("wardha")
# print(setCities)

# setCities.clear()
# print(setCities)

# setA = {"chinmay","sarika","ram"}
# setB = {"komal","abhisha","shraddha"}
# setD = setA.union(setB)
# print(setD)
#
# setA = {"chinmay","sarika","ram"}
# setB = {"komal","abhisha","ram"}
#
# # setC = setA.intersection(setB)
# # print(setC)
#
# # setA.intersection_update(setB)
# # print(setA)
#
#
# setA = {"chinmay","sarika","ram"}
# setB = {"komal","abhisha","ram"}
#
# # setC = setA.difference(setB)
# # print(setC)
# # setB.difference_update(setA)
# # print(setB)
#
# setA = {"chinmay","sarika","ram"}
# setB = {"komal","abhisha","ram"}
#
# # setC  = setA.symmetric_difference(setB)
# # print(setC)
# # setA.symmetric_difference_update(setB)
# # print(setA)
#
#
# # setA = {"chinmay","sarika","ram"}
# # setB = {"komal","abhisha","ram"}
# # q = setA.isdisjoint(setB)
# # print(q)
#
# # setA = {11,22,33}
# # setB = {22,33}
# # q2 = setA.issuperset(setB)
# # print(q2)
# # q3 = setB.issubset(setA)
# # print(q3)
#
# # setNames = {"chinmay","sarika"}
# # setNames.update(["kajal","sarika"])
# # print(setNames)
#
# setA = {11,22,33}
# # setB = setA
# # setB.update({44,55})
# # print(setA)
# # print(setB)
#
# # setB = setA.copy()
# # setB.update({33,44})
# # print(setB)
# # print(setA)


# union()
# setA = {1,2,3}
# setB = {4,5,6}
# setC = setA.union(setB)
# print(setC)
# print(type(setC))
#
# setE = {11,22,33,44,55}
# setF = {44,55,66,77,88,99,100}
#
# # intersection()
# setG = setE.intersection(setF)
# print(setF)
# print(setE)
# print(setG)
#
#
# #intersection_update()
# SetAA = {1,2,3,4}
# setBB = {3,4,5,6}
# SetAA.intersection_update(setBB)
# print(SetAA)
# setBB.intersection_update(SetAA)
# print(setBB)
#
#
# #difference()
# SetAA = {1,2,3,4}
# setBB = {3,4,5,6}
#
# setEE = SetAA.difference(setBB)
# setFF = SetBB.difference(SetAA)
# print(setFF)

#difference_update()


# SetAA = {1,2,3,4}
# setBB = {3,4,5,6}
#
# SetAA.difference_update(setBB)
# print(SetAA)
#
# setBB.difference_update(SetAA)
# print(setBB)
#
#
# SetAA = {1,2,3,4}
# setBB = {3,4,5,6}
#
# setQ = {11,22,33}
# setS = {11,22}
#
# q1 = setS.issubset(setQ)
# q2 = setQ.issubset(setS)
# print(q1)
# print(q2)
#
# q3 = setQ.issuperset(setS)
# print(q3)
#
# setQ = {11,111,33}
# setS = {11,222222,44444,55}
#
# # setW = setQ.symmetric_difference(setS)
# # print(setW)
#
# # setQ.symmetric_difference_update(setS)
# # print(setQ)
#
# q1 = setQ.isdisjoint(setS)
# print(q1)
