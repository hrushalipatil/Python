# two class and one function

class fruits:
    def color(self):
        print("apple is red in color")


class flower:
    def color(self):
        print("rose is red in color")


def set_color(object):
    object.color()


a = fruits()
b = flower()
set_color(a)
set_color(b)

x = fruits()
x.color()  # apple is red in color

y = flower()
y.color()  # rose is red in color


# 2. program
class nagpur:
    def maharastra(self):
        print("nagpur in maharastra")


class mumbai:
    def maharashtra(self):
        print("mumbai in maharastra")


class gujrat:
    def surat(self):
        print("surat n gujrat")


def state(object):
    if (hasattr(object, "maharastra")):
        object.maharastra()
    elif (hasattr(object, "surat")):
        object.surat()
    else:
        print("wrong object pass....")


A = nagpur()
state(A)  # nagpur in maharastra

B = mumbai()
state(B)  # mumbai in maharastra

# C = punjab()
# state(C)  # wrong object pass....

D = gujrat()
state(D)  # surat n gujrat


# program 3
# print(10 + 15)  # 25
#
# print("hello " + "world")  # "helloworl"
#
# print([11, 22, 23] + [44, 55, 66])  # [11,22,33,44,55,66]


# operator overloading
class Bookx():
    def __init__(self, x):
        self.pages = x


class Booky():
    def __init__(self, y):
        self.pages = y


b1 = Bookx(12)
b2 = Booky(23)
# print(b1 + b2)
print(b1.pages + b1.pages)  # 24
