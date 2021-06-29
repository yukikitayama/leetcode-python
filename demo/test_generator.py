def func1():
    for i in range(3):
        return i


def func2():
    for i in range(3):
        yield i


print(func1())
print(func2())

# TypeError: 'int' object is not iterable
# for i in func1():
#     print(i)

for i in func2():
    print(i)
print()

# Why do you do this?


def func3(digit_str):
    for i in range(4):
        x = int(digit_str)
        for d in (-1, 1):
            y = (x + d) % 10
            yield digit_str[:i] + str(y) + digit_str[i + 1:]


digit_str = '1111'
for digit in func3(digit_str):
    print(digit)
print()


def func4(digit_str):
    for i in range(4):
        x = int(digit_str)
        for d in (-1, 1):
            y = (x + d) % 10
            print('here')
            return digit_str[:i] + str(y) + digit_str[i + 1:]


# func4 return length len(digit_str) string and iterate over the string one char by one char
for digit2 in func4(digit_str):
    print(digit2)
