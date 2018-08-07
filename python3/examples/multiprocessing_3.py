import multiprocessing as mp
import threading as td
import time


def job(q):
    result = 0
    for i in range(10 ** 6):
        result += i
    q.put(result)


def multicore():
    print("Testando multicore")
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    result = q.get() + q.get()
    print(f"core result: {result}")


def multithread():
    print("Testando multithread")
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    result = q.get() + q.get()
    print(f"thread result: {result}")


def normal_count():
    print("Testando normal_count")
    result = 0
    for _ in range(2):
        temp = 0
        for i in range(10 ** 6):
            temp += i
        result += temp
    print(f"normal_count result: {result}")


def normal_sum_list_1():
    print("Testando normal_sum_list_1")
    result = sum((i for i in range(10 ** 6) for _ in range(2)))
    print(f"normal_sum_list result: {result}")


def normal_sum_list_2():
    print("Testando normal_sum_list_2")
    result = sum(range(10 ** 6)) + sum(range(10 ** 6))
    print(f"normal_sum_list result: {result}")


def chronometer(f):
    start = time.time()
    f()
    end = time.time() - start
    print(f"{f.__name__} {end:.4f}", end="\n\n")


if __name__ == "__main__":
    chronometer(multicore)
    chronometer(multithread)
    chronometer(normal_count)
