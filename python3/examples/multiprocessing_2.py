import multiprocessing as mp


def job(_id, c):
    print(f"Testando id {_id}")
    q.put(c)


if __name__ == "__main__":
    q = mp.Queue()

    p1 = mp.Process(target=job, args=(1, 5))
    p2 = mp.Process(target=job, args=(2, 6))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(q.get())
    print(q.get())

