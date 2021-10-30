"""
https://www.geeksforgeeks.org/synchronization-pooling-processes-python/
"""


import multiprocessing


def deposit(balance):
    for _ in range(10000):
        balance.value = balance.value + 1


def withdraw(balance):
    for _ in range(10000):
        balance.value = balance.value - 1


def deposit_lock(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def withdraw_lock(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


def main_1():

    balance = multiprocessing.Value('i', 100)

    p1 = multiprocessing.Process(target=deposit, args=(balance,))
    p2 = multiprocessing.Process(target=withdraw, args=(balance,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Final balance: {balance.value}')


def main_2():

    balance = multiprocessing.Value('i', 100)

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=deposit_lock, args=(balance, lock))
    p2 = multiprocessing.Process(target=withdraw_lock, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Final balance: {balance.value}')


if __name__ == '__main__':
    for _ in range(10):
        main_1()
    print()

    for _ in range(10):
        main_2()
    print()
