import sys

gener = (x for x in range(500)) # if there is ~5-10 elements, generator will be larger
lst = [x for x in range(500)]

print(sys.getsizeof(gener))
print(sys.getsizeof(gener.__next__()))
print(sys.getsizeof(gener))
print(sys.getsizeof(lst))
