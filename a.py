def h():
    print 'hello world!'


import threading
t = threading.Thread(target=h)
t.start()
