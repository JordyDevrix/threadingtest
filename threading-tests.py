import threading
import time

done = False


def worker(valu):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(valu)


value = 0

while True:
    t1 = threading.Thread(target=worker, args=(value, ))
    t1.start()
    value = input('Press enter to quit')
    done = True
    t1.join()
    done = False
