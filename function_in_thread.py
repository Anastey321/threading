import threading

resourse = 0
lock = threading.Lock()


def update(new_value):
    global resourse

    with lock:
        resourse += new_value

    print(resourse)


for i in range(100):
    thread = threading.Thread(target=update, args=(100, ) )
    thread.start()