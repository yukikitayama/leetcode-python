# Use Euclidean algorithm for greatest common divisor
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a = 4
b = 6
print(abs(a * b) // get_gcd(a, b))


# Use built-in functions
import math
print(abs(a * b) // math.gcd(a, b))

# math.lcm is available from Python 3.9
print(math.lcm(a, b))
