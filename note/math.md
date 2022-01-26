## Math

- Sum of digits time complexity is O(logN), base is 10.
  - https://github.com/yukikitayama/leetcode-python/blob/main/math/sum_of_digits_time_is_logn.png
  - [Explain why time complexity for summing digits in a number of length N is O(logN)](https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn)
- Read an integer one by one from left to right and create number
  - Initialize as `num = 0`, and then in the for loop, `num = num * 10 + curr_num`

### Greatest Common Divisor

- Greatest common divisor of a and b is the largest positive integer d such that d is dividor of both a and b.
  - e.g. gcd(8, 12) is 4. 2 is also common divisor but it's not the largest. 6 is divisor of 12 but 8 is not divisible
    by 6 because divmod(8, 6) is quotient: 1, remainder: 2 not 0.
- Use Euclidean algorithm
  1. Wanna get GCD of `a` and `b`. 
  2. Keep replacing `(a, b)` by `(b, a % b)` until it becomes `(d, 0)`.
  3. `d` is GCD.
- [GCD example](https://github.com/yukikitayama/leetcode-python/blob/main/math/greatest_common_divisor.py)
- Python built-in function `math.gcd` is available from Python 3.5.

### Least Common Multiple

- Least common multiple of a and b is the smallest positive integer that is divisible by a and b.
  - e.g. lcm(4, 6), multiples of 4: 4, 8, **12**, 16, ..., multiple of 6: 6, **12**, 18, ... 12 is the smallest common
    number.
- Use greatest common divisor
  1. Make or import a function to calculate GCD.
  2. `LCM(a, b) = abs(a * b) / gcd(a, b)`.
- [LCM example](https://github.com/yukikitayama/leetcode-python/blob/main/math/least_common_multiple.py)
- Python built-in function `math.lcm` is available from Python 3.9

### Modulo

- Modulo is distributive `(a + b) % n = {(a % n) + (b % n)} % n`
  - LeetCode: [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)
- [Wiki modulo properties](https://en.wikipedia.org/wiki/Modulo_operation#Properties_(identities))

### Remainder

- Numerator is `dividend`. Denominator is `divisor`. Division produces `quotient` and `remainder`.
- Remainder of dividend divided by divisor is equal to the remainder of remainder divided by divisor.
  - e.g. divmod(5, 2) = (2, 1), divmod(1, 2) = (0, 1)
  - [1015. Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/)

### Log

- `log_base(result) = exponent <-> base^exponent = result`
  - `log_2(4) = 2 <-> 2^2 = 4`
- Check whether a number if power of two
  - `if math.log(NUMBER, 2).is_integer()`
    - If NUMBER is 4, it returns 2, which is integer
    - If NUMBER is 3, it returns 1.58..., which is not integer. 
  - `math.log(result, base)`

### Strictly Increasing

- The next value must be greater than the current value.
- "Greater than or equal to" is not strictly increasing.
- e.g. `1 -> 2 -> 3` is strictly increasing, but `1 -> 3 -> 3 -> 4` is, though increasing, not strictly increasing.
