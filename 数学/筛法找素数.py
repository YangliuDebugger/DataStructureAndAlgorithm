# 找出n以内的所有素数
import time


def easy_sieve(n):
    """
    埃氏筛法
    Time complexity: O(nloglogn)
    """
    prime = [1] * (n+1)
    prime[0] = prime[1] = 0
    i = 2
    while i * i <= n:
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = 0
        i += 1
    return [idx for idx, v in enumerate(prime) if v]


def euler_sieve(n):
    """
    欧拉线性筛法
    Time complexity: O(n)
    """
    visit = [0] * (n+1)
    prime = [0] * (n+1)
    for i in range(2, n+1):
        if not visit[i]:
            prime[0] += 1
            prime[prime[0]] = i
        for j in range(1, prime[0]+1):
            if i * prime[j] > n:
                break
            visit[i * prime[j]] = 1
            if i % prime[j] == 0:
                break
    return prime[1:prime[0]+1]


def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


start = time.perf_counter()
print(len(easy_sieve(10000000)))
print(time.perf_counter() - start)

start = time.perf_counter()
print(len(euler_sieve(10000000)))
print(time.perf_counter() - start)

start = time.perf_counter()
print(len(rwh_primes(10000000)))
print(time.perf_counter() - start)

start = time.perf_counter()
print(len(rwh_primes1(10000000)))
print(time.perf_counter() - start)

# Leetcode Python 3 playground running time, rwh_prime is fast is because is slice assignment is fast in python
# easy_sieve: 2.133493348000002s
# euler_sieve: 4.5507064490000175s
# rwh_primes: 0.47547689600014564s
# rwh_primes1: 0.44516443299994535s
