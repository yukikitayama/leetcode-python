# String Manipulation

- Python string is immutable (whereas C++ is mutable and Java is immutable)
- [How can I copy a Python string?](https://stackoverflow.com/questions/24804453/how-can-i-copy-a-python-string)
- [demo_string.py](https://github.com/yukikitayama/leetcode-python/blob/main/demo/demo_string.py)

## Immutable String

- An immutable string cannot be modified
- Modifying one of the characters means creating a new string.
- Understand `string concatenation`
  - First, allocate space for the new string
  - Then, copy the contents from the old string
  - Finally, append it to the new string
- Below looks `O(N)` time, but actually `O(N^2)`

```python
s = ''
n = 100
for i in range(n):
    s += 'hello'
```

- Time complexity is `O(N^2)`, because `len('hello'): 6`, 
  - `5 + 5 * 2 + 5 * 3 + ... + 5 * n`
  - `5 (1 + 2 + 3 + ... + n)`
  - `5 * (n * (n + 1) / 2)`
- In each iteration, string gets longer, but needs to copy everthing from the old string to new string.
- This does not happen in languages where string is mutable, such as `C++`.
- To avoid this, convert `string` into `list of characters`, so you can modify a part of it.

## Rabin-Karp Algorithm

- Pattern searching
  - e.g. Plagiarism detection, similar protein search in bioinformatics.
- Idea
  - Allows algorithm to compute the hash of the pattern string and substring by sliding window in the given string.
  - Pattern matching becomes computing two hashes and compare, which makes the time constant.
  - Rolling hash also makes the recomputing of the hash in the next sliding window the constant time.
- Time is `O(n + m)` where `n` is the length of the given string, and `m` is the pattern length.
- Worst case time is `O(n * m)`. Worst case of Rabin-Karp algorithm occurs when all characters of pattern and text are same as the hash values of all
  the substrings of the given string match with hash values of the pattern
  - e.g. The given string: "AAAAAAA", pattern: "AAA"
- [Rolling Hash Function Tutorial, used by Rabin-Karp String Searching Algorithm](https://www.youtube.com/watch?v=BfUejqd07yo)

### Problem

- [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)
- [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)
