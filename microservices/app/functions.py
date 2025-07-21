from functools import lru_cache

#for routes
@lru_cache(maxsize=128)
def nth_fibonacci(n):
    if n<=1:
        return n

    return nth_fibonacci(n-1) + nth_fibonacci(n-2)

@lru_cache(maxsize=128)
def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
        print(res)
    return res

@lru_cache(maxsize=128)
def poww(n,p):
    if p==0:
        return 1
    initial_n = n
    for i in range(1, p):
        n *= initial_n
    return n



#for logging
