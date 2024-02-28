#
class A(object):
       def method(self):
           print("A is called")  # 3
           super().method()


class B(object):
    def method(self):
        print("B is called")  # 3
        super().method()


class C(object):
    def method(self):
        print("C is called")  # 3


class X(A,B):
    def method(self):
        print("X is called") # 2
        super().method()

class Y(B,C):
    def method(self):
        print("Y is called") # 2
        super().method()

class P(X,Y,C):
    def method(self):
        print("P is called") # 1
        super().method()
# p = P()
# p.method()

y=Y()
y.method()

