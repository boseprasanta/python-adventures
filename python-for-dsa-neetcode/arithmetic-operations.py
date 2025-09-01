# Division is decimal by default
a = 3 / 2
print(a)  # 1.5


b = -3/2
print(b)  # -1.5


# it always rounds towards negative infinity
# i.e floor value

a1 = 3 // 2
print(a1)  # 1


b1 = -3 // 2
print(b1)  # -2

# but say we want it to work like C/C++/Java
# i.e round towards zero

c1 = int(-3 / 2)
print(c1)  # -1


# Modulus operator
# it gives remainder
m1 = 5 % 2
print(m1)  # 1


# for modulus operator python follows the rule
# (a // b) * b + (a % b) == a
# so the sign of the modulus operator will be
# same as the sign of the divisor

m2 = 5 % -2
print(m2)  # -1