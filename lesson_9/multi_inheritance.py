class A(object):
    def test(self):
        print("A")

class B(object):
    def test(self):
        print("B")

class C(object):
    def test(self):
        print("C")

class D(A, B, C):
    def test(self):
        super(D, self).test()
        print("D")


d = D()
d.test()
