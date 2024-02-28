# 6 nov -monday

# list :


# =========list comprehension==============

# [expression for item in iteration if condition]

# program 1:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = [expression for item in iterable]

square = [item * item for item in list]

print(square)

# program 2:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

add2 = [item + 2 for item in list1]

print(add2)

# program 3:
list2 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

positive = [item for item in list2 if item > 0]
print(positive)  # [1, 3, 5, 7, 9]

negative = [item for item in list2 if item < 0]
print(negative)  # [-2, -4, -6, -8, -10]

# program 4:

names = ["vrushali", "kabir", "shruti", "addy", "saili"]

uppercase = [item.upper() for item in names]
print(uppercase)

lowercase = [item.lower() for item in names]
print(lowercase)

startwith = [item for item in names if item.startswith("s")]
print(startwith)  # ['shruti', 'saili']

# program 5:
string = "I am learning javascript"  # output:['I', 'a', 'l', 'j']

listwords = string.split(" ")

print(listwords)  # ['I', 'am', 'learning', 'javascript']

listfirstletter = [item[0] for item in listwords]

print(listfirstletter)  # ['I', 'a', 'l', 'j']

# program 6:

# table of 2

table_of_two =[item*2 for item in range(1,11)]
print(table_of_two)

table3 = [item*3 for item in range(1,11)]
print(table3) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# table of 5
# by range function:
# table=5
# for i in range(1,11):
#       print(table*i)

tableA=[item*23 for item in range(1,11)]
print(tableA)