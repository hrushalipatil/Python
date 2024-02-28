# # write
#
# f = open("mytext3.txt", "w")
# str = (input("Enter a names"))
# f.write(str)
# f.close()
#
# # read
#
# f1 = open("mytext3.txt", "r")
# str = f1.read()
# print(str)
# f1.close()
#
# # append
#
# f2 = open("mytext4.txt", "a")
# print("type @ when you writing")
# userInput = None
# while (userInput != "@"):
#     userInput = input("Enter a names :")
#     if (userInput != "@"):
#         f2.write(userInput + "\n")
# f2.close()
#
# # Readline by line
# f3 = open("mytext4.txt", "r")
# list = f3.readlines()
# print(list)
# for item in list:
#     print(item)
# f3.close()
#
# # r - read
# # w - write
# # a - append


# a+ - append + read
f4 = open('mytext5.txt', 'a+')
print('@ to stop the input')
userInput = None

while (userInput != '@'):
    userInput = input('Enter the name')
    if (userInput != '@'):
        f4.write(userInput + "\n")
f4.seek(0, 0)
str = f4.read()
print(str)
f4.close()

# module , package , library
# program (class / functions) ====> modules
# packages  ====> modules
# libraries ====>multiple packages


import os
import sys

file = input("enter a fileName :")
if os.path.isfile(file):
    f5 = open(file, "r")
else:
    print(file, "does not exist")
    sys.exit()
str = f5.read()
print(str)
f5.close()

# f = open("mytext5.txt", "w")
# str = (input("enter a sentance"))
# f.write(str)
# f.close()
