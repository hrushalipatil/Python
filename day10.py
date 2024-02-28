# capitalize

# first_Name = "vrushali"
# P = first_Name.capitalize()
# print(P)

# lower()

# city = "PUNE"
# Q = city.lower()
# print(Q)

# upper()
# color = "pink"
# R = color.upper()
# print(R)

# strip()

# color1 = " Green"
# S = len(color1)
# print(S)                      # 7 -----space add kar k 7 aayaa

# T = color1.strip()
# print(len(T))                 # 5 ------- in strip only count charter
# print(T)                      # Green
#
# U = color1.lstrip()
# print(U)
# # print(len(U))
# U = color1.rstrip()
# print(U)
# # print(len(U))

# split() ------- split return as a list give it as a string in split we cant define as list
# info = "vrushali patil 7709192441"
# V = info.split(" ")
# print(V)
# print(type(V))


# .join()
# names = ["vrushali","sanjeet", "kabir", "shruti", "akash"]
# W= " *** ".join(names)
# print(W)

# replace
# info2 = "I am learning javascript"
# X = info2.replace("javascript", "python")
# print(X)

info3 = "vrushali kabir"
A1 = info3.startswith("v")        #true
A2 = info3.startswith("vru")      #true
A3 = info3.endswith("li")         #false
A4 = info3.endswith("ir")         #true
print(A1)
print(A2)
print(A3)
print(A4)
