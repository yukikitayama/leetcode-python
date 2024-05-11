# Sorting

## Bucket sort (Bin sort)

- Sorting algorithm to achieve time complexity `O(N)`
- Items are placed at array indexes based on their value.
- Indexes are called `buckets`
- [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

## Counting Sort

- Time is `O(N)` to iterate the given array
- `K` is value range of array. Space is `O(K)` to create an auxiliary array from the given array.
- Good choice if the value range of an array is small compared with the scale of the array
  - e.g. `1 <= array length <= 10^5` but `1 <= array[i] <= 100`
- We need to know the value range in advance to implement counting sort.
- [506. Relative Ranks](https://leetcode.com/problems/relative-ranks/description)

### Algorithm

- Make an empty auxiliary array `counter`
- Iterate the given array and get each element as `value`
- Increment the auxiliary array by the array element as index such as `counter[value]`

## LeetCode

- [1874. Minimize Product Sum of Two Arrays](https://leetcode.com/problems/minimize-product-sum-of-two-arrays/)
- [1833. Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/description/)