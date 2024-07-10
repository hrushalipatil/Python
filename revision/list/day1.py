# # retrieve
#
#
# names = ['vrushali', 'aboli', 'apeksha', 'sayali']
# # print(names)
# # print(type(names))   # list
# #
# # for x in range(len(names)):
# #     print(x, '=', names[x])
# #
# # for name in names:
# #     # Printing each name one by one
# #     print(name)
#
# city = "pune"
# # names = ["shraddha","amol","sarika"]
# # for x in range(len(city)):
# #     print(city[x])
#
# for char in city:
#     print(char)
#
# # # update
# #
# # print(names[0])    # vrushali
# #
# #
# # # add
# # # append -- adding at last
# # names.append("riya")
# # print(names)     # ['vrushali', 'aboli', 'apeksha', 'sayali', 'riya']
# #
# #
# # # delete
# # names.pop() #last index remove
# # # ['vrushali', 'aboli', 'sayali', 'riya']
# #
# #
# # names.pop(2)
# # print(names)   #['vrushali', 'aboli', 'sayali']
# #
#
# # ==========================================================
#
# birthyear = [1999, 2000, 2001, 2002]
#
# age = []
#
# for x in birthyear:
#     # print(x)    # 1999,2000,2001,2002
#     x = 2024 - x
#     age.append(x)
#
# print(age)  # [25, 24, 23, 22]
#
# # ============================================================
#
# num = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
#
# above55 = []
#
# for x in num:
#     # print(x)
#     if (x > 55):
#         above55.append(x)
# print(above55)  # [66, 77, 88, 99, 100]
#
# # ============================================================
#
#
# num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even = []
# odd = []
#
# for x in num2:
#     # print(x)
#     if (x % 2 == 0):
#         even.append(x)
#     else:
#         odd.append(x)
#
# print(even)  # [2, 4, 6, 8, 10]
# print(odd)  # [1, 3, 5, 7, 9]

# ============================================================


# Lst = [1, 2, 's', 'f', 3, 5, 'h', 'j', 'l', '8']
# numlst = []
# str1 = []
# for x in Lst:
#     if isinstance(x,int):
#         numlst.append(x)
#     elif isinstance(x,str):
#         str1.append(x)
#
# print(numlst)
# print(str1)


Lst = [1, 2, 's', 'f', 3, 5, 'h', 'j', 'l', 8]
numlst = []
str1 = []

for i in Lst:
    if type(i) == int and i >= 0:
        print(numlst.append(i))
    else:
        print(str1.append(i))
print(numlst)
print(str1)
# [1, 2, 3, 5, 8]
# ['s', 'f', 'h', 'j', 'l']

# =========================================================
#          0   1   2   3   4
numbers = [11, 22, 33, 44, 55]
print(numbers[0])
numbers2 = numbers
numbers2[0] = 111
print(numbers)  # [111, 22, 33, 44, 55]
print(numbers2)  # [111, 22, 33, 44, 55]

# ========================================================
names = ["v", "k", "m"]
names2 = names.copy()
names2[0] = "D"
print(names)  # ['v', 'k', 'm']
print(names2)  # ['D', 'k', 'm']

# ========================================================

dict = {
    "firstName": "vru",
    "lastName": "patil"
}

dict2 = dict
dict2['firstName'] = "vrushali"
print(dict2)  # {'firstName': 'vrushali', 'lastName': 'patil'}
print(dict)  # {'firstName': 'vrushali', 'lastName': 'patil'}

# =========================================================

dict3 = dict.copy()
dict3['firstName'] = "shruti"
print(dict3)  # {'firstName': 'shruti', 'lastName': 'patil'}
print(dict)  # {'firstName': 'vrushali', 'lastName': 'patil'}

# =========================================================


names = ['A', 'B', 'C', 'D']


def ADD(names):
    names.append('E')
    return names


a= ADD(names)
print(a)  # ['A', 'B', 'C', 'D', 'E']


# ========================================================

