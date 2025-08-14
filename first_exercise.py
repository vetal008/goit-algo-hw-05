def caching_fibonacci(cache=dict()):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


if __name__ == '__main__':
    fib = caching_fibonacci()
    print(fib(10))



