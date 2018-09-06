def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def tail_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_factorial(n - 1, accumulator * n)


def fat_stack_recursion(x):
    if x == 0:
        return 1
    else:
        return x * fat_stack_recursion(x - 1)


def tail_aux_fat(x, y):
    if y == 0:
        return x
    return tail_aux_fat(x * y, y - 1)


def fat_tail_recursion(y):
    return tail_aux_fat(1, y)


if __name__ == "__main__":
    num = 5

    import time

    init = time.time()
    print(factorial(num))
    end = time.time()
    print(f"Time factorial: {end-init:2.4e}")

    init = time.time()
    print(tail_factorial(num))
    end = time.time()
    print(f"Time tail_factorial: {end-init:2.4e}")

    init = time.time()
    print(fat_stack_recursion(num))
    end = time.time()
    print(f"Time fat_stack_recursion: {end-init:2.4e}")

    init = time.time()
    print(fat_tail_recursion(num))
    end = time.time()
    print(f"Time fat_tail_recursion: {end-init:2.4e}")
