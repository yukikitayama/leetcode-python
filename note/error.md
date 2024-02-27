# Error

## TypeError: unhashable type: 'list'

This appeared when I used a list as a key of a dictionary. Only **hashable objects** are acceptable as keys of dictionary. 
Example of hashable objects are **tuples** and **strings**. Hashable objects are objects with a hash value that doesn't 
change over time.

```python
list_ = [1, 2, 3]

dictionary[tuple(list_)] = 0
```

https://careerkarma.com/blog/python-typeerror-unhashable-type-list/
