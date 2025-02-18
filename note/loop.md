# Loop

## While break else

`while` loop can use with `else`. When the `while` condition no longer is true, a block of code after `else` statement 
runs once.

However, when `break` is used in `while`, `else` block won't be executed. So `else` clause is executed if you exit a 
block normally, like not by `break`, `return`, raise an exception.

https://stackoverflow.com/questions/3295938/else-clause-on-python-while-statement

- [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/description/)

```
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1
else:
    print("Loop finished normally")
# Output:
# Counter: 0
# Counter: 1
# Counter: 2
# Loop finished normally
```

```
counter = 0
while counter < 3:
    print("Counter:", counter)
    if counter == 1:
        break
    counter += 1
else:
    print("Loop finished normally")
# Output:
# Counter: 0
# Counter: 1
```