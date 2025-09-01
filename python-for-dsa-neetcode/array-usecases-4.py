# array functions and usecases

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr.reverse()
print(arr)  # [9, 8, 7, 6, 5, 4, 3, 2, 1] reverses the array in place


arr.sort()  # sorts the array in place
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr1 = [3, 6, 1, 8, 4, 2]
arr1.sort(reverse=True)  # sorts the array in place in descending order
print(arr1)  # [8, 6, 4, 3, 2, 1]

# sort list of strings
words = ["banana", "apple", "cherry", "date"]
words.sort()
print(words)  # ['apple', 'banana', 'cherry', 'date']

words.sort(key = lambda x: len(x))  # sort by length of string
print(words)  # ['date', 'apple', 'banana', 'cherry']