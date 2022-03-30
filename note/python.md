# Python

## Hash table

When you use modulo as hash function, the divisor should use prime number (e.g. 1999), because it can best avoid 
collision.

Integer, string and tuple are the Python valid dictionary keys. You cannot use list as key, because Python list is 
[mutable unhashable object](https://www.geeksforgeeks.org/how-to-use-a-list-as-a-key-of-a-dictionary-in-python-3/). So first convert the list to tuple, and then use it as a key of the Python dictionary.

### Complexity

In the best case, the bucket size is small enough to be regarded as constant, so insertion and search are O(1). But in 
the worst case, all the items go to the same bucket and the size becomes N, so search time complexity will be O(N) while
insertion is still O(1).

If there are too many values in the same bucket, you should use `height-balanced binary search tree` instead. In the 
worst case, search and insertion time complexity is O(logN).

## Counter()

- `collections.Counter`
- Supports comparison operators
  - Time complexity is `O(N)` where `N` is the number of keys in Counter.
  - [Python Runtime of collections.Counter Equality](https://stackoverflow.com/questions/52341976/python-runtime-of-collections-counter-equality)
  - Equality compares corresponding counts.

```python
import collections
c1 = collections.Counter('aab')
c2 = collections.Counter()
print(c1 == c2)  # False
c2['a'] = 1
c2['b'] = 1
print(c1 == c2)  # False
c2['a'] = 2
print(c1 == c2)  # True
c2['c'] = 0
print(c1 == c2)  # False
```

- `COUNTER.elements()` returns a list of each key repeated by its value times.
  - e.g. `counter = Counter('aab') -> counter: {'a': 2, 'b': 1} -> counter.elements() -> ['a', 'a', 'b']`

## OrderedDict()

- `OrderedDict` preserves the order in which the keys are inserted. It's not about sorting by key to be ordered.
- So `OrderedDict` should be used with `DICTIONARY.items()` and `DICTIONARY.values()` to iterate to make use of an 
  inserted order.
- Regular Python dictionary does not track the order of insertion, so iterating the keys gives in an arbitrary order.

## Stack

- Use stack when you wanna delay processing the current data later

#### Problem

- [71. Simplify Path](https://leetcode.com/problems/simplify-path/)

## Sort

### Timsort

- Python `LIST.sort()` and `sorted(LIST)`.
- Time is `O(NlogN)`.
- Space is `O(N)`

### Counting sort

- Suitable when the value range of array is not significantly greater than the length of array.
- Algorithm
  - Initialize array with 0s with length (max - min + 1)
  - Get shift by -min
  - Iterate each num in the given array
  - Count up the initialized array at current num + shift
- Complexity
  - Let N be the length of the given array, and M be the value range of the array.
  - Time is `O(M + N)` because initializing the array is `O(M)` and iterating the given array is `O(N)`.
  - Space is `O(M)` for the initialized array.

#### Example

- [1200. Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)

### Bucket Sort

- Sorting algorithm that works by distributing the elements of an array into a number of buckets
- Require prior knowledge for the range of the data
- Useful if you know the range of values from the problem constraints.
- For example, initialize an empty array by the length by min and max of the value range, insert the original array 
  value as the index to the new array, so you don't need to apply sort, because when inserting, values are sorted.

#### Example

- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)
- [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)

### Quickselect

- Should consider whether Quickselect can be applied when the problem is to find the k (or kth) smallest/larest/etc 
  element(s).

#### Example

- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

## Swap

- Reduce a temporary variable and lines of code by multiple items at the both sides of an equal sign.

```python
# Before
tmp = curr.next
curr.next = prev
prev = curr
curr = tmp

# After
curr.next, prev, curr = prev, curr, curr.next
```

## String

- `STRING.split()` time complexity is `N` where `N` is the length of the string.
  - [Time/space complexity of in-built python functions](https://stackoverflow.com/questions/55113713/time-space-complexity-of-in-built-python-functions)
- `Substring` is a **contiguous** sequence of characters within a string.
- `STRING.isupper()`
  - Returns True if all characters in the string are uppercase.

## Array

- `Subsequence`
  - An array by deleting some or no elements without changing the order of the remaining elements
  - e.g. `[3, 6, 2, 7]` is a subsequence of the array `[0, 3, 1, 6, 2, 2, 7]`.
- `enumerate(iterable, start)` can change the starting integer by start.

```python
input = ['a', 'b', 'c']
print(list(enumerate(input)))
# [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(enumerate(input, 1)))
# [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(enumerate(input[1:], 1)))
# [(1, 'b'), (2, 'c')]
```

- `LIST.reverse()`
  - Time complexity of reversing a list is `O(N)` the length of list.
- [Python list time complexity table](https://wiki.python.org/moin/TimeComplexity)
  - `insert()` is `O(N)` time, because you need to shift all elements after the insert position one step backward.
  - `remove()` is also `O(N)` time, because after removing an item from position i, you need to shift all elements after
    i one step forward.
  - `append()` is `O(1)` time.
- `Slicing`
  - `LIST[::2]` means every 2 element from 0 to end index
  - e.g. `[1, 2, 3, 4, 5][::2]` is `[1, 3, 5]`

## Iterator

- Only needs to know how to get the next item.
  - It doesn't need to store the entire data in memory.
- It can represent a sequence without using a data structure
  - Below, if min and max are far apart, an array data structure allocates a lot of memory
  - But the RangeIterator still consumes only `O(1)` space
```python
class RangeIterator:
    def __init__(self, min, max):
        self.current = min
        self.max = max

    def has_next(self):
        return self.current < self.max

    def next(self):
        # This updates self.current
        self.current += 1
        # This does not update self.current
        return self.current - 1
```

- Can handle an infinite sequence. An array is always bounded finite sequence.

### Problem

- [284. Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)

## Generator

### Generator Expression

- `GENERATOR = (x for x in list)`
  - Use generator expression in round parentheses , similarly to making list comprehension, to create generators on the fly
  - Use it by `x = next(GENERATOR, DEFAULT_VALUE)`. `DEFAULT_VALUE` is returned when the generator is exhausted.

#### Problem

- [849. Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/)

## Set

- `SET.discard(ITEM)` doesn't raise an error if the specified item does not exist in the set, while `SET.remove(ITEM)`
  raises an error.

## reduce()

- The purpose of using `reduce()` is to reduce the iterable object to a single cumulative value without using a for 
  loop.
- Actually many of the use cases with `reduce()` are replaced with the new Python built-in functions, but good to know
  `reduce()` exists.
- In Python 2.X `reduce()` was a built-in function, but in Python 3.0 it moved to `functools.reduce()`.
- `functools.reduce(function, iterable[, initial_value])`
  - `function`: A function which has two arguments.
    - The left argument is the accumulated value
    - The right argument is the update value from the iterable.
- e.g. `reduce(lambda x, y: x * y, [1, 2, 3, 4])` is `((1 * 2) * 3) * 4`
- [Demo](https://github.com/yukikitayama/leetcode-python/blob/main/demo/demo_functools_reduce.py)
- The difference between `itertools.accumulate()` and `functools.reduce()`
  - `itertools.accumulate()` returns an iterator of accumulation in the sequence.
  - `functools.reduce()` only returns the final value fo the accumulation in the sequence.

### Reference

- [Python's reduce(): From Functional to Pythonic Style](https://realpython.com/python-reduce-function/)
- [The fate of reduce() in Python 3000](https://www.artima.com/weblogs/viewpost.jsp?thread=98196)

## prod()

- `math.prod`
- Quick tool to calculate the cumulative product from an array of numbers.

```python
import math
nums = [1, 2, 3, 4]
print(math.prod(nums))
# 1 * 2 * 3 * 4 = 24
```

## Operator

- Assignment operator with inline if-else statement. The below increments if true and decrements if false. Even if `-` 
  does not have `=`, it works as assignment operator
  - `num += 1 if SOMETHING is True else -1`

## String

- `ord('a')` gives `97`.
- `chr(97)` gives `'a'`.
- `chr()` gives `ASCII characters` by 0-based integer.

## Integer

- Integer overflow does not occur in Python3.
- It does not have fixed maximum, called `arbitrary precision`
- But it's limited by available compute memory.
- [Is there a way to get the largest integer one can use in Python? [duplicate]](https://stackoverflow.com/questions/4581842/is-there-a-way-to-get-the-largest-integer-one-can-use-in-python)
- [Can Integer Operations Overflow in Python?](https://mortada.net/can-integer-operations-overflow-in-python.html)