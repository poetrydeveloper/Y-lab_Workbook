def get_prime_factorials(n) -> list[int]:
    i = 2
    prime_factorials = []
    while i * i <= n:
        while n % i == 0:
            prime_factorials.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prime_factorials.append(int(n))
    return prime_factorials


def count_find_num(a, b):
    for i in range(2, b + 1):
        d = get_prime_factorials(i)
        if set(a).issubset(set(d)):
            print(i, d)


primesL = [2, 5, 7]
limit = 500

count_find_num(primesL, limit)
