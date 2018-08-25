def soma(valor_x=None, valor_y=None):
    """
        >>> soma(5,5)
        10
        >>> soma(2,1)
        3
        >>> soma()
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
        >>> soma(2,[])
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for +: 'int' and 'list'
    """

    print(valor_x + valor_y)


if __name__ == "__main__":
    """
        execute_script:
            python calculadora_doctest.py

        execute script verbose:
            python calculadora_doctest.py -v

        execute script verbose:
            import doctest
            doctest.testmod(verbose=True)
    """

    import doctest

    doctest.testmod(verbose=True)
