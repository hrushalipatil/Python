

# 4 nov 2023
# program 1
def addition(x, y):
    return x + y


A = addition(10, 10)
print(A)  # 20

# LAMBDA
addition = lambda a, b: a + b
B = addition(10, 100)
print(B)  # 110

# program 2

year = [1999, 1998, 1997, 1996]
age = []
print(year)  # [1999, 1998, 1997, 1996]

for item in year:
    list_age = 2023 - item
    age.append(list_age)
print(age)  # [24, 25, 26, 27]

# LAMBDA
age_list = lambda age: 2023 - age
X = list(map(age_list, year))
print(X)  # [24, 25, 26, 27]

# -------------------------------------------------------
# revision
# listA = [11, 12, 13, 14, 15, 16, 17, 18]
# answer = list(map(lambda x: x + 2, listA))
# print(answer)  # [13, 14, 15, 16, 17, 18, 19, 20]

A = [12, 24, 36, 48, 60]
answer = list(map(lambda x: x - 1, A))
print(answer)  # [11, 23, 35, 47, 59]

B = [1, 2, 3, 4, 5, 6, 7, 8]
mul = list(map(lambda x: x * 2, B))
print(mul)  # [2, 4, 6, 8, 10, 12, 14, 16]

# filter
marks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
above10 = []
for i in marks:
    if i > 12:
        above10.append(i)
print(above10)

answer = list(filter(lambda x: x > 40, marks))
print(answer)

# reduce
s = [11, 111, 1111, 1111]
# total = 0
# for i in s:
#     total = total+i
# print(total)

import functools

# from functools import reduce
print(functools.reduce(lambda acc, ans: acc + ans, s))

t = [1, 2, 3, 4, 5]
print(functools.reduce(lambda acc, ans: ans * acc, t, 2))

l = [-11, 11, -12, 12, -13, 13]

positive = list(filter(lambda ptv: ptv > 0, l))
print(positive)  # [11, 12, 13]

negative = list(filter(lambda ntv: ntv < 0, l))
print(negative)  # [-11, -12, -13]



#
