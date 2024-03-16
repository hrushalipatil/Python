# ********************** set ************************

# # program 1

# empty_set = set()
# print(empty_set)
# print(type(empty_set))                    #set

# # program 2
# my_set = set([1,3,4,5,6,4,5,6])
# print(my_set)                              # set dosen't store a duplicate value

# # program 3
# my_setB = {1, 2, 36, 7, 8, 9, 44}
# print(my_setB)                               # {1, 2, 36, 7, 8, 9, 44}
# print(type(my_setB))                         # set

# # program 4
# print(len(my_setB))                           # 7

# #program 5
# #add()

# mySetC = set()
# print(type(mySetC))                           # set

# mySetC.add(12)
# mySetC.add(13)
# mySetC.add(14)
# mySetC.add(15)
# mySetC.add(13)

# print(mySetC)                               # {12, 13, 14, 15}

# #update()

# mySetC.update([16, 17, 18, 19, 20])
# print(mySetC)                                  # {16, 17, 18, 19, 20}


# # removing the element

setE = {"vrushali","shruti","anmol","pooja","darsh","kabir"}

# #remove

# setE.remove("pooja")
# print(setE)


# # discard()

# setE.discard('anmol')
# print(setE)                   # {'vrushali', 'pooja', 'darsh', 'shruti', 'kabir'}

# A= setE.discard('darsh')
# print(setE)
# print(A)                        # {'vrushali', 'pooja', 'shruti', 'kabir'}

# print(setE)
# setE.pop()
# print(setE)

# # Set does not stores the value by index
# setG = {111,222,333,444}
# print(setG[0])

# # clear()
# setH = {11,22,33,44,55,66,77,88,99,100}
# print(setH)
# setH.clear()
# print(setH)

# # remove()
setK = {"aachal","rutuja","vrushali","kabir"}
# setS = setK
# setS.remove("rutuja")
# # print(setK)                                        # {'vrushali', 'kabir', 'aachal'}
# # print(setS)                                        # {'aachal', 'kabir', 'vrushali'}

# # copy()
# setKb = setK.copy()
# setKb.remove("aachal")
# print(setKb)                                           # {'rutuja', 'kabir', 'vrushali'}
# print(setK)                                            # {'aachal', 'rutuja', 'kabir', 'vrushali'}


# setG = set([1,2,3])
# print(setG)                                            # {1, 2, 3}
