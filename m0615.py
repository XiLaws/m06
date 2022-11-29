import multiprocessing
import random
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
def process(num):
    time.sleep(random.randrange(1,11))
    print('process:' + str(num) + ' completed at '+ current_time)
    return

if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=process, args=(i,))
        processes.append(p)
        p.start()

    while len(processes) > 0:
        processes = [task for task in processes if task.is_alive()]
        time.sleep(1)

    print('All processes completed.')