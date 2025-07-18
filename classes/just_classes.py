class User:
    def __init__(
        self,
        first_name,
        last_name,
    ):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + self.last_name


user = User("Roman", "Kovalchuk")

print(user.get_full_name())
print(User.get_full_name(user))

"""
Спочатку викликається метод __new__, який створює
екземпляр класу — тобто виділяє памʼять
і повертає сам обʼєкт

Потім викликається __init__,
який ініціалізує обʼєкт — задає йому атрибути,
перевірки, логіку.
"""

