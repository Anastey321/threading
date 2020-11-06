import  threading
from queue import Queue

def create_event(events, queue):
    for event in events:
        print("New event", event)

        thread_notification = threading.Event()

        queue.put( (event, thread_notification)  )


def consum_event(queue):
    while True:
        event,  thread_notification = queue.get()
        print(event, "processed")

        thread_notification.set()

        queue.task_done()


events = [
     [45,2,45,2,42,2,1],[45,6,2,2,5,47,4,3,2,35,3,235]
]

queue = Queue()




thread_consum_event1 = threading.Thread(target=consum_event, args=(queue,))
thread_consum_event1.start()
thread_consum_event2 = threading.Thread(target=consum_event, args=(queue,))
thread_consum_event2.start()


for event_pull in events:
    thread_event_creator = threading.Thread(target=create_event, args=(event_pull,queue) )
    thread_event_creator.start()

queue.join()

print("Finish")