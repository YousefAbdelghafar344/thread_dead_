import threading
import time

resource_1 = threading.Lock()
resource_2 = threading.Lock()

def thread_1():
    with resource_1:
        print("thread 1 accquire res 1")
        time.sleep(1)
        print("thread 1 waiting for res 2")
    with resource_2:
        print("thread 1 accquire res 2 complete")
            
def thread_2():
    with resource_2:
        print("thread 2 accquire res 2")
        time.sleep(1)
        print("thread 2 waiting for res 1")
        with resource_1:
            print("thread 2 accquire res 1 compete")

a = threading.Thread(target=thread_1)
b = threading.Thread(target=thread_2)

a.start()
b.start()






