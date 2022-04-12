"""
- 5 threads will simultaneously use one object of this class
- Deadlock happens if 5 forks are picked up, 1 for each philosopher
- Enforce at most 4 philosopher can approach the table
"""


from threading import Semaphore


class DiningPhilosophers:

    def __init__(self):
        self.sizelock = Semaphore(4)
        self.locks = [Semaphore(1) for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # e.g. philosopher: 2, left: 2, right: 1
        # philosopher: 0, left: 0, right: 4 (-1 % 5 = 4)
        left = philosopher
        right = (philosopher - 1) % 5

        with self.sizelock:
            with self.locks[left], self.locks[right]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
