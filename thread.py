
# import  threading
import random
import time
from threading import Thread

class Resourse:

    def __init__(self):
        self.value = 1

class NumberPrinter(Thread):

    def __init__(self, thread_id, resourse):
        # init smth for thread
        Thread.__init__(self)
        # your job
        self.thread_id = thread_id
        self.resourse = resourse

    def run(self):

        number = random.randint(1,5)
        time.sleep(number)


        self.resourse.value = self.resourse.value+1
        print("thread", self.name, "is running with number", number, "value", self.resourse.value)

#  RUN FEW THREADS

resource = Resourse()
for i in range(20):
    thread = NumberPrinter(i,resource)
    thread.start()
    # thread.join()

# print("Finish:", resource.value)