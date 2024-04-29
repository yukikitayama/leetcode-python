# Bit Manipulation

## Base

- **Base** is a counting system which carries numbers and uses digital symbols and certain rules.
- Each counting system has a base. When the base is `X`, the number on each digit will be carried over when it reaches
  `X`, and we call it `base-X`
- Base-10 is called **decimal**. It's the counting system people use
  - Uses 10 digits from 0 to 9
  - 123.45 can be written in decimal as `123.45 = 1 * 10^2 + 2 * 10^1 + 3 * 10^0 + 4 * 10^-1 + 5 * 10^-2`
- Base-2 is called **binary**. It's often asked in coding interview
  - Uses 2 digits from 0 and 1
- Base-16 is called **hexadecimal**. It's used in color in coding
  - Uses 16 digits from 0 to 9, and A, B, C, D, E and F. 10 corresponds to A. 15 corresponds to F.
- Base-8 is called **octal**.
  - Uses 8 digits from 0 to 7.
  - 720.5 can be written in octal as `720.5 = 7 * 8^2 + 2 * 8^1 + 0 * 8^0 + 5 * 8^-1`

## Convert binary to decimal

- Sum of 1 or 0 multiplied by 2 to the power of digit position
- `110010 = 1 * 2^5 + 1 * 2^4 + 0 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 32 + 16 + 0 + 0 + 2 + 0 = 50` 

## Convert decimal to binary

- Convert the integer part (123 in 123.45) and the fractional part (45 in 123.45) separately with different rule.
- To convert the integer part, keep integer-dividing a number by 2 until it reaches 0 and record the remainder each time. 
  Concatenate the remainders in reverse order.
  - Convert 50 in decimal (base-10) to in binary (base-2), 
  - `50 // 2 = 25 and 50 % 2 = 0`
  - `25 // 2 = 12 and 12 % 2 = 1`
  - `12 // 2 = 6 and 12 % 2 = 0`
  - `6 // 2 = 3 and 6 % 2 = 0`
  - `3 // 2 = 1 and 3 % 2 = 1`
  - `1 // 2 = 0 and 1 % 2 = 1`
  - The remainders in reverse order is `110010`. This is the binary representation of 50.
  - To check, `1 * 2^5 + 1 * 2^4 + 0 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 32 + 16 + 0 + 0 + 2 + 0 = 50`
- To convert the fractional part, keep multiplying only the fractional part by 2 until the fractional part becomes 0 and 
  record the integer part each time. Concatenate the recorded integers.
  - Convert 0.6875 in decimal to binary
  - `0.6875 * 2 = 1.375 and integer: 1`
  - Ignore leading 1 and multiply only the fractional part `0.375 * 2 = 0.75 and integer: 0`
  - `0.75 * 2 = 1.5 and integer: 1`
  - `0.5 * 2 = 1.0 (fractional part became 0) and integer: 1`
  - Concatenate the recorded integers `1011`. `0.1011` is the binary representation fo 0.6875
  - To check, `1 * 2^-1 + 0 * 2^-2 + 1 * 2^-3 + 1 * 2^-4 = 0.5 + 0 + 0.125 + 0.0625 = 0.6875`
- Hence, 50.6875 in decimal is 110010.1011 in binary.

## Convert decimal to non-decimal

- Let `num` denote the given number and `k` is of base-k.
- If `num = 0`
  - Converted number of any base-k is 0
- If `num > 0`
  - Integer divide `num` by `k` until it reaches 0, and record the remainder each time
  - Traverse the remainders in reverse order and concatenate them, which is the representation in base-k system.
- If `num < 0`
  - Base-k representation of `num` is also negative
  - Take absolute value of `num` to remove minus sign
  - Integer divide the `num` by `k` until it reaches 0 and record the remainder each time
  - Traverse the remainders in reverse order, concatenate them and add minus sign to make it negative.

## Computer byte number

- 1-byte number means 8 digits binary number. It has 2^8 possible values, because it has 8 positions for digits and 
  each has 2 options either using 0 or 1.
- 2-byte number is 16 digits binary number. It has 2^16 possible values
- 4-byte number is 32 digits binary number. It has 2^32 possible values
- 8-byte number is 64 digits binary number. It has 2^64 possible values

## Signed integer

- The highest bit represents the sign, so the highest bit is called **sign bit**. The digits other than the highest bit
  are used to represent the size of number.
- When the highest bit is 0, it's non-negative integer
- When the highest bit is 1, it's a negative integer

### 1-byte signed integer (i.e. 8 digits binary number)

- When the highest bit is 0, the 1-byte signed number ranges from 0 to 127 (2^7 - 1)
  - 0 is `00000000`
  - 127 is `01111111`
