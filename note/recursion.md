## Recursion

- Solve problems using a functions that calls itself.
- `Base case (bottom case)` is the case where one can compute the answer directly without any further recursion calls.
  - Something to stop recursion.
- `Execution tree` is used to find time complexity in recursion
  - Each node represents recursive function call.
  - Total number of nodes in the tree is the number of recursion calls, which is time complexity.
- `Stack overflow` is where the stack allocated for recursion reaches its maximum space limit and the program crashes. 
- Space allocated by the recursion stack
  - Returning address of function call, i.e. the line of code to return after a function call is completed.
  - Parameters passed to the function call
  - Local variables in the function call
- `Tail recursion` is a recursion where the recursive call is the final instruction in the recursion function, no other 
  computations at the end of the function, and there should be only one recursive call in the function.
  - Benefit of tail recursion is that it allows to `reuse a fixed amount space` in the recursion stack to save space by 
    avoiding accumulating the stacks.
  - So tail recursion is used to avoid `stack overflow`.
  - Tail recursion also makes things easier to read and understand, compared to non-tail-recursion.
  - It doesn't need a call stack for all the recursive calls, because, as soon as it returns from a recursive call, 
    immediately go to return to the original caller.
  - Non-tail-recursion functions are not automatically optimized by Python and Java. But C and C++ recognizes tail 
    recursion pattern and automatically optimizes the execution.
    - [Optimizing tail-recursion in Python](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion)

```python
def tail_recursion(nums):
    def recursion(nums, accumulator):
        if len(nums) == 0:
            return accumulator
        # recursion() is a tail recursion 
        # because the final instruction is only a recursive call
        return recursion(nums[1:], nums[0] + accumulator)
    return recursion(nums, 0)

def not_tail_recursion(nums):
    if len(nums) == 0:
        return 0
    # not_tail_recursion() is not a tail recursion 
    # because it needs to add the result of recursion to nums[0] as an extra computation,
    # so the final instruction is not only a recursive call
    return nums[0] + not_tail_recursion(nums[1:])
```
