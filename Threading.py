# lesson 44 Threading
# multiple tasks at one time

import threading
from queue import Queue
import time

## a lock per shared variable or shared function
print_lock = threading.Lock()


def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, worker)


## assigning a worker to a thread
## this is the job
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()




q = Queue()
## the number of workers is 10
## each thread has one worker
for x in range(10):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()

## creating 20 jobs
for worker in range(20):
    q.put(worker)
## wait for thread to terminate
q.join()

print('Entire job took: ', time.time() - start)


