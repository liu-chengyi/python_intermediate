import threading
import time

# semaphore help limit the access to the resource (say 5 functions)
semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    print("{} is now releasing!".format(thread_number))
    semaphore.release()

for thread_number in range (1, 11):
    t = threading.Thread(target=access, args=(thread_number,)) # note the args here expects the input being a tuple so need a comma at the end
    t.start()
    time.sleep(1)