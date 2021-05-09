# Python module to import

print(f'File two __name__ is set to: {__name__}')


def function_three():
    print('Function three is executed')


def function_four():
    print('Function four is executed')


if __name__ == '__main__':
    print('File two executed when ran directly')
else:
    print('File two executed when imported')
