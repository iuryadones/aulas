import multiprocessing as mp
import time


def job(v, num, l=None):
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)

def multicore():
    v = mp.Value('i', 0)

    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 5))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def chronometer(f):
    start = time.time()
    f()
    end = time.time() - start
    print(f'{f.__name__} {end:.4f}', end='\n\n')

if __name__ == "__main__":
    chronometer(multicore)
