import threading
 
def function1():
    for x in range (100):
        print("ONE")

def function2():
    for x in range (100):
        print("TWO")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()

# indicate do not continue to the rest of the code untill the threading is finished
t1.join()
t2.join()

print("你好")