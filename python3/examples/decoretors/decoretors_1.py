def cached(f):
    """Retorna uma funcao igual a 'f' mas com um cache associado.

    Note que esta função *não* funciona com keyword arguments.
    """

    def g(*args):
        if args not in g.cache:
            g.cache[args] = f(*args)
        return g.cache[args]

    g.cache = {}
    g.__doc__ = f.__doc__
    g.__name__ = f.__name__
    return g


@cached
def test(number):
    return number ** 2


def main():
    print(test(10))
    print(test(10))
    print(test(10))
    print(test(9))
    print(test(9))


if __name__ == "__main__":
    main()
