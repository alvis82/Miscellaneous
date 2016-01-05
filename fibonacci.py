#!/usr/bin/env python

import math

# This is a naive recursive approach to calculate the nth fibonacci numbers.
# The time complexity of this method is exponential which is O(2^n). And this
# method will also use up to O(n) stack space which will cause stack overflow
# when n is too large, such as 1000. Hence the performance of this method is
# really bad. When n is too large, it even can not calculate.
def fib_by_recursive(n):
    if n < 0:
        raise ValueError("n must not be negative.")
    
    if n <= 1:
        return n
    else:
        return fib_by_recursive(n - 1) + fib_by_recursive(n - 2)

# This is an improved iterative approach which will take O(n) time complexity
# and O(1) space complexity. The performance of this method is good when n isn't
# very large. The only problem is it doesn't store all the fib numbers between
# 1 to n - 1. So if it is called several times, the performance will decrease.
def fib_by_loop(n):
    if n < 0:
        raise ValueError("n must not be negative.")

    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b

# This method has the same time complexity as the iterative approach which is
# O(n). The space complexity is O(n) as well because it will store every fib
# numbers. This method is useful when a sequence of fib numbers is required.
def fib_by_dp(n):
    if n < 0:
        raise ValueError("n must not be negative.")

    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs

# This is a decorator for fib_by_cache. It provides a cache for store the first
# n fibonacci numbers.
def cache_for_fib(func):
    cache = {0: 0, 1: 1}

    def inner(n, cached = cache):
        return func(n, cached)

    return inner

# This method provide an amortized O(1) time complexity when calculate a series
# of fib numbers. Its space complexity is O(n). This method encapsulates a cache
# to store all fib numbers being calculated so far. And the user doesn't need to
# know how those numbers are stored.
@cache_for_fib
def fib_by_cache(n, cache):
    if n < 0:
        raise ValueError("n must not be negative.")

    if n not in cache:
        for i in range(len(cache), n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]

# This method is based on the fact (fn+1, fn)^T = [[1,1],[1,0]]^n * (f1, f0)^T.
# To calculate x to the power y, the divide and conquer can be used. Hence the
# time complexity of this method is O(logn) and the space complexity is O(1).
# The performance of this method will be worse than the iterative approach due
# to this method requires more calculation in each iteration. But when n grows,
# the performance will be more and more better due to logarithmic complexity.
def fib_by_matrix(n):
    if n < 0:
        raise ValueError("n must not be negative.")

    if n <= 1:
        return n
    
    a, b, c = 1, 1, 0
    for i in bin(n)[3:]:
        tmp = b ** 2
        a, b, c = a ** 2 + tmp, a * b + b * c, tmp + c ** 2
        if i == '1':
            a, b, c = a + b, a, b

    return b

# This method is based on Binet's Fibonacci Number Formula. The time complexity
# depends the time complexity of the buildin power function which normally is
# O(logn). The space complexity is O(1). The performance is better than any
# methods above because it can directly calculate the nth fib numbers. But due
# to the precision problem of how the float numbers are represented in computer,
# we will not get the precise fib number when n is large. And when n grows too
# large, this method cannot work due to the float overflow.
def fib_by_binet(n):
    if n < 0:
        raise ValueError("n must not be negative.")

    sqrt5 = math.sqrt(5)
    return int((((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n) / sqrt5)

# This method provide a better performance than above method by approximation.
# The methods works because the second part of the dividend is very small and
# will decrease rapidly. 
def fib_by_binet_approx(n):
    if n < 0:
        raise ValueError("n must not be negative.")

    sqrt5 = math.sqrt(5)
    return int(round((((1 + sqrt5) / 2) ** n) / sqrt5))

if __name__ == "__main__":
    print "Calculating Fibonacci numbers:"
    print "fib_by_recursive:",
    for i in range(11):
        print fib_by_recursive(i),
    print
    print "fib_by_loop:",
    for i in range(11):
        print fib_by_loop(i),
    print
    print "fib_by_dp:",
    for n in fib_by_dp(10):
        print n,
    print
    print "fib_by_cache:",
    for i in range(11):
        print fib_by_cache(i),
    print
    print "fib_by_matrix:",
    for i in range(11):
        print fib_by_matrix(i),
    print
    print "fib_by_binet:",
    for i in range(11):
        print fib_by_binet(i),
    print
    print "fib_by_binet_approx:",
    for i in range(11):
        print fib_by_binet_approx(i),
    print
