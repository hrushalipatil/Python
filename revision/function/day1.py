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
print(upperName)  # ['VRUSHALI', 'KABIR', 'SAYALI', 'SUBHUTI']

# program 5

names2 = ["Aboli", "sayali", "snehal", "falguni"]
# 1.endswith i
F = [i for i in names2 if i.endswith("i")]
print(F)  # ['Aboli', 'sayali', 'falguni']

# 2.endwith i and do upper case
G = [i.upper() for i in names2 if i.endswith("i")]
print(G)  # ['ABOLI', 'SAYALI', 'FALGUNI']

# 3. string first character
H = [i[0] for i in names]
print(H)  # ['v', 'k', 's', 's']

J = [i[0].upper() for i in names]
print(J)  # ['V', 'K', 'S', 'S']

info = [
    {
        "firstName": "Vrushali",
        "lastName": "Patil",
        "age": 23,
        "vehicle": True
    },
    {
        "firstName": "Sayali",
        "lastName": "Jogi",
        "age": 4,
        "vehicle": True
    },
    {
        "firstName": "Kabir",
        "lastName": "Wandhare",
        "age": 19,
        "vehicle": False

    },

    {
        "firstName": "tavish",
        "lastName": "anade",
        "age": 20,
        "vehicle": True
    }

]

L = [i['firstName'] for i in info]
print(L)  # ['Vrushali', 'Sayali', 'Kabir', 'tavish']




# even odd list find
even_odd =[11,22,33,44,55,66,77,88]

N= ["even" if i%2==0 else "odd" for i in even_odd]
print(N)      # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

info2 = [
    {
        "firstName": "Vrushali",
        "lastName": "Patil",
        "age": 23,
        "vehicle": True
    },
    {
        "firstName": "Sayali",
        "lastName": "Jogi",
        "age": 4,
        "vehicle": True
    },
    {
        "firstName": "Kabir",
        "lastName": "Wandhare",
        "age": 19,
        "vehicle": False

    },

    {
        "firstName": "tavish",
        "lastName": "anade",
        "age": 20,
        "vehicle": True
    }

]

# 1.

# vehicle value key is false  print their firstname
M = [i["firstName"] for i in info2 if not i['vehicle']]
print(M)    # ['Kabir']


# 2.

N= [i['firstName'] for i in info2 if i["vehicle"]==True and i["age"]>=18]
print(N)   # ['Vrushali', 'tavish']


# 3.

O = [i["firstName"] for i in info2 if i["vehicle"]==True ]
print(O)   # ['Vrushali', 'Sayali', 'tavish']


P=["can Drive" if i["age"]>=18 else "cannot drive" for i in info2]
print(P)    # ['can Drive', 'cannot drive', 'can Drive', 'can Drive']

# =============================================================================




