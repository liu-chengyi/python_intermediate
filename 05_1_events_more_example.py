import threading
import time

data_ready = threading.Event()
shared_data = None

def worker():
    print("Worker waiting for data...")
    data_ready.wait()  # Block until .set() is called
    print("Worker received signal, processing data: {}".format(shared_data))

def producer():
    global shared_data
    time.sleep(2)
    shared_data = "Important data"
    print("Producer has set the data.")
    data_ready.set()  # Signal the worker to continue

threading.Thread(target=worker).start()
threading.Thread(target=producer).start()