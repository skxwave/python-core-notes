import sys
from typing import Union
import test_module


test_list = [1, 2, 3]
test_tuple = (1, 2, 3)

a, b, c = test_tuple

test_dict = {
    "name": "Hello",
    "surname": "World",
}

# print(test_dict.items())
# print(test_dict.keys())
# print(test_dict.values())
# print(dict.fromkeys(test_list))
# print(("name", "Hello") in test_dict.items())

test_dict2 = {
    test_module: "Hello",
    frozenset: "World",
}
# print(test_dict2)

ziptest = dict(zip([1, 2], [1, 2]))
# print(ziptest)


def test(
    bar: list = [],
    foo: dict = {},
) -> tuple[list, dict]:
    bar.append(1)
    if not foo.get("name"):
        foo["name"] = "Roman"
    else:
        foo["surname"] = "Kovalchuk"
    return bar, foo


# bar, foo = test()
# print(bar, foo)
# bar, foo = test()
# print(bar, foo)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# gen = fibonacci_generator()
# print("size when initialized", sys.getsizeof(gen)) # 200

# for _ in range(1000):
#     next(gen)
#     print("size while getting data", sys.getsizeof(gen)) # 200

# print("size after", sys.getsizeof(gen)) # 200


def subgen():
    yield 1
    yield 2
    yield 3


def subgen_test():
    yield "start"
    yield from subgen()
    yield "stop"


gen = subgen_test()

# print(next(gen))
# print(next(gen))


class Test1:
    __slots__ = ("x", "y")

    def __init__(self, x):
        self.x = x


class Test2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


test1 = Test1(1)
test2 = Test2(1, 2)

print(sys.getsizeof(test1))
print(sys.getsizeof(test2))
print(__name__)  # "__main__"
