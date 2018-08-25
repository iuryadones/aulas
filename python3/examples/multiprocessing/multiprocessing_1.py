import multiprocessing as mp
import threading as td


def job(a, b):
    print(f"Testando {a} {b}")


if __name__ == "__main__":
    p = mp.Process(target=job, args=(1, 2))
    p.start()
    p.join()

    t = td.Thread(target=job, args=(3, 4))
    t.start()
    t.join()
