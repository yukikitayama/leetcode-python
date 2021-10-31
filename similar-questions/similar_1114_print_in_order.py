import threading


class Foo:
    def __init__(self):
        self.first_job_done = threading.Lock()
        self.second_job_done = threading.Lock()
        # Initialize both locks to be locked to allow context manager with statement to work
        self.first_job_done.acquire()
        self.second_job_done.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()

        self.first_job_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_job_done:
            printSecond()

            self.second_job_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_job_done:
            printThird()
