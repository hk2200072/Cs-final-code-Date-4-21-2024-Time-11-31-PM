import random
import math

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def generate_prime(bit_length):
    while True:
        prime = random.getrandbits(bit_length)
        if is_prime(prime):
            return prime

def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1, y0, y1 = x1, x0 - q * x1, y1, y0 - q * y1
    if y0 < 0:  # Ensure that y0 is non-negative
        y0 += b
    return a, x0, y0

def encrypt(message, e, n):
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

bit_length = int(input("Enter the number of bits needed for prime numbers: "))

half_bit_length = bit_length // 2

p = generate_prime(half_bit_length)
q = generate_prime(half_bit_length)

while p == q:
    q = generate_prime(half_bit_length)

n = p * q
phi_n = (p - 1) * (q - 1)
e = random.randint(3, phi_n - 1)

while math.gcd(e, phi_n) != 1:
    e += 1

d = extended_gcd(e, phi_n)[1]

if d < 0:
    d += phi_n  # Make d positive if it's negative

print("p:", p)
print("q:", q)
print("\nPublic key (e, n) is:")
print("e:", e)
print("n:", n)
print("\nPrivate key (d, n) is:")
print("d:", d)
print("n:", n)
print("\nphi_n:", phi_n)

word = input("\nEnter a word to encrypt: ")
encrypted_word = encrypt(word, e, n)
print("Encrypted word:", encrypted_word)
