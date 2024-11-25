numbers = []
for i in range(1,16):
    numbers += [i]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(1, len(numbers)+1):
    is_prime = True
    if i == 1:
        continue
    else:
        for j in range(2, i-1):
            if i % j == 0:
                is_prime = False
            else:
                break
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)


print(primes)
print(not_primes)