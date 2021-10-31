import threading


lock_1 = threading.Lock()

with lock_1:
    print('Lock is not blocked.')

lock_2 = threading.Lock()
lock_2.acquire()

lock_2.release()

# This continue for ever until another thread releases()
with lock_2:
    print('This will not be printed if it is locked')

