# # birthyear = [1999,1998,1997,1996]
# #
# # age=[]
# #
# # for i in birthyear:
# #     x=2024-i
# #     age.append(x)
# # print(age)    # [25, 26, 27, 28]
# #
# # f= lambda x:2024-x
# # f(birthyear[0])
#
#
#
# # program 1
# lst = [1989,1990,1991,1992]
# ages = []
#
# for i in lst:
#     x = 2024 - i
#     ages.append(x)
# print(ages)
#
# a = list(map(lambda x:2024-x,lst))
# print(a)
# print([2024 - i for i in lst])
#
# # program 2
# f = lambda x : 2024 - x
# f(lst[0])
#
# # program3
# names = ["chinmay", "sarika", "kajal", "ninad"]
# above5 = []
# for x in names:
#     if len(x) > 5:
#         above5.append(x)
# print(above5)
#
# print([x for x in names if len(x) > 5])
# e = list(filter(lambda x: len(x) > 5, names))
# print(e)
#
# transactions = []
# d = [2, 3, 4, -55, -66, 77, 44, 555]
# for x in d:
#     if x < 0:
#         # print("withdrawl")
#         transactions.append("withdraw")
#     else:
#         transactions.append("deposit")
# print(transactions)
# print(["withdrawl" if x < 0 else "deposit" for x in d])
# print(list(filter(lambda x: x > 0, d)))
# print(list(filter(lambda x: x < 0, d)))

A = [1999, 1998, 1997, 1996]

age = []

for i in A:
    B = 2024 - i
    age.append(B)
print(age)  # [25, 26, 27, 28]

C = list(map(lambda x: 2024 - x, A))
print(C)

D = lambda x: 2024 - x
D(A[0])

names = ['aboli', 'apeksha', 'snehal', 'sayali']
above5 = []

for i in names:
    if len(i) > 5:
        above5.append(i)

print(above5)  # ['apeksha', 'snehal', 'sayali']

F = [i for i in names if len(i) > 5]
print(F)

G = list(map(lambda x: len(x) > 5, names))
print(G)  # [False, True, True, True]

H = list(filter(lambda x: len(x) > 5, names))
print(H)  # ['apeksha', 'snehal', 'sayali']
print(H)  # ['apeksha', 'snehal', 'sayali']
