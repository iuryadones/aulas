import multiprocessing as mp


def square(x):
    return x ** 2

def main():
    pool = mp.Pool(4)
    result = pool.map(square, range(1000))
    pool.close()
    pool.join()

    print(res)


if __name__ == "__main__":
    main()

