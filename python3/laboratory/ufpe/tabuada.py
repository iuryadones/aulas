N = int(input("Digite a quantidade da serie de fib: "))

fib = [0,1,1]

for i in range(3,N):
    fib += [fib[i-1] + fib[i-2]]
    print(fib[i]/fib[i-1])

for seq in fib:
    print(seq)
