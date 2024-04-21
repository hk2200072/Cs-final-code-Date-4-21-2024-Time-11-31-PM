import time

def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

# User input for N, E, ciphertext
n = int(input("Enter N: "))
e = int(input("Enter E: "))
ciphertext = int(input("Enter the ciphertext: "))

# Calculate p and q
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        q = i
        p = n // i
        break

print("p:", p)
print("q:", q)

# Calculate private key
phi_n = (p - 1) * (q - 1)
d = pow(e, -1, phi_n)  # Modular multiplicative inverse of e modulo phi_n
private_key = (d, n)

# Output the value of d
print("Private key exponent (d):", d)

# Decrypt ciphertext
decrypted_message = decrypt([ciphertext], private_key)
print("Decrypted message:", decrypted_message)
