import math

print("math.fmod(-10, 3)  =", math.fmod(-10, 3))  # remainder of x / y
print("math.floor(-10 / 3) =", math.floor(-10 / 3))  # floor value
print("math.ceil(-10 / 3) =", math.ceil(-10 / 3))  # ceil value
print("math.trunc(-10 / 3) =", math.trunc(-10 / 3))  # rounds towards zero
print("math.sqrt(16) =", math.sqrt(16))  # square root
print("math.pow(2, 3) =", math.pow(2, 3))  # power
print("math.gcd(12, 15) =", math.gcd(12, 15))  # gcd


# Max / Min  Int

float('inf')  # positive infinity
float('-inf')  # negative infinity

# Python numbers are infinite so they don't overflow

import math

a_big_number = math.pow(2, 200) # very big number

if a_big_number > float('inf'):
    print("a_big_number is greater than infinity")
elif a_big_number > float('-inf'):
    print("a_big_number is greater than negative infinity")
