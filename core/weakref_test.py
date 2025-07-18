import weakref


class User:
    __slots__ = ("name",)

    def __init__(
        self,
        name,
    ):
        self.name = name

    def __del__(self):
        print(f"bye {self=}")


user = User("Roman")
user2 = User("Maks")

print(user.name)
print(user2.name)



print(user.name)
