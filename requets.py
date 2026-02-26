# multithreading = allows program to handle multiple tasks concurrently in a single process(__builtins__)

import threading

import time

done = False

def worker():
    global done
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

threading.Thread(target=worker, daemon=True).start()

input("press 9 to quit: ")
