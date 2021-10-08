s = 'abcde'
it = iter(s)
t = 'ace'
for char in t:
    res = char in it
    print(f'char: {char}, res: {res}')