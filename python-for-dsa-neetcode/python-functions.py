def outer(a, b):
    c = "c"
    def inner():
        return a + b + c
    return inner()

result = outer("a", "b")
print(result)  # abc


# can modify objects but not reassign
# unless nonlocal keyword is used

def double(arr, val11):
    x = 5
    def inner():
        for key, val in enumerate(arr):
            arr[key] = val * 2
        nonlocal val11        
        val11 = 20 # reassigning val here won't affect the val in
    inner()

arr1 = [1, 2, 3]
val1 = 10

double(arr1, val1)

print("arr1 =", arr1) # [2, 4, 6] because arr is modified in place
print("val1 =", val1)