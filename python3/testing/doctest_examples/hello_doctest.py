def print_hello_world(word="world"):
    """
        >>> print_hello_world()
        hello world
        >>> print_hello_world('John')
        hello John
    """

    print("hello " + word)


if __name__ == "__main__":
    """
        execute_script:
            python hello_doctest.py

        execute script verbose:
            python hello_doctest.py -v

        execute script verbose:
            import doctest
            doctest.testmod(verbose=True)
    """

    import doctest

    doctest.testmod(verbose=True)
