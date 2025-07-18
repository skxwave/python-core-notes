class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        A.__init__(self)  # straight from class


class C(A):
    def __init__(self):
        print("C")
        A.__init__(self)  # straight from class


class D(B, C):
    def __init__(self):
        print("D")
        B.__init__(self)
        C.__init__(self)

"""
Result: D, B, A, C, A

Thats bad, because we have doubled A
"""
d = D()


class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

"""
Result: D, B, C, A

Thats great, we resolved it better, without repeating
"""
d = D()
