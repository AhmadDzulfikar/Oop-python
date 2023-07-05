class A:
    def method_a(self):
        print("ini adalah method A")

class B:
    def method_b(self):
        print("ini adalah method B")


class Child(A,B): # NOTE : multiple inheritance itu class sub bisa dapet inherit dari banyak class
    pass

object = Child()

object.method_a()
object.method_b()