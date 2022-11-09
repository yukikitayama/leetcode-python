# Stack

## Monotonic stack

A stack in which the elements are always sorted. A stack can be monotonically increasing (sorted ascending) or 
monotonically decreasing (sorted descending)

In monotonic decreasing stack, If we want to push `x`, then all elements that are less than `x` are popped 
off first to maintain the sorted property. 

For example, if we have `stack = [4, 2, 1]` and we want to push `3`, then the `2` and `1` must be popped before the `3` 
is pushed, otherwise the stack will no longer be sorted.