# # string
# str = "vrushali"
# print(str)  # vrushali
#
# # list
# names = ['vrushali', 'kabir', 'sayali']
#
# print(names)
# print(type(names))  # list
#
# # object
#
# obj = {
#     'Name': "vrushali",
#     'age': 24,
# }
#
# print(obj)
# print(type(obj))  # dict
#
# # --------------------------------------------------------
#
#
# fruit1 = ['apple', 'banana', 'graphs']
#
# fruit2 = ['apple', 'banana', 'lichy']
#
# fruit1[0] = "pineapple"
# print(fruit1)  # ['pineapple', 'banana', 'graphs']
#
# fruit2[1] = "kiwi"
# print(fruit2)  # ['apple', 'kiwi', 'lichy']
#
# # ------------------------------------------------------------
#
#
# # does  tuple stores the value by index?? yes
#
# # donest update the value
#
# tuple1 = ('a', 'b', 'c')
#
# print(tuple1)
# print(type(tuple1))  # tuple
# print(tuple1[0])  # a
#
# # for with range
#
# # for with range
# for i in range(3):
#     print(i)
#     print(tuple1[i])  # a b c
#
# # for without
# # for i in tuple1:
# #     print(i)          # a b c
#
# # while loop
#
# T = (11, 22, 33, 44, 55)
#
# i = 0
# while (i < 5):
#     print(T[i])
#     i = i + 1
#
# T1 = (12, 13)
#
# print(type(T1))  # tuple
#
# # T1[0] = 66     # TypeError: 'tuple' object does not support item assignment
# # print(T1)
#
#
# T2 = (11, 22, 33, 44, 55, 66, 44, 44)
# print(T2)  # (11, 22, 33, 44, 55, 66, 44, 44)
#
# # a,b,c,d,e = T2
#
#
# # print(a)   # 11
# # print(b)   # 22
# # print(c)   # 33
# # print(d)   # 44
# # print(e)   # 55
#
# T3 = T2.count(44)
# print(T3)  # 3
#
# T4 = T2.index(22)
# print(T4)  # 1
#
# print(33 in T2)  # true
#
# # how to create tuple with constructor
#
# # Create a tuple from a list
# listA = [1, 2, 3]
# tupleA = tuple(listA)
# print(tupleA)  # Output: (1, 2, 3)
#
# # Create a tuple from a string
# string = "hello"
# tupleA = tuple(string)
# print(tupleA)  # Output: ('h', 'e', 'l', 'l', 'o')
#
# # Create a tuple directly
# my_tuple = tuple([1, 2, 3])
# print(my_tuple)  # Output: (1, 2, 3)
#
# A = (1, 2, 3, 4, 5, 6)
#
# B = list(A)
# print(B)  # [1, 2, 3, 4, 5, 6]
#
# B.append(7)
# print(B)  # [1, 2, 3, 4, 5, 6, 7]
#
# # Tuple
#
# C = tuple(B)
#
# print(C)  # (1, 2, 3, 4, 5, 6, 7)


# ---------------------------------------------------------------------------------


num = [11, 22, 33, 44, 55, 66, 33, 44, 22]
print(num)  # [11, 22, 33, 44, 55, 66, 33, 44, 22]

print(num[1])      # 22

info = {
    "firstName":"ninad",
    "lastName":"dani",
    "rollNo":"1211",
    "age":"12",
    "age": "123"     # age ki value update hongi
}
print(info)



#
setB = {11,22,33,44,44,55,55}
print(setB)     # {33, 22, 55, 11, 44}

