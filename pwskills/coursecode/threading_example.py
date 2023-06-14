
import time
"""def test(id):
    for i in range(10):
        print("test %d printing %d"%(id,i))
        time.sleep(1)

#test(1)"""

import threading
"""def test(id):
    for i in range(10):
        print("test %d printing %d , %s" %(id,i,time.ctime()))
        time.sleep(1)

#now use threading to run fuction for multiple id's
thread=[threading.Thread(target=test,args=(i,))for i in range(3)]
print(thread)
for i in thread:
    i.start()
"""

shared_val=0
lock_var=threading.Lock()

def test3(id):
    global shared_val
    with lock_var:
        shared_val=shared_val+1
        print("lock variable id = %d incese shared var = %d"%(id,shared_val))
        time.sleep(3)
#test3(3)
#test3(2)
#test3(4)

#now using treading pass at a time multiple ids
thread=[threading.Thread(target=test3,args=(i,))for i in range(4)]
print(thread)

for i in thread:
    i.start()