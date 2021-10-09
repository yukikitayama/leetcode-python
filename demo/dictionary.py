import pprint


node = {'a': 1, 'b': 2, 'c': 3, '$': 'test'}
pprint.pprint(node)

# When popped with a key in the dictionary
popped = node.pop('a', False)
print(f'popped: {popped}')
pprint.pprint(node)

# When popped with a key not in the dictionary and with default value
popped = node.pop('d', False)
# The default value is returned
print(f'popped: {popped}')
# And the dictionary is intact
pprint.pprint(node)

popped = node.pop('$', False)
print(f'popped: {popped}')
if popped:
    print('if')
else:
    print('else')
