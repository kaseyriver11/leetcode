
primes = [2]

i = 1
while len(primes) < 10001:
    i = i + 2
    prime = True
    for j in range(2, i):
        if (i % j) == 0:
            prime = False
            break
    if prime:
        primes.append(i)
