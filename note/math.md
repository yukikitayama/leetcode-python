## Math

- Sum of digits time complexity is O(logN), base is 10.
  - https://github.com/yukikitayama/leetcode-python/blob/main/math/sum_of_digits_time_is_logn.png
  - [Explain why time complexity for summing digits in a number of length N is O(logN)](https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn)
- Read an integer one by one from left to right and create number
  - Initialize as `num = 0`, and then in the for loop, `num = num * 10 + curr_num`

## Greatest Common Divisor

- Greatest common divisor of a and b is the largest positive integer d such that d is dividor of both a and b.
  - e.g. gcd(8, 12) is 4. 2 is also common divisor but it's not the largest. 6 is divisor of 12 but 8 is not divisible
    by 6 because divmod(8, 6) is quotient: 1, remainder: 2 not 0.
- Use Euclidean algorithm
  1. Wanna get GCD of `a` and `b`. 
  2. Keep replacing `(a, b)` by `(b, a % b)` until it becomes `(d, 0)`.
  3. `d` is GCD.
- [GCD example](https://github.com/yukikitayama/leetcode-python/blob/main/math/greatest_common_divisor.py)
- Python built-in function `math.gcd` is available from Python 3.5.

## Least Common Multiple

- Least common multiple of a and b is the smallest positive integer that is divisible by a and b.
  - e.g. lcm(4, 6), multiples of 4: 4, 8, **12**, 16, ..., multiple of 6: 6, **12**, 18, ... 12 is the smallest common
    number.
- Use greatest common divisor
  1. Make or import a function to calculate GCD.
  2. `LCM(a, b) = abs(a * b) / gcd(a, b)`.
- [LCM example](https://github.com/yukikitayama/leetcode-python/blob/main/math/least_common_multiple.py)
- Python built-in function `math.lcm` is available from Python 3.9

## Modulo

- Modulo is distributive `(a + b) % n = {(a % n) + (b % n)} % n`
  - LeetCode: [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)
- [Wiki modulo properties](https://en.wikipedia.org/wiki/Modulo_operation#Properties_(identities))
- [1260. Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/)
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

[368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/description/)

Given a list of values [E, F, G] sorted in ascending order (i.e. E < F < G), and the list itself forms a divisible subset as described in the problem, then we could extend the subset without enumerating all numbers in the subset, in the following two cases:
- Corollary I: For any value that can be divided by the largest element in the divisible subset, by adding the new value into the subset, one can form another divisible subset, i.e. for all h, if h % G == 0, then [E, F, G, h] forms a new divisible subset.
- Corollary II: For all values that can divide the smallest element in the subset, by adding the new value into the subset, one can form another divisible subset, i.e. for all d, if E % d == 0, then [d, E, F, G] forms a new divisible subset.

## Remainder

- Numerator is `dividend`. Denominator is `divisor`. Division produces `quotient` and `remainder`.
- Remainder of dividend divided by divisor is equal to the remainder of remainder divided by divisor.
  - e.g. divmod(5, 2) = (2, 1), divmod(1, 2) = (0, 1)
  - [1015. Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/)

### Prefix sum and remainder

- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/description/)
  - [Java O(n) time O(k) space](https://leetcode.com/problems/continuous-subarray-sum/solutions/99499/java-o-n-time-o-k-space/)
    - Read the Comments section
      - "For e.g. in case of the array [23,2,6,4,7] the running sum is [23,25,31,35,42] and the remainders are [5,1,1,5,0]. We got remainder 5 at index 0 and at index 3. That means, in between these two indexes we must have added a number which is multiple of the k. Hope this clarifies your doubt :) (a+(n*x))%x is same as (a%x)"

## Prefix sum

- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/description/)

## Log

- `log_base(result) = exponent <-> base^exponent = result`
  - `log_2(4) = 2 <-> 2^2 = 4`
- Check whether a number if power of two
  - `if math.log(NUMBER, 2).is_integer()`
    - If NUMBER is 4, it returns 2, which is integer
    - If NUMBER is 3, it returns 1.58..., which is not integer. 
  - `math.log(result, base)`
- The logarithm functions is non-linear, so when you take the log, you need to contain the entire terms on one side
  - e.g. `a + b = c`, taking log of both side is `log(a + b) = log(c)`, not `log(a) + log(b) = log(c)`.
  - [When I take the Log of both sides of an equation, should I only do it once?](https://math.stackexchange.com/questions/2036159/when-i-take-the-log-of-both-sides-of-an-equation-should-i-only-do-it-once)
- Find the depth of a N-ary tree.
  - If a tree divides `M` branches at each level, and if we know the number of node, the depth of the tree is `log_M(N)`
    (base M)
  - e.g. 4 branches at each level, and total nodes are 1,000,000, the depth of the tree is `log_4(1000000) = 9.97...`

## Strictly Increasing

- The next value must be greater than the current value.
- "Greater than or equal to" is not strictly increasing.
- e.g. `1 -> 2 -> 3` is strictly increasing, but `1 -> 3 -> 3 -> 4` is, though increasing, not strictly increasing.

## Digital Root

- Summing digits of a number and continue until a single-digit number is reached.
- On each iteration using the result from the previous result
  - e.g. `38 -> 3 + 8 = 11 -> 1 + 1 -> 2`, so the digital root of 38 is 2.
- In base 10, if n = 0, digital root of n is 0
- If n = 9 * k, digital root of n is 9
  - e.g. `9 * 2 = 18 -> 1 + 8 = 9`
  - `9 * 3 = 27 -> 2 + 7 = 9`
- If n != 9 * k, digital root of n is `n % 9`
  - `1 % 9 = 1`
  - `11 % 9 = 2`
  - `50 % 9 = 5`
- [258. Add Digits](https://leetcode.com/problems/add-digits/)

# Permutations

- `n! / (n - r)!` where `n` is the number of thins to choose from, and we choose `r` of them, `no repetitions`, 
  `order matters`
- [Combinations and Permutations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
- [447. Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/)

## Reverse polish notation

- `3 4 +`, `3` and `4` are operands, and `+` is operator.
- In reverse polish notation, operators follow their operands.
- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
- [Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

## Sum of integers

- `(n * (n + 1)) / 2`
- [1 + 2 + 3 + 4 + ⋯](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF)
- [2421. Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/description/)
- [2485. Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer/description)
- [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/description)

## Binary exponentiation

**Binary exponentiation** is a method to optimize time of computing `x` raised to the power `n` in `x^n`.

With this approach, time complexity will be `O(logN)` instead of `O(N)` by multiplying `x` by `n` times (**Linear exponentiation**).

The idea is,
- If `n` is even, `(x^2)^{n / 2}`
- If `n` is odd, `x * (x^2)^{(n - 1) / 2}`

```
2^100 = (2 * 2)^50
4^50 = (4 * 4)^25
...
(10 steps)
```

instead of

```
2^100 = 2 * 2^99
2^99 = 2 * 2 * 2^98
...
(100 steps)
```

For example, when `x = 2` and `n = 16` to compute `2^16`, `log(16) = 4`

```
2^16 = (2 * 2)^{16 / 2} = 4^8
4^8 = (4 * 4)^{8 / 2} = 16^4
16^4 = (16 * 16)^{4 / 2} = 256^2
256^2 = (256 * 256)^{2 / 2} = 65536

(4 steps)
```

But with linear exponentiation,

```
2^16 = 2 * 2^16
2 * 2^16 = 2 * 2 * 2^15
2 * 2 * 2^15 = 2 * 2 * 2 * 2^14
...
(16 steps)
```

## Triangle

For 3 sides to form a valid triangle, the sum of any 2 sides needs to be greater than the third side. 

`a + b > c` AND `b + c > a` AND `c + a > b`

- [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/description)
