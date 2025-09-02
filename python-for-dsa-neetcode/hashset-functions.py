myset = set()

myset.add(1)
myset.add(5)


print(myset)  # {1, 5}

myset.remove(5)
print(myset)  # {1}

myset2 = { j for j in range(10) }

print(myset2)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}