- When the highest bit is 1, the 1-byte signed number ranges from -128 to -1
  - -128 is `10000000`
  - -1 is `10000001`

### Signed 32-bit integer

the leftmost bit (bit position 31) is the sign bit, where 0 represents positive numbers and 1 represents negative numbers. This leaves only 31 bits for representing the actual numerical value.

### Signed 64-bit integer

the leftmost bit (bit position 63) is the sign bit, where 0 represents positive numbers and 1 represents negative numbers.

## Unsigned integer

- It cannot represent negative numbers because all digits in binary representation are used to represent the size of the
  number.

### 1-byte unsigned integer (i.e. 8 digits binary number)

- It ranges from 0 to 255
  - 0 is `00000000`
  - 255 is `11111111`, 2^8 - 1
- The maximum value of the unsigned integer is twice bigger than the signed integer, because the unsigned integer
  doesn't have to keep one digit for sign bit.

## Machine number

- Machine number is signed number, meaning the highest bit of the machine number is used for a sign
  - Highest bit 0 is non-negative number
  - Highest bit 1 is negative number
- Given a binary number for example `10001010`, converting it to decimal number is `2^7 + 2^3 + 2^1 = 138`, but the
  machine number is `-10` because the highest bit 1 is used for negative number and `2^3 + 2^1 = 8 + 2 = 10`

## Complement code

- The computer uses something called **complement code** for calculations, because complement code has advantages over
  something called **original code** and **inverse code**.
- Original code is machine code
- Inverse code of non-negative numbers is the same as original code. The inverse code of negative number is to flip
  every bit of the original code except the sign bit
- Complement code of non-negative numbers is the same as original code and inverse code. The complement code of
  negative numbers is obtained by adding 1 to the inverse code.

## Bit operations

### AND &

- When both bits are 1, result is 1, otherwise 0

### OR |

Properties of bitwise **OR**
- When both bits are 0, result is 0, otherwise 1
  - Returns 1 if at least one of the corresponding bits in the operands is 1
- Associative, meaning `(a | b) | c = a | (b | c)`
- Commutative, meaning `a | b = b | a`
- **Idempotent**, meaning `a | a = a`

### XOR ^

- When both bits are the same, result is 0, otherwise 1

### Negation ~

- 0 becomes 1, and 1 becomes 0
- ~ 0 = 1
- ~ 1 = 0

### Left shift

- Shift all the binary bits to the left, discard the highest bit, and fill the lowest bit with 0.
- Example of signed 8-bit binary number
  - Use 29. The binary representation is `00011101`.
  - Left shift of 29 by 2 bits is 116, because of `01110100`.
  - Left shift of 29 by 3 bits is -104, because `11101000` and, in signed integer, the highest bit is sign bit, so 
    highest bit `1` indicates the integer is negative integer, and `1101000` is 104.
- Left shift operation corresponds to multiplication.
  - Shifting a number to the left by `k` bits is equal to multiplying the number by `2^k`.
  - Left shift of 29 by 2 bits is 116. `2^k = 2^2 = 4`, and `4 * 29 = 116`.

### Right shift

- Shift all the binary bits to the right, discard the lowest bit, but there are different ways to fill the highest bit.
- Fill the highest bit with the existing highest bit. This is called **arithmetic shift**
- Fill the highest bit with 0. This is called **logical shift**
- Example of signed 8-bit binary number
  - Use -50. The binary representation is `11001110`.
  - Arithmetic right shift of -50 by 2 bits is -115, because the highest bit of -50 is `1` and arithmetic shift repeats
    this bit, so `11110011`
  - Logical right shift of -50 by 2 bits is 51, because logical shift fills with 0 so `00110011`.
- Arithmetic right shift operation corresponds to division.
  - For non-negative numbers, arithmetic right shift of a number by `k` digit is equal to integer division by `2^k`.
  - For negative numbers, integer division is rounded to 0, but right shift is rounded down.
    - `-50 >> 2 = -13`, but `-50 / (2^2) = -50 / 4 = -12.5`, but in Python `-50 // 4 = -13`.

## Properties of bitwise operations

Using these properties, many bit operation problems can be solved strategically.

xxx

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
  - ANDing the two numbers `n` and `n - 1` always flips the least significant 1-bit in `n` to 0, and keeps all other 
    bits the same
- [231. Power of Two](https://leetcode.com/problems/power-of-two/)
- [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

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
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
  - Use integer as bit mask
- [2505. Bitwise OR of All Subsequence Sums](https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/description)

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

## Multiply and Divide by 2

- People say `bitwise shift` is faster than multiplication and division.
- `x * 2` is the same as `x << 1` left shift.
  - e.g. `x: 2`, its bin is `10`, `x << 1` is `100`, which is `4`.
- `x / 2` is the same as `x >> 1` right shift.