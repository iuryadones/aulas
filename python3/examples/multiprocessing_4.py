import multiprocessing as mp
import time


def job(x):
    return x * x


def multicore():
    pool = mp.Pool(4)

    results = pool.map(job, range(10 ** 2))
    print(results)

    result = pool.apply_async(job, (10,))
    print(result.get())

    results = [pool.apply_async(job, (i,)) for i in range(10 ** 2)]
    print([res.get() for res in results])

    pool.close()
    pool.join()


def chronometer(f):
    start = time.time()
    f()
    end = time.time() - start
    print(f"{f.__name__} {end:.4f}", end="\n\n")


if __name__ == "__main__":
    chronometer(multicore)
