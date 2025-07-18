from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    age: int


class HandleUser:
    __slots__ = "_user"

    def __init__(self):
        self._user: User = None

    def create_user(self, name: str, age: int) -> None:
        if self._user:
            raise TypeError("User already exists.")
        self._user = User(name, age)

    def update_user(self, name: str, age: int) -> None:
        return self._user

    @property
    def user(self) -> User:
        return self._user
    
    # def __eq__(self, value) -> bool:
    #     # return super().__eq__(value)
    #     return self.__class__ == value


user_handler = HandleUser()
user_handler2 = HandleUser()

user_handler.create_user(name="Roman", age=21)
user_handler2.create_user(name="Roman", age=21)

user = user_handler.user
user2 = user_handler2.user

print(user.age, user.name)
print(user2.age, user2.name)

print(user_handler == user_handler2)


