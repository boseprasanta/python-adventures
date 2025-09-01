# array is called list in python
arr = [1, 2, 3, 4, 5]
print(arr)  # [1, 2, 3, 4, 5]


# array in python are dynamic so can be use as stack
arr.append(6)
arr.append(7)

print(arr)  # [1, 2, 3, 4, 5, 6, 7]


# pop from end
x = arr.pop()
print(x)  # 7
print(arr)  # [1, 2, 3, 4, 5, 6]

# pop from start
y = arr.pop(0)
print(y)  # 1
print(arr)  # [2, 3, 4, 5, 6]
# pop from middle
z = arr.pop(2)
print(z)  # 4
print(arr)  # [2, 3, 5, 6]

# insert at start
arr.insert(0, 1)
print(arr)  # [1, 2, 3, 5, 6]
# insert at middle
arr.insert(3, 4)
print(arr)  # [1, 2, 3, 4, 5, 6]
# insert at end
arr.insert(7)