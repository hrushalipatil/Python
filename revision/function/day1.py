# list compression

# [expression : loop : condition ]


# program 1
# table of 2
A = [1, 2, 3, 4, 5, 6]

B = [i * 2 for i in A]
print(B)  # [2, 4, 6, 8, 10, 12]

# program 2
# even
C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = [i for i in C if i % 2 == 0]
print(D)  # [2, 4, 6, 8, 10]

# program 3
# odd
E = [i for i in C if i % 2 != 0]
print(E)  # [1, 3, 5, 7, 9]

# program 4
# make every character to upper()

names = ["vrushali", "kabir", "sayali", "subhuti"]

upperName = [i.upper() for i in names]
print(upperName)      # ['VRUSHALI', 'KABIR', 'SAYALI', 'SUBHUTI']


# program 5


