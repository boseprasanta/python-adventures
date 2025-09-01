# sublists (aka slicing)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[0 : 4]) # arr(0) to arr(3) => [1, 2, 3, 4]

print(len(arr)) # 4


# unpacking array
a, b, c, *rest = arr
print(a, b, c) # 1 2 3
print(rest) # [4, 5, 6, 7, 8, 9]

e, f, g = [10 , 20, 30] # works elemnts in left and right should be same
print(e, f, g) # 10 20 30


# looping through array

for i in range(len(arr)):
    print("index =", i, "value =", arr[i])

for e in arr:
    print("value =", e)

for index, value in enumerate(arr):
    print("index =", index, "value =", value)

# joining two arrays
arr2 = [10, 11, 12]

for n1, n2 in zip(arr, arr2):
    print(n1, n2) # will print till the smaller array ends  