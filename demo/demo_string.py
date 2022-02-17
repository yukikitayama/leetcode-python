import copy


def demo1():

    text = 'test'
    x = text.ljust(5)
    print(len(x))
    print(f'x: {x}.')

    cur = []
    cur += ['test']
    print(cur)
    cur += ['is']
    print(cur)

    text = 'test'
    print(text[:0] + text[1:])
    print()
    for i in range(len(text)):
        print(text[:i] + text[i + 1:])


def demo2():
    # As long as they have the same value, they reference to the same place
    a = 'a'
    b = a
    c = a[:]
    d = a + ''
    e = copy.copy(a)
    print(f'id(a): {id(a)}, a: {a}')
    print(f'id(b): {id(b)}, b: {b}')
    print(f'id(c): {id(c)}, c: {c}')
    print(f'id(d): {id(d)}, d: {d}')
    print(f'id(e): {id(e)}, e: {e}')
    print(a == b)
    print(a == c)
    print(a == d)
    print(a == e)

    # Python string is immutable
    print(f'id(a): {id(a)}, a: {a}')
    a = a + 'b'
    print(f'id(a): {id(a)}, a: {a}')


def demo3():

    s = ''
    n = 100
    for i in range(n):
        s += 'hello'


if __name__ == '__main__':

    # demo1()

    demo2()

    demo3()
