import functools
@functools.lru_cache(maxsize=None)
def fibonacci(number):
    if number==1:
        return 0
    elif number==2:
        return 1
    elif number==3:
        return 1
    return fibonacci(number-3)+fibonacci(number-1)

N=int(input())
print(fibonacci(N+1))