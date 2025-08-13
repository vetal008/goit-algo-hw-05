def caching_fibonacci(cache={}):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            print(f'{n} in cache')
            return cache[n]
        print(f'{n} -> {fibonacci(n - 1)}')
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


if __name__ == '__main__':
    fib = caching_fibonacci()
    print('---------')
    print(fib(10))
    print('---------')
    print(fib(6))



