# Dynamic Programming

- There are two ways to implement
  - Bottom-up (Tabulation)
    - Use iteration, by using for loop
    - Start from the base case, save the result in array, and repeat.
    - Usually faster than top-down, because functions calls and cache lookups of top-down are relatively expensive.
  - Top-down (Memoization)
    - Use recursion, by using recursion function.
    - Recursion until it hits the base case, save the result in hashmap, keep until clear the recursion stack.
    - Usually easier to write than bottom-up
- Any DP problem can be implemented and solved with either method.
  - You should be able to do both, because you may be asked to rewrite solution in bottom-up instead if solved in 
    top-down.
- A problem is likely to be a DP problem if ...
  1. Asking for the maximum, minimum, longest, or shortest of something.
  2. Asking for the number of distinct ways to do something (`Counting DP`).
  3. Current decisions depend on previous decisions.
  4. Asking for the path with constraints preventing moving backwards, only allowing to move down and right.
- Without memoization, it's just basic recursion with time O(2^n). But adding memoization makes it DP with time O(N).
- Framework
  1. Identify states
  2. Identify recurrence relation to transition between states.
  3. Identify base case to stop top-down recursion or to start tabulation.
- In multi-dimensional states DP problems, states could be ...
  - Start and end indices `i` and `j`.
  - Numerical constraint `k`. e.g. "You are only allowed to complete `k` transactions".
  - Status in a given state. e.g. "`True` if currently holding a key, `False` if not".
  - Tuple or bitmask indicating "visited" or "used". 
- `functools.lru_cache(maxsize=None)`
  - It means the cache size is not limited. We do this because the number of states that will be re-used in a problem
    is large, and we don't wanna evict a state early and have to re-calculate it.

```python
import functools

def func():
    @functools.lru_cache(maxsize=None)
    def recursion():
        pass
```

- Time and space complexity are the multiplication of states dimentions.
  - State reduction can lower time and space complexity.
- Space optimization
  - Whenever values calculated by DP are reused a few times and not used again, try if it can save space by replacing
    DP array with variables, so space is reduced from O(N) to O(1).
- Counting DP
  - Identify the base cases by logical thinking and usually the base is not 0.

## Time complexity

Time complexity of DP algorithm is tied to the number of possible states.

## Space complexity

In bottom-up case, we save the result in tabular. In top-down case, states are memoized. So the space complexity is 
equal to the number of states.

## Kadane's Algorithm

- Find the maximum sum subarray.
- Iterates array and decide whether current index is work keeping or disregard to reset.
- Kadane's Algorithm does not follow the typical DP framework, but it's DP because it uses optimal sub-structures.

### Complexity

- Time is O(n)
- Space is O(1)

## Memoization

Typically save the result in **hashmap**

## Recursion

Need base cases to stop recursion

Use logical thinking to find the base cases in each problem