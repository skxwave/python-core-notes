class FieldValidation:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("must be integer")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__.pop(self.name, None)


def typed_property(expected_type: type):
    class TypedField:
        def __init__(self, func):
            self.func = func

        def __set_name__(self, owner, name):
            self.name = name

        def __get__(self, instance, owner):
            return instance.__dict__.get(self.name)

        def __set__(self, instance, value):
            if not isinstance(value, expected_type):
                raise TypeError(f"{self.name} must be {expected_type.__name__}")
            instance.__dict__[self.name] = value

    return TypedField


class A:
    x = FieldValidation()
    y = FieldValidation()
    z = FieldValidation()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @typed_property(int)
    def test(self):
        pass


a = A(1, 2, 3)
a.test = 2
print(a.x)
del a.x
print(a.x)
print(a.test)
print(a.__dict__)
