cube = lambda x:x**3
def fibonacci(n):
    fib_list = []
    n1, n2 = 0, 1
    for i in range(n):
        fib_list.append(n1)
        n1, n2 = n2, n1 + n2
    return fib_list
n = int(input())
print(list(map(cube, fibonacci(n))))