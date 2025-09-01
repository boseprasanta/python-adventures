# initialize an array with sane values in all blocks

n = 5
arr = [1] * n

print(arr)  # [1, 1, 1, 1, 1]

# initiate 2d array
print([[1]* n for _ in range(n)])  # [[1, 1, 1, 1, 1], [1, 1,


# length of array
print(len(arr))  # 5


# negative indexing
print(arr[-1])  # 1
print(arr[-2])  # 1 (2nd last element)