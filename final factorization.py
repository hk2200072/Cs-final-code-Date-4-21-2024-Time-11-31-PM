import math
import time

def factorize_number(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def calc_d(e, phi_n):
    calc_d = pow(e, -1, phi_n)
    return calc_d

def calculate_private_key(e, phi):
    start_time = time.perf_counter_ns()

    private_key = calc_d(e, phi)

    end_time = time.perf_counter_ns()
    runtime = (end_time - start_time) / 1e6  # Convert to milliseconds

    return private_key, runtime

public_key_n = int(input("Enter the public key n: "))
public_key_e = int(input("Enter the public key e: "))

prime_factors = factorize_number(public_key_n)

if len(prime_factors) == 2:
    prime_p, prime_q = prime_factors
    phi_n = (prime_p - 1) * (prime_q - 1)
    private_key, runtime = calculate_private_key(public_key_e, phi_n)
    print("RSA Parameters:")
    print("Prime p:", prime_p)
    print("Prime q:", prime_q)
    print("Phi(n):", phi_n)
    print("Public Key n:", public_key_n)
    print("Public Key e:", public_key_e)
    print("Private Key d:", private_key)
    print("Runtime (ms):", runtime)