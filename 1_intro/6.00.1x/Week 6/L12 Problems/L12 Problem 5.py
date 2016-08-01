# Write a generator, genPrimes, that returns the sequence of prime numbers on
# successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    primes = []
    prime = 1
    while True:
        prime += 1
        for number in primes:
            if prime % number == 0:
                break
        else:
            primes.append(prime)
            yield prime