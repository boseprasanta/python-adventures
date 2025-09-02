# strings can be sliced like arrays
s = "Hello, World!"
print(s[0:5])

# s[0] = "h"  # error, strings are immutable 

# updating the string creates a new string
s = "h" + s[1:]
print(s) 

# valid strings can be changed to integer
print(int("123") + 234)

print(str(123) + "234")

# join function to join list of strings
words = ["Hello", "World"]

s2 = " ".join(words)
print(s2)