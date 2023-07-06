# MRO = Method Resolution Order // multiple inheritance


class A:
    def show(self):
        print('this is show A')

class B:
    def show(self):
        print('this is show B')

class C(A,B):  # urutannya C -> A -> B
    pass

object = C()

object.show() # urutan yang dipanggil C -> A -> B
help(object)

