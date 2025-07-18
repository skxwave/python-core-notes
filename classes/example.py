import hashlib

class Vector:
    def __init__(
        self,
        x: int,
        y: int,
    ):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))


# v = Vector(1, 2)
# print(v.__hash__())

# x = "string"
# y = "string1"

# print(x.__ne__(y))
# print(x.__hash__)


class Rofl:
    def __init__(self, number: int):
        self.__number = number

    def __add__(self, other):
        return self.__number / other
    
    # def __add__(self, other):
    #     return f"{self.__number} Hello world {other}"
    
    def __str__(self):
        return str(self.__number)
    
    def __repr__(self):
        return str(self.__number)
    
    def __eq__(self, other):
        return isinstance(other, Rofl) and self.__number == other._Rofl__number

    def __hash__(self):
        return hash(self.__number)
    

# obj1 = Rofl(5)
# obj2 = Rofl(10)
# new_obj = obj1 + obj2
# print(new_obj)
test = Rofl(1)
test2 = Rofl(1)

test_dict = {
    test: "Hello",
}
print(test_dict[test2])

print(dir(Rofl))
