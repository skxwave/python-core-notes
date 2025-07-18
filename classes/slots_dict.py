class User:
    __slots__ = ("name", "surname", "__dict__")

    def __init__(self, name):
        self.name = name


user = User(name="Roman")
user.surname = "Kovalchuk"
user.surname2 = "Kovalchuk2"
print(user.name)
print(user.surname)
print(user.surname2)
print(user.__dict__)
print(user.__slots__)


class SuperUser:
    def __init__(self, name):
        self.name = name


admin = SuperUser(name="Roman")
print(admin.name)
print(admin.__dict__)

admin.surname = "Kovalchuk"
print(admin.surname)
print(admin.__dict__)
