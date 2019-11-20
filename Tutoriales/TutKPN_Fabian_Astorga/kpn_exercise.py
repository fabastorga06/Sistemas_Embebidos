from threading import Thread
import queue, time

a_k = queue.Queue()
b_k = queue.Queue()
c_k = queue.Queue()
d_k = queue.Queue()
e_k = queue.Queue()
f_k = queue.Queue()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def add_process():
    while(True):
        c_data = c_k.get()
        f_data = f_k.get()
        a_k.put(c_data + f_data)

def delay0_process():
    f_k.put(0)
    while(True):
        a_data = a_k.get()
        b_k.put(a_data)

def delay1_process():
    b_k.put(1)
    while(True):
        e_data = e_k.get()
        f_k.put(e_data)

def split_process():
    while(True):
        b_data = b_k.get()
        c_k.put(b_data)
        d_k.put(b_data)
        f_k.put(b_data)
        d_data = d_k.get()
        time.sleep(1)
        print(d_data)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():
    thread_add = Thread(target=add_process)
    thread_delay0 = Thread(target=delay0_process)
    thread_delay1 = Thread(target=delay1_process)
    thread_split = Thread(target=split_process)    

    thread_add.start()
    thread_delay0.start()
    thread_delay1.start()
    thread_split.start()

main()