# multithreading = allows program to handle multiple tasks concurrently in a single process(__builtins__)

import threading

import time

done = False


def worker():
    counter= 0
    while True:
        time.sleep(1)
        counter += 1
        print(counter)


threading.Thread(target=worker,daemon=True).start()

worker()

input("press 9 to quit")
done=True
