# Concurrency

- `Semaphore(2)` means a thread can acquire up to 2
- `Barrier(3)` means it needs wait 3 threads
- [Using locks, conditions, and semaphores in the with statement](https://docs.python.org/3.8/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement)

```python
from threading import Semaphore

sem = Semaphore(2)

with sem:
    pass
```

- [1226. The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/)
- [1117. Building H2O](https://leetcode.com/problems/building-h2o/description/)