import multiprocessing as mp
import threading as td
import numpy as np

def job(mat, a, b):
    print(f"Sum: {mat.sum()}")
    print(f"Mean: {mat.mean()}")

if __name__ == "__main__":
    mu = 0
    sigma = 0.1
    matrix = np.random.normal(mu, sigma, (2,2))
    io.imshow(matrix)
    io.show()

    io.imsave('matrix.png', matrix)

    matrix_read = io.imread('matrix.png')
    io.imshow(matrix_read)
    io.show()

    lista_p = []
    for i in range(0,4):
        for j in range(0,4):
            lista_p.append(
                mp.Process(target=job,
                           args=(matrix, i, j)))
    for p in lista_p:
        p.start()

    for p in lista_p:
        p.join()
