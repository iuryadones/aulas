"""
    Minha primeira lib em python

"""

def fibonacci(n):
    """
        fibonacci(int n) -> serie de fib
    """
    a ,b = 0, 1
    try:
        for i in range(n):
            yield b
            a,b = b, a+b
    except:
        print("Erro")

if __name__ == '__main__':
    fib = fibonacci
    for el in fib(100):
        print(el)
