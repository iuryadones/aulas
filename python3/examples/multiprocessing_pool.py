import multiprocessing as mp
import os

def square(x):
    return x ** 2

def pool_map():
    pool = mp.Pool(processes=4)
    result = pool.map(square, range(1000))
    print(result)
    pool.close()
    pool.join()

def pool_map_async():
    pool = mp.Pool(processes=4)
    result = pool.map_async(square, range(1000))
    print(result.get())
    pool.close()
    pool.join()

def pool_imap():
    pool = mp.Pool(processes=4)
    result = pool.imap(square, range(1000))
    print([r for r in result])
    pool.close()
    pool.join()

def pool_methods():
    pool = mp.Pool(processes=4)
    [print(d) for d in dir(pool) if not d.startswith('_')]
    pool.close()
    pool.join()

def cpu_count():
    core = os.cpu_count() // 2
    cpu = os.cpu_count()

    print(f'Core: {core}')
    print(f'CPU: {cpu}')

if __name__ == "__main__":
    cpu_count()
    pool_methods()
    pool_map()
    pool_map_async()
    pool_methods()
    pool_imap()
