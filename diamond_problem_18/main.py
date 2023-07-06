# diamond problem 

class A:
    def show(self):
        print('this is class A')

class B(A):
    def show(self):
        print('this is class B')

class C(A):
    def show(self):
        print('this is class C')

class D(C,B):
    pass

object = D()

object.show()
help(object)