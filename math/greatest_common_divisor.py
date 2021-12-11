# Example of Euclidean algorithm
a = 48
b = 18
print(f'a: {a}, b: {b}')

while b:
    a, b = b, a % b
    print(f'a: {a}, b: {b}')

print(a)


# Make it a function
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(get_gcd(a, b))


# Python built-in function
import math
print(math.gcd(a, b))
