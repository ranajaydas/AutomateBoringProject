import threading
import time
print('Start of program.')


def takenap():
    time.sleep(5)
    print('Wake up!')


# The first thread starts
thread_obj = threading.Thread(target=takenap)
thread_obj.start()


# Another thread runs itself
thread_obj2 = threading.Thread(target=print,
                               args=['Cats', 'Dogs', 'Frogs'],
                               kwargs={'sep': ' & '})
thread_obj2.start()
