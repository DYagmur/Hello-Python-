#Numbers and Arithmetic in Python

# How tall am I, in meters, when wearing my hat?

hat_height_cm = 25
my_height_cm = 190
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =" , total_height_meters, "?")
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

print(min(1, 2, 3))
print(max(1, 2, 3))

#abs returns the absolute value of it argument:
print(abs(32))
print(abs(-32))

#In addition to being the names of Python's two main numerical types, int and float can also be called as functions which convert their arguments to the corresponding type
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(min)