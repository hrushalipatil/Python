names = ["vrushali", "kabir", "shruti", "ashivi"]
print(names)  # ['vrushali', 'kabir', 'shruti', 'ashivi']

print(type(names))  # list

cities = ('pune', 'nagpur')
print(type(cities))  # <class 'tuple'>

cities = 'mumbai'
print(type(cities))  # str

cities = 'mumbai',
print(type(cities))  # tuple

# ====================================================

# 'tuple' object does not support item assignment -- update nhi akr sakte

# # cities[0] = "nagpur"
# print(cities[0])

cities = ("nagpur", "nanded", 'wardha')
print(cities)

# =====================================================

cities = ("nagpur", "nanded", 'wardha')
# 1.
for x in cities:
    print(x)

# 2.
for x in range(len(cities)):
    print(x)  # 1 2 3
    print(cities[x])  # nagpur,nanded,wardha

# 3.
x = 0
while (x < len(cities)):
    print(cities[x])
    x = x + 1

# 4.
languages = ("marathi", "hindi", "sankrit", "telgu", "punjabi", "english")
a, b, c, e, d, f = languages
print(a)  # marathi

# 5.
city = ["pune", "mumbai", "bangalore"]


def ADDCITY(X):
    X.append("wardha")
    return tuple(X)


a, b, c, d = ADDCITY(city)

print(a)  # pune
print(d)  # wardha

# 6.
k = (11, 22, 33, 11)
k = list(k)  # [11,22,33]
k.append(44)
k = tuple(k)
print(k)  # (11, 22, 33, 11, 44)

e = k.count(11)
print(e)  # 2

f = k.index(22)
print(f)  # 1
