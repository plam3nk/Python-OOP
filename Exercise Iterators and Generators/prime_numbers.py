def get_primes(numbers):
    for num in numbers:
        prime = True
        if num >= 2:
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                yield num


print(list(get_primes([-2, 0, 0, 1, 1, 0])))
