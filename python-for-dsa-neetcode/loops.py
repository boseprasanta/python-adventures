# while loop from n = 0 to n = 4
n = 0

print("while loop from n = 0 to n = 4")
while n < 5:
    print("n =", n)
    n = n + 1
    # n++ is wrong

# for loop from i = 0 to i = 4

print("for loop from i = 0 to i = 4")
for i in range(5):
    print("i =", i)



print("defination of range is range(start, end, step)")
for i in range(1, 10, 5): # will print from 1 to 9
    print("i =", i)    

print("for loop from i = 10 to i = 1")
for j in range(10, 0, -1): # will print from 10 to 1
    print("j =", j)