class Point:
    MAX_COORD = 100
    MIN_COORD = 0


the_same_class = type(
    "Point2",
    (),
    {
        "MAX_COORD": 100,
        "MIN_COORD": 0,
    },
)

print(the_same_class.MAX_COORD)
print(Point.MAX_COORD)


print(Point.__dict__)