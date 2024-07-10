# 1
# f = open("mytext.txt" ,'w')
# str = input("enter a fruits : ")
# f.write(str)
# f.close()

# 2
# f=open("mytext.txt",'r')
# str = f.read()
# print(str)
# f.close()

# 3
# f=open("mytext1.txt",'w')
#
# print('type @ to stop data writing')
# while str != "@":
#     str = input("enter a names : ")
#     if str != '@':
#         f.write(str + "\n")
# f.close()


# 4
# f = open("mytext1.txt", "r")
# #1
# str=f.read()
# print(str)
# f.close()
# #2
# List = f.readlines()
# for item in List:
#     print(item)
# f.close()

# 5
# #copy image file to new file
# f1 = open("sunset.png", "rb")
# f2 = open("newsunset.png", "wb")
#
# bytes = f1.read()
 # f2.write(bytes)
# f2.close()
# f1.close()
#
# # open with file -----we dont need to close this file it will close automatically
#
# with open("mytext1.txt","r") as file:
#     str = file.read()
#     print(str)
#
# with open("mytext2.txt","w") as file:
#     str = input("Enter the sentence " + '\n')
#     file.write(str)


# import os
# import sys
#
# f = input("enter a fileName :")
# if os.path.isfile(f):
#     f1 = open(f, " r")
# else:
#     print(f, " does not exist")
#
#     sys.exit()
# str = f1.read()
#
# print(str)
# # f.close()
# f1.close()


# ---------------------------------------------------------------------------

recordlength = 10
# with open("flowers.bin", "wb") as file:
#
#     n = int(input("Enter a number of flowers do you want write : "))
#
#     for item in range(n):
#         flower_names = input("Enter a flowers :")
#
#         flower_names_length = len(flower_names)
#
#         flower_names = flower_names + (recordlength - flower_names_length) * " "
#
#         flower_names_bytes = flower_names.encode()
#
#         file.write(flower_names_bytes)

with open("flowers.bin", "rb") as file:
    n = int(input("Enter a number which you want to read "))  # 3
    #                                   1234567910|12345678910|12345678910|12345678910|12345678910
    #                                   sunflower  lily        jasmine     rose        lotus

    file.seek(recordlength * (n - 1))  # 10 * 3-1 ==> 10*2 ==> 20
    str = file.read(recordlength)

    str = str.decode()
    print(str)
