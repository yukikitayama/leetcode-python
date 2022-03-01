# Bit Manipulation

## Two's Complement

- To compute two's complement notation -x, revert all bits in x, and add 1
- x = 7: 0 0 0 0 0 1 1 1, ~x: 1 1 1 1 1 0 0 0, ~x + 1: 1 1 1 1 1 0 0 1
- x = 6: 0 0 0 0 0 1 1 0, ~x: 1 1 1 1 1 0 0 1, ~x + 1: 1 1 1 1 1 0 1 0

## Get the Rightmost 1-bit

- `x & (-x)`
  - `-x` is two's complement
- [231. Power of Two](https://leetcode.com/problems/power-of-two/)

| Code | Binary representation |
|------|-----------------------|
| x = 7 | 0 0 0 0 0 1 1 **1** |
| -x = ~x + 1 | 1 1 1 1 1 0 0 **1** |
| x & (-x) | 0 0 0 0 0 0 0 **1** |

## Turn Off the Rightmost 1-bit (Zeroing Out Least Significant Nonzero Bit)

- `x & (x - 1)`
  - Subtracting 1 means changing the rightmost 1-bit to 0, and setting all the lower bits to 1, and then 1 & 0 = 0.
- [231. Power of Two](https://leetcode.com/problems/power-of-two/)

| Code | Binary representation |
|------|-----------------------|
| x = 4 | 0 0 0 0 0 **1** 0 0 |
| x - 1 | 0 0 0 0 0 **0** 1 1 |
| x & (x - 1) | 0 0 0 0 0 **0** 0 0 |

## Check Whether a Number is the Power of 2

- `if (x & (x - 1)) == 0`
  - `x` and `x - 1` have different bits in all of their bits, so AND yields 0.

| Action | Binary representation |
|--------|-----------------------|
| x = 4 | 1 0 0 |
| x - 1 = 3 | 0 1 1 |
| x & (x - 1) | 0 0 0 |

## XOR

- Use `A ^ B` in Python
- XOR truth table

| Input A | Input B | Output |
|---------|---------|--------|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

- It can be used to flip `False` to `True`, or `True` to `False`, by always `^ True` to something.
  - If `flag` is `False`, `flag ^= True` is `True`.
  - If `flag` is `True`, `flag ^= True` is `False`. 

### Problems

- [67. Add Binary](https://leetcode.com/problems/add-binary/)
- [137. Single Number II](https://leetcode.com/problems/single-number-ii/)
- [260. Single Number III](https://leetcode.com/problems/single-number-iii/)
- [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
- [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)
- [318. Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/)
- [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
  - `XOR` plus `Trie`

## 1-bits Bitmask

- In binary representation, all the bits are 1, like `111`.
- To flip bits in a given number

| Action | Binary representation |
|--------|-----------------------|
| Given number: 5 | 1 0 1 |
| 1-bits bitmask | 1 1 1 |
| Number ^ bitmask | 0 1 0 |

- Make 1-bits bitmask
  - Get the number of digits in binary representation of a given number
  - Left-shift 1 the above number of times to give us 1 followed by multiple 0s
  - Subtract 1 to give us all the above 0s become 1s, which is 1-bits bitmask.
- `INTEGER.bit_length()` is a built-in function to get the length of bits or digits.

```python
import math
# Replace num with your given number
num = 5  # 101 in binary representation
number_of_digits = math.floor(math.log2(num)) + 1  # 3
one_bits_bitmask = (1 << number_of_digits) - 1  # 111

# Built-in function
num.bit_length()  # 3
```

## Carry

- `(a & b) << 1`
- AND (`&`) finds the common 1-bit, and left-shift (`<<`) moves the carry to the next bit position

| Action | Binary representation |
|--------|-----------------------|
| a | 1 1 1 1 |
| b | 0 0 1 0 |
| (a & b) << 1| 0 1 0 0 |

## Create a binary number from the most significant bit

- `(previous bit << 1) | current bit`
  - e.g. Previous bit: 1, current bit: 1, the result needs to be 11, which is 3 in binary representation.
  - `1 << 1` gives us `10`. `10 | 1` gives us `11`. It's 3.
- `previous digit * 10 + current digit` is the equivalent in decimal representation
  - e.g. Make 12, previous digit: 1, current digit: 2, 10 + 2 = 12

## Zero Left-Padding

- `[(DECIMAL_NUMBER >> i) & 1 for i in range(BIT_LENGTH)]`
- Standardize the number of bits for numbers
- e.g. `bin(3) = '0b11' -> '11'`. `bin(25) = '0b11001' -> '11001'`. The length of bits is different
- The goal of zero left-padding is to make `[1, 1, 0, 0, 1]` from `5`, and `[0, 0, 0, 1, 1]`.
  - First find the maximum length of bits, then make all the binary forms have the same length, and then store them in a
    list.

```python
# -2 because bin() returns extra '0b' in front of binary numbers
l = len(bin(max(3, 25))) - 2
binaries_25 = []
for i in range(l):
    # (25 >> i) & 1 gets the bits from the right
    binaries_25.append((25 >> i) & 1)

# Reverse it because we store bit from the right, but we wanna see bits from the left
binaries_25.reverse()

binaries_3 = []
for i in range(l):
    # bin(3) is '0b11', so when i is 0 and 1, it gets 1,
    # but for i >= 2, 3 >> i is always 0, so it successfully appending additional 0s for length l
    binaries_3.append((3 >> i) & 1)

# Reverse it because we store bit from the right, but we wanna see bits from the left
binaries_3.reverse()
```

## Filter a Character

- Use `XOR`
- Filter out the same character and find out the extra character in the other
  - `s: 'a', t: 'ae'`
  - XOR `s[0] ^ t[0]` returns `0`
  - XOR `0 ^ t[1]` return `ord(t[1])`
  - Back to character by `chr(ord(t[1]))`
- [389. Find the Difference](https://leetcode.com/problems/find-the-difference/)