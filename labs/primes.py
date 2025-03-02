# generate primes

primes = []
upto = 100000
for candidate in range(2, upto):
    is_prime = True
    # only need to check if divisable by primes
    for divisor in range(2, candidate):
        # if divisable by any int, it is not a prime number
        if (candidate % divisor == 0):
            is_prime = False
            # so there is no reason to keep checking
            break
    if is_prime:
        primes.append(candidate)

print(primes)

for candidate in range(2, 100):
    is_prime = True
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(candidate)