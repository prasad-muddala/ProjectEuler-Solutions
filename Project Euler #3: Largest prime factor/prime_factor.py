import sys

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    i = 2
    largest_prime = 2
    while i*i <= N:
        while N % i == 0:
            largest_prime = i
            N //= i    
        i += 1
    if N>largest_prime:
        largest_prime = N;
    print(largest_prime)
