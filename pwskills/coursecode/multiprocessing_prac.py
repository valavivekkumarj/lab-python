import multiprocessing

##multiprocessing with processes

def test():
    print("this is my test programe")

if __name__=='__main__':   #main programe of python which have all resources of python 
    m=multiprocessing.Process(target=test) #here  both programe run simultaneslly
    print("this is my main programe")
    m.start()     #this start is used to execute child process of main programe
    m.join()        #join can free all resources after child process execute and give to main programe


#multiprocessing with pool
def square_of_n(n):
    return n**2

if __name__=='__main__':
    with multiprocessing.Pool(processes=5) as pool: #using pool we can process at a time multiple data
        #it divide data and use in multiple processe at a time so fast executation happen
        out=pool.map(square_of_n,[1,2,3,4,5])
        print(out)


        #######################################################################################
        #multiprocessing using queue
def produce(q):
    for i in range(10):
        q.put(i)

def consume(q):
    while True:
        item=q.get()
        if item==None:
            break
        print(item)

if __name__=='__main__':
    queue=multiprocessing.Queue()
    m1=multiprocessing.Process(target=produce,args=(queue,))
    m2=multiprocessing.Process(target=consume,args=(queue,))
    m1.start()
    m2.start()
    m1.join()
    m2.join()


