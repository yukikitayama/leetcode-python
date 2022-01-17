# String Manipulation

### Rabin-Karp Algorithm

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

#### Problem

- [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)
- [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)
