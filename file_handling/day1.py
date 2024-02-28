# program 1
# text handleing

f = open("mytext.txt", "w")
str = input("Enter a Text : ")
f.write(str)
f.close()

# program 2
# Read mode
f = open("mytext.txt", "r")
str1 = f.read()
print(str1)
f.close()

# program 3 - store multiple names in the string
f = open("mytext2.txt", "w")
print('type @ to stop data writing')
userInput = None
while userInput != '@':
    userInput = input("Enter the names")  # vrushali # patil # sanjeet # wandhare #@
    if userInput != '@':
        f.write(userInput + "\n")
f.close()

# program 4
f = open("mytext2.txt", "r")
# #1
# str3=f.read()
# print(str3)
# f.close()
# #2
# List = f.readlines()
# for item in List:
#     print(item)
f.close()